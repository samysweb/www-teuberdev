---
title: "An Information-Flow Perspective on Algorithmic Fairness"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Bernhard Beckert

date: "2024-02-20T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-12-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: The 38th Annual AAAI Conference on Artificial Intelligence
publication_short: In AAAI 2024

abstract: |2-
  This work presents insights gained by investigating the relationship between algorithmic fairness and the concept of secure information flow. The problem of enforcing secure information flow is well-studied in the context of information security: If secret information may "flow" through an algorithm or program in such a way that it can influence the program's output, then that is considered insecure information flow as attackers could potentially observe (parts of) the secret.
  There is a strong correspondence between secure information flow and algorithmic fairness: if protected attributes such as race, gender, or age are treated as secret program inputs, then secure information flow means that these "secret" attributes cannot influence the result of a program. While most research in algorithmic fairness evaluation concentrates on studying the impact of algorithms (often treating the algorithm as a black-box), the concepts derived from information flow can be used both for the analysis of disparate treatment as well as disparate impact w.r.t. a structural causal model.
  In this paper, we examine the relationship between quantitative as well as qualitative information-flow properties and fairness. Moreover, based on this duality, we derive a new quantitative notion of fairness called fairness spread, which can be easily analyzed using quantitative information flow and which strongly relates to counterfactual fairness. We demonstrate that off-the-shelf tools for information-flow properties can be used in order to formally analyze a program's algorithmic fairness properties, including the new notion of fairness spread as well as established notions such as demographic parity. 

# Summary. An optional shortened abstract.
summary: An exploration of the relationships between qualitative and quantitative information flow and various causal and non-causal fairness definitions with applications to program analysis.

tags:
- Algorithmic Fairness
- Formal Methods
- Program Analysis

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
#  - name: CEUR-
#    url: https://ceur-ws.org/Vol-3442/paper-21.pdf

url_pdf: 'https://arxiv.org/abs/2312.10128'
url_code: 'https://zenodo.org/records/10385361'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
url_poster: '/media/pdf/AAAI_24_Poster.pdf'
url_project: ''
url_slides: ''
url_source: ''
#url_video: 'https://www.youtube.com/watch?v=xUysflQIftE&t=3083s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'The computation of the german wage tax uses religious affiliation as an input. This is necessary to compute the church tax. But does it inadvertedly modify other outputs?'
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
