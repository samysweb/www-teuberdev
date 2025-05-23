---
title: "Formally Verified Algorithmic Fairness using Information-Flow Tools (Extended Abstract)"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Bernhard Beckert

date: "2023-05-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-06-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["Workshop Paper"]

# Publication name and optional abbreviated publication name.
publication: 2nd European Workshop on Algorithmic Fairness 2023
publication_short: In EWAF 2023

abstract: |2-
  This work presents results on the use of Information-Flow tools for the formal verification of algorithmic fairness properties. The problem of enforcing secure information-flow was originally studied in the context of information security: If secret information may "flow" through an algorithm in such a way that it can influence the program’s output, we consider that to be insecure information-flow as attackers could potentially observe (parts of) the secret. Due to its wide-spread use, there exist numerous tools for analyzing secure information-flow properties. Recent work showed that there exists a strong correspondence between secure information-flow and algorithmic fairness:
  If protected group attributes are treated as secret program inputs, then secure information-flow means that these "secret" attributes cannot influence the result of a program. We demonstrate that off-the-shelf tools for information-flow can be used to formally analyze algorithmic fairness properties including established notions such as (conditional) demographic parity as well as a new quantitative notion named fairness spread.

# Summary. An optional shortened abstract.
summary: We demonstrate preliminary results on strong connections between Information Flow and Algorithmic Fairness Analysis

tags:
- Formal Methods
- Algorithmic Fairness
- Program Analysis

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
#  - name: CEUR-
#    url: https://ceur-ws.org/Vol-3442/paper-21.pdf

url_pdf: 'https://ceur-ws.org/Vol-3442/paper-21.pdf'
#url_code: 'https://github.com/samysweb/nnequiv'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
url_poster: ''
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
