---
title: "Quantifying Software Correctness by Combining Architecture Modeling and Formal Program Analysis"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Florian Lanzinger
- Christian Martin
- Frederik Reiche
- admin
- Robert Heinrich
- Alexander Weigl

date: "2024-01-08T00:00:00Z"
doi: "10.1145/3605098.3636008"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-01-25T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: The 39th ACM/SIGAPP Symposium on Applied Computing
publication_short: In SAC 2024

abstract: |2-
  Most formal methods see the correctness of a software system as a binary decision. However, proving the correctness of complex systems completely is difficult because they are composed of multiple components, usage scenarios, and environments. We present QuAC, a modular approach for quantifying the correctness of service-oriented software systems by combining software architecture modeling with deductive verification. Our approach is based on a model of the service-oriented architecture and the probabilistic usage scenarios of the system. The correctness of a single service is approximated by a coverage region, which is a formula describing which inputs for that service are proven to not lead to an erroneous execution. The coverage regions can be determined by a combination of various analyses, e.g., formal verification, expert estimations, or testing. The coverage regions and the software model are then combined into a probabilistic program. From this, we can compute the probability that under a given usage profile no service is called outside its coverage region. If the coverage region is large enough, then instead of attempting to get 100% coverage, which may be prohibitively expensive, run-time verification or testing approaches may be used to deal with inputs outside the coverage region. We also present an implementation of QuAC for Java using the modeling tool Palladio and the deductive verification tool KeY. We demonstrate its usability by applying it to a software simulation of an energy system.

# Summary. An optional shortened abstract.
summary: A formal approach for the quantiative assessment of service-oriented software which combines high-level software architecture modelling with deductive verification.

tags:
- Formal Methods
- Program Analysis
- Quantification

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
#  - name: CEUR-
#    url: https://ceur-ws.org/Vol-3442/paper-21.pdf

url_pdf: 'https://arxiv.org/abs/2401.14320'
#url_code: 'https://zenodo.org/records/10385361'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
#url_poster: '/media/pdf/AAAI_24_Poster.pdf'
url_project: ''
url_slides: ''
url_source: ''
#url_video: 'https://www.youtube.com/watch?v=xUysflQIftE&t=3083s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#   caption: 'The computation of the german wage tax uses religious affiliation as an input. This is necessary to compute the church tax. But does it inadvertedly modify other outputs?'
#   focal_point: ""
#   preview_only: false

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
