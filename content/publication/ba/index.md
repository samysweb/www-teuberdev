---
title: "An Incremental Abstraction Scheme for Solving Hard SMT-Instances over Bit-Vectors"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Marko Kleine Büning
- Carsten Sinz


date: "2020-08-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2020-08-23T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
#publication: In *Wowchemy Conference*
#publication_short: In *ICW*

abstract: |2-
    Decision procedures for SMT problems based on the theory of bit-vectors are a fundamental component in state-of-the-art software and hardware verifiers. While very efficient in general, certain SMT instances are still challenging for state-of-the-art solvers (especially when such instances include computationally costly functions). In this work, we present an approach for the quantifier-free bit-vector theory (QF_BV in SMT-LIB) based on incremental SMT solving and abstraction refinement. We define four concrete approximation steps for the multiplication, division and remainder operators and combine them into an incremental abstraction scheme. We implement this scheme in a prototype extending the SMT solver Boolector and measure both the overall performance and the performance of the single approximation steps. The evaluation shows that our abstraction scheme contributes to solving more unsatisfiable benchmark instances, including seven instances with unknown status in SMT-LIB. 

# Summary. An optional shortened abstract.
summary: We define four concrete approximation steps for the multiplication, division and remainder operators and combine them into an incremental abstraction scheme.

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2008.10061.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Part of the abstraction refinement algorithm developed in my Bachelor Thesis'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- ba

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
