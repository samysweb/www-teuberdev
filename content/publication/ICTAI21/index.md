---
title: "Geometric Path Enumeration for Equivalence Verification of Neural Networks"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Marko Kleine Büning
- Philipp Kern
- Carsten Sinz

date: "2021-12-21T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-12-26T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: 2021 IEEE 33rd International Conference on Tools with Artificial Intelligence
publication_short: In ICTAI 2021

abstract: |2-
  As neural networks (NNs) are increasingly introduced into safety-critical domains, there is a growing need to formally verify NNs before deployment. In this work we focus on the formal verification problem of NN equivalence which aims to prove that two NNs (e.g. an original and a compressed version) show equivalent behavior. Two approaches have been proposed for this problem: Mixed integer linear programming and interval propagation. While the first approach lacks scalability, the latter is only suitable for structurally similar NNs with small weight changes.
  The contribution of our paper has four parts. First, we show a theoretical result by proving that the epsilon-equivalence problem is coNP-complete. Secondly, we extend Tran et al.’s single NN geometric path enumeration algorithm to a setting with multiple NNs. In a third step, we implement the extended algorithm for equivalence verification and evaluate optimizations necessary for its practical use. Finally, we perform a comparative evaluation showing use-cases where our approach outperforms the previous state of the art, both, for equivalence verification as well as for counter-example finding.

# Summary. An optional shortened abstract.
summary: We present and evaluate an approach for proving equivalence properties on neural networks and show that the verification of $\epsilon$-equivalence is coNP-complete

tags:
- Formal Methods
- Neural Network Verification 
- Compression
- Equivalence
- Geometric Path Enumeration

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
links:
 - name: Experiments
   url: 'https://github.com/samysweb/nnequiv-experiments'
 - name: DOI / IEEE Xplore
   url: https://doi.org/10.1109/ICTAI52525.2021.00035

url_pdf: 'https://arxiv.org/pdf/2112.06582.pdf'
url_code: 'https://github.com/samysweb/nnequiv'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
#url_video: 'https://www.youtube.com/watch?v=xUysflQIftE&t=3083s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Using Geometric Path Enumeration for multiple networks enables equivalence verification.'
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
