---
title: "Heterogeneous Dynamic Logic: Provability Modulo Program Theories"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Mattias Ulbrich
- André Platzer
- Bernhard Beckert

date: "2025-07-11T00:00:00Z"
#doi: "10.1145/3605098.3636008"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-07-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["preprint"]

# Publication name and optional abbreviated publication name.

abstract: |2-
  Formally specifying, let alone verifying, properties of systems involving multiple programming languages is inherently challenging. We introduce Heterogeneous Dynamic Logic (HDL), a framework for combining reasoning principles from distinct (dynamic) program logics in a modular and compositional way. HDL mirrors the architecture of satisfiability modulo theories (SMT): Individual dynamic logics, along with their calculi, are treated as dynamic theories that can be flexibly combined to reason about heterogeneous systems whose components are verified using different program logics. HDL provides two key operations: Lifting extends an individual dynamic theory with new program constructs (e.g., the havoc operation or regular programs) and automatically augments its calculus with sound reasoning principles for the new constructs; and Combination enables cross-language reasoning in a single modality via Heterogeneous Dynamic Theories, facilitating the reuse of existing proof infrastructure. We formalize dynamic theories, their lifting and combination in Isabelle, and prove the soundness of all proof rules. We also prove relative completeness theorems for lifting and combination: Under common assumptions, reasoning about lifted or combined theories is no harder than reasoning about the constituent dynamic theories and their common first-order structure (i.e., the "data theory"). We demonstrate HDL's utility by verifying an automotive case study in which a Java controller (formalized in Java dynamic logic) steers a plant model (formalized in differential dynamic logic). 

# Summary. An optional shortened abstract.
summary: |2-
  We introduce Heterogeneous Dynamic Logic (HDL), a framework for combining reasoning principles from distinct (dynamic) program logics in a modular and compositional way. HDL mirrors the architecture of satisfiability modulo theories (SMT)

tags:
- Dynamic Logic
- Program Logics
- Formal Methods
- Heterogeneous Systems
- Differential Dynamic Logic
- Cyber-Physical Systems

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
#  - name: Teaching Resources
#    url: 

url_pdf: 'https://arxiv.org/pdf/2507.08581'
#url_code: 'https://zenodo.org/records/10385361'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
#url_poster: '/media/pdf/AAAI_24_Poster.pdf'
#url_code: 'https://github.com/LS-Lab/Verified-Neural-Highway-Control'
#url_slides: ''
#url_source: ''
#url_video: 'https://www.youtube.com/watch?v=xUysflQIftE&t=3083s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#    caption: ""
#    focal_point: ""
#    preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#- ba

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
