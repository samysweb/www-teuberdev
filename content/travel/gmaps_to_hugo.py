#!/usr/bin/env python3
"""
Converts a Google Takeout "Saved" export (Maps > Saved) into Hugo content
stubs for the travel guide: content/travel/<list>/<place>.md, with
title/latitude/longitude already filled in where they could be resolved.

Usage:
    python3 gmaps_to_hugo.py "Takeout/Maps (your places)/Saved" content/travel
    python3 gmaps_to_hugo.py "Takeout/Maps (your places)/Saved" content/travel --google-api-key=AIza...

Input (one of):
  - A folder of CSV files (one per Google Maps list). Column names are
    read in German first, falling back to English:
      Titel/Title, Notiz/Note, URL, Tags, Kommentar/Comment
    Blank separator rows (no Titel) are skipped. The CSV filename (e.g.
    "Karlsruhe.csv") becomes both the output folder and the geocoding
    context ("<title>, Karlsruhe") for disambiguation.
  - A single .json/.geojson file ("Saved Places.json", which despite the
    extension is GeoJSON) — coordinates are read directly, no requests
    needed at all.

Coordinate resolution for CSV rows, in order (stops at the first hit):
  1. Regex match directly on the URL text (works if it already has
     "/@lat,lng/" or "!3d..!4d..").
  2. Fetching the URL and checking where the server redirects to.
  3. The CID trick: some Takeout URLs only contain a feature id
     ("!1s0x...:0x<CID_HEX>"). Rebuilding it as
     https://www.google.com/maps?cid=<decimal> and following that used
     to redirect to a URL with coordinates; Google has been inconsistent
     about honouring this server-side, so treat it as a bonus, not a
     guarantee.
  4. Geocoding by name: "<Titel>, <list name>" is sent to either the
     Google Places API (Text Search, New) if --google-api-key is given,
     or to the free OpenStreetMap Nominatim search otherwise. This is
     the most reliable fallback but is a *search*, not a lookup of the
     exact saved place, so review the result.

Only stdlib is used (urllib), nothing to pip install. Re-running is
safe: existing files are skipped unless --overwrite is passed.
"""
import csv
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

COORD_PATTERNS = [
    re.compile(r"!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)"),   # precise pin, in "data=" param
    re.compile(r"/@(-?\d+\.\d+),(-?\d+\.\d+)"),       # map center fallback
]
CID_PATTERN = re.compile(r"!1s0x[0-9a-fA-F]+:0x([0-9a-fA-F]+)")
NOMINATIM_MIN_INTERVAL = 1.0  # seconds; required by Nominatim's usage policy
_last_nominatim_call = 0.0


def slugify(text: str) -> str:
    text = (text or "").strip()
    replacements = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
                     "Ä": "Ae", "Ö": "Oe", "Ü": "Ue"}
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "spot"


def _match_coords(text: str):
    for pat in COORD_PATTERNS:
        m = pat.search(text)
        if m:
            return float(m.group(1)), float(m.group(2))
    return None


def _fetch_final_url(url: str, timeout: float):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.geturl()
    except Exception as e:
        print(f"    ! Konnte URL nicht abrufen ({url}): {e}")
        return None


def coords_from_url(url: str, timeout: float = 10.0):
    """Steps 1-3: everything that can be derived from the URL alone."""
    if not url:
        return None

    coords = _match_coords(url)
    if coords:
        return coords

    final = _fetch_final_url(url, timeout)
    if final:
        coords = _match_coords(final)
        if coords:
            return coords

    cid_match = CID_PATTERN.search(url)
    if cid_match:
        cid_decimal = int(cid_match.group(1), 16)
        cid_url = f"https://www.google.com/maps?cid={cid_decimal}"
        final = _fetch_final_url(cid_url, timeout)
        if final:
            coords = _match_coords(final)
            if coords:
                return coords

    return None


def geocode_google(query: str, api_key: str, timeout: float = 10.0):
    """Step 4a: Google Places API - Text Search (New)."""
    url = "https://places.googleapis.com/v1/places:searchText"
    body = json.dumps({"textQuery": query}).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "places.location,places.displayName",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"    ! Places API Fehler fuer '{query}': {e}")
        return None
    places = data.get("places") or []
    if not places:
        return None
    loc = places[0].get("location") or {}
    lat, lng = loc.get("latitude"), loc.get("longitude")
    if lat is None or lng is None:
        return None
    return float(lat), float(lng)


def geocode_nominatim(query: str, timeout: float = 10.0):
    """Step 4b: free fallback via OpenStreetMap Nominatim. Rate-limited to
    1 req/sec as required by Nominatim's usage policy, regardless of the
    script's own --sleep setting."""
    global _last_nominatim_call
    wait = NOMINATIM_MIN_INTERVAL - (time.monotonic() - _last_nominatim_call)
    if wait > 0:
        time.sleep(wait)
    _last_nominatim_call = time.monotonic()

    qs = urllib.parse.urlencode({"q": query, "format": "json", "limit": 1})
    url = f"https://nominatim.openstreetmap.org/search?{qs}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "teuberdev-travel-guide-import/1.0 (personal, low-volume use)"
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            results = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"    ! Nominatim Fehler fuer '{query}': {e}")
        return None
    if not results:
        return None
    r = results[0]
    return float(r["lat"]), float(r["lon"])


def resolve_coords(title: str, url: str, context: str, google_api_key: str,
                    use_geocode_fallback: bool, timeout: float):
    coords = coords_from_url(url, timeout)
    if coords or not use_geocode_fallback:
        return coords, (None if coords is None else "url")

    query = f"{title}, {context}".strip(", ")
    if google_api_key:
        coords = geocode_google(query, google_api_key, timeout)
        source = "google-places"
    else:
        coords = geocode_nominatim(query, timeout)
        source = "nominatim"
    return coords, (source if coords else None)


