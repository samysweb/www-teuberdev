---
title: "Quantifying Software Reliability via Model-Counting"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Alexander Weigl


date: "2021-08-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-06-27T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: International Conference on Quantitative Evaluation of SysTems 2021 (Upcoming)
publication_short: In QEST 2021

abstract: |2-
    Critical software should be verified. But how to handle the
    situation when a proof for the functional correctness could not be
    established? In this case, an assessment of the software is required
    to estimate the risk of using the software.

    In this paper, we contribute to the assessment of critical software
    with a formal approach to measure the reliability of the software
    against its functional specification. We support bounded C-programs
    precisely where the functional specification is given as assumptions
    and assertions within the source code. We count and categorize the
    various program runs to compute the reliability as the ratio of
    failing program runs (violating an assertion) to all terminating
    runs. Our approach consists of a preparing program translation, the
    reduction of C-program into SAT instances via software-bounded
    model-checker (CBMC), and precise or approximate model-counting
    providing a reliable assessment. We evaluate our prototype
    implementation on over 24 examples with different model-counters. We
    show the feasibility of our pipeline and benefits against
    competitors.

# Summary. An optional shortened abstract.
summary: We present and evaluate a pipeline allowing for the quantification of C-programs according to their specification adherence.

tags:
- Formal Methods
- Quantification

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
links:
 - name: Experiments
   url: 'https://github.com/samysweb/counterSharp-experiments'

#url_pdf: 'https://arxiv.org/pdf/2008.10061.pdf'
url_code: 'https://github.com/samysweb/counterSharp'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'A pipeline for software quantification'
  focal_point: ""
  preview_only: false

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
