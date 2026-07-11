<p align="center"><a href="https://wowchemy.com" target="_blank" rel="noopener"><img src="https://wowchemy.com/img/logo_200px.png" alt="Wowchemy Website Builder"></a></p>

# Academic Template for [Hugo](https://github.com/gohugoio/hugo)

The Hugo **Academic Resumé Template** empowers you to create your job-winning online resumé and showcase your academic publications.

[Check out the latest demo](https://academic-demo.netlify.app) of what you'll get in less than 10 minutes, or [view the showcase](https://wowchemy.com/user-stories/).

[**Wowchemy**](https://wowchemy.com) makes it easy to create a beautiful website for free. Edit your site in Markdown, Jupyter, or RStudio (via Blogdown), generate it with Hugo, and deploy with GitHub or Netlify. Customize anything on your site with widgets, themes, and language packs.

- 👉 [**Get Started**](https://wowchemy.com/docs/install/)
- 📚 [View the **documentation**](https://wowchemy.com/docs/)
- 💬 [Chat with the **Wowchemy community**](https://discord.gg/z8wNYzb) or [**Hugo community**](https://discourse.gohugo.io)
- 🐦 Twitter: [@wowchemy](https://twitter.com/wowchemy) [@GeorgeCushen](https://twitter.com/GeorgeCushen) [#MadeWithWowchemy](https://twitter.com/search?q=(%23MadeWithWowchemy%20OR%20%23MadeWithAcademic)&src=typed_query)
- 💡 [Request a **feature** or report a **bug** for _Wowchemy_](https://github.com/wowchemy/wowchemy-hugo-modules/issues)
- ⬆️ **Updating Wowchemy?** View the [Update Guide](https://wowchemy.com/docs/update/) and [Release Notes](https://wowchemy.com/updates/)

## Crowd-funded open-source software

To help us develop this template and software sustainably under the MIT license, we ask all individuals and businesses that use it to help support its ongoing maintenance and development via sponsorship.

### [❤️ Click here to unlock rewards with sponsorship](https://wowchemy.com/plans/)

## Ecosystem

* **[Wowchemy Admin](https://github.com/wowchemy/wowchemy-admin/):** An admin tool to import publications from BibTeX

[![Screenshot](https://raw.githubusercontent.com/wowchemy/wowchemy-hugo-modules/master/academic.png)](https://wowchemy.com)

<!--
[![Analytics](https://ga-beacon.appspot.com/UA-78646709-2/academic-kickstart/readme?pixel)](https://github.com/igrigorik/ga-beacon)
-->

## CV LaTeX Frontend (Hugo)

This repository now contains a second frontend that renders a LaTeX CV from the same website data.

### Output target

- CV entry point: `content/cv/_index.md`
- Output format: `CVTex` (configured in `config/_default/hugo.yaml`)
- Main template: `layouts/cv/list.cvtex.tex`

### CV data files

- Public CV data: `data/cv/public.yaml`
- Service data: `data/cv/service.yaml`
- Private local CV data template: `data/cv/private.example.yaml`
- Private local CV data (ignored by git): `data/cv/private.yaml`

Create your local private file like this:

```bash
cp data/cv/private.example.yaml data/cv/private.yaml
```

### TeX flags (in generated `cv.tex`)

The generated file defines TeX booleans with `\newif` and defaults from `data/cv/public.yaml`:

- `\ifresearchfull`
- `\iftalksinvitedonly`
- `\ifshowstudentsupervision`
- `\ifshowprivatefields`

You can flip them directly in the generated `.tex` before LaTeX compilation.

### Talks schema

All talks under `content/talk/*.md` now include:

```yaml
talk_kind: invited|contributed
```

This is used by the CV rendering to split/filter talks.

### Service schema

`data/cv/service.yaml` uses normalized roles:

- `conference_review`
- `subreview`
- `journal_review`

Extension is possible via:

```yaml
role: custom
role_custom: "Program Committee"
```

Recommended fields per entry:

- `venue`
- `year` (string, supports values like `2024/2025`)
- `note` (optional)

### Research interests

Both fields are always maintained in `data/cv/public.yaml`:

- `research_interests_text`
- `research_interests_bullets`

Selection is controlled by the TeX flag `\ifresearchfull`.