def write_stub(out_dir: Path, title: str, lat, lng, note: str, comment: str,
                tags_raw: str, source_url: str, coord_source: str, overwrite: bool):
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(title)
    path = out_dir / f"{slug}.md"
    if path.exists() and not overwrite:
        print(f"    = uebersprungen (existiert schon): {path}")
        return

    lat_line = f"latitude: {lat}\n" if lat is not None else "# TODO latitude fehlt, bitte manuell ergaenzen\n"
    lng_line = f"longitude: {lng}\n" if lng is not None else "# TODO longitude fehlt, bitte manuell ergaenzen\n"
    summary = (note or "").replace('"', "'")

    comment_lines = []
    if note:
        comment_lines.append(f"<!-- Google Notiz: {note} -->")
    if tags_raw:
        comment_lines.append(f"<!-- Google Tags: {tags_raw} -->")
    if comment:
        comment_lines.append(f"<!-- Google Kommentar: {comment} -->")
    if coord_source in ("google-places", "nominatim"):
        comment_lines.append(f"<!-- Koordinaten per {coord_source}-Suche geraten, bitte pruefen! -->")
    comment_lines.append(f"<!-- Quelle: {source_url} -->")

    content = (
        "---\n"
        f"title: {title}\n"
        f"{lat_line}"
        f"{lng_line}"
        "travel_tags: []\n"
        f"summary: \"{summary}\"\n"
        "---\n\n"
        + "\n".join(comment_lines) + "\n"
    )
    path.write_text(content, encoding="utf-8")
    status = "OK   " if lat is not None else "FEHLT"
    tag = f" ({coord_source})" if coord_source in ("google-places", "nominatim") else ""
    print(f"    {status} {title}{tag} -> {path}")


def process_csv(csv_path: Path, out_root: Path, overwrite: bool, sleep: float,
                 google_api_key: str, use_geocode_fallback: bool, timeout: float):
    list_slug = slugify(csv_path.stem)
    context = csv_path.stem  # keep umlauts etc. for nicer geocoding queries
    out_dir = out_root / list_slug
    print(f"[{csv_path.name}] -> content/travel/{list_slug}/")
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = (row.get("Titel") or row.get("Title") or row.get("Name") or "").strip()
            if not title:
                continue  # blank separator rows in the export
            note = (row.get("Notiz") or row.get("Note") or "").strip()
            comment = (row.get("Kommentar") or row.get("Comment") or "").strip()
            tags_raw = (row.get("Tags") or "").strip()
            url = (row.get("URL") or row.get("Google Maps URL") or "").strip()
            coords, coord_source = resolve_coords(
                title, url, context, google_api_key, use_geocode_fallback, timeout)
            lat, lng = coords if coords else (None, None)
            write_stub(out_dir, title, lat, lng, note, comment, tags_raw, url, coord_source, overwrite)
            time.sleep(sleep)


def process_geojson(json_path: Path, out_root: Path, overwrite: bool):
    data = json.loads(json_path.read_text(encoding="utf-8"))
    features = data.get("features", [])
    list_slug = slugify(json_path.stem)
    out_dir = out_root / list_slug
    print(f"[{json_path.name}] -> content/travel/{list_slug}/ ({len(features)} Orte)")
    for feat in features:
        props = feat.get("properties", {})
        title = props.get("name") or props.get("Title") or props.get("Titel") or "Unbenannt"
        note = props.get("note") or props.get("Note") or props.get("Notiz") or ""
        geom = feat.get("geometry") or {}
        coords = geom.get("coordinates")  # GeoJSON = [lng, lat]
        lat, lng = (coords[1], coords[0]) if coords and len(coords) >= 2 else (None, None)
        write_stub(out_dir, title, lat, lng, note, "", "", "Google Takeout GeoJSON", None, overwrite)


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 gmaps_to_hugo.py <input: CSV-Ordner oder .json/.geojson> <output: content/travel> "
              "[--overwrite] [--sleep=0.3] [--google-api-key=KEY] [--no-geocode-fallback]")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_root = Path(sys.argv[2])
    rest = sys.argv[3:]
    overwrite = "--overwrite" in rest
    use_geocode_fallback = "--no-geocode-fallback" not in rest
    sleep = 0.3
    google_api_key = ""
    timeout = 10.0
    for arg in rest:
        if arg.startswith("--sleep="):
            sleep = float(arg.split("=", 1)[1])
        elif arg.startswith("--google-api-key="):
            google_api_key = arg.split("=", 1)[1]
        elif arg.startswith("--timeout="):
            timeout = float(arg.split("=", 1)[1])

    if in_path.is_file() and in_path.suffix.lower() in (".json", ".geojson"):
        process_geojson(in_path, out_root, overwrite)
    elif in_path.is_dir():
        csvs = sorted(in_path.glob("*.csv"))
        if not csvs:
            print(f"Keine CSV-Dateien in {in_path} gefunden.")
            sys.exit(1)
        for csv_path in csvs:
            process_csv(csv_path, out_root, overwrite, sleep, google_api_key, use_geocode_fallback, timeout)
    else:
        print("Input muss ein Ordner mit CSVs oder eine .json/.geojson Datei sein.")
        sys.exit(1)

    print("\nFertig. Eintraege mit 'FEHLT' brauchen die Koordinaten von Hand. "
          "Eintraege mit '(nominatim)'/'(google-places)' wurden per Namenssuche geraten - kurz gegenpruefen.")


if __name__ == "__main__":
    main()