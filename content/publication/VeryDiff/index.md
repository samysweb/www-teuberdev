---
title: "Revisiting Differential Verification: Equivalence Verification with Confidence"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Philipp Kern
- Marvin Janzen
- Bernhard Beckert

date: "2024-10-28T00:00:00Z"
doi: "10.48550/arXiv.2410.20207"

# Schedule page publish date (NOT publication's date).
publishDate: "2023-10-28T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["manuscript"]

# Publication name and optional abbreviated publication name.
#publication: 
#publication_short: 

abstract: |2-
  When validated neural networks (NNs) are pruned (and retrained) before deployment, it is desirable to prove that the new NN behaves equivalently to the (original) reference NN. To this end, our paper revisits the idea of differential verification which performs reasoning on differences between NNs: On the one hand, our paper proposes a novel abstract domain for differential verification admitting more efficient reasoning about equivalence. On the other hand, we investigate empirically and theoretically which equivalence properties are (not) efficiently solved using differential reasoning. Based on the gained insights, and following a recent line of work on confidence-based verification, we propose a novel equivalence property that is amenable to Differential Verification while providing guarantees for large parts of the input space instead of small-scale guarantees constructed w.r.t. predetermined input points. We implement our approach in a new tool called VeryDiff and perform an extensive evaluation on numerous old and new benchmark families, including new pruned NNs for particle jet classification in the context of CERN's LHC where we observe median speedups >300x over the State-of-the-Art verifier alpha,beta-CROWN. 

# Summary. An optional shortened abstract.
#summary: We evaluate the potential of Large Language Models (specifically GPT 3.5 and GPT 4o) for the generation of code annotations in the Java Modelling Language using a prototypical integration of the Java verification tools KeY and JJBMC with OpenAI's API.

tags:
- Formal Methods
- Neural Network Verification 
- Compression
- Equivalence
- Differential Verification

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
#  - name: DOI
#    url: https://doi.org/10.1007/978-3-031-75387-9_15

url_pdf: 'https://arxiv.org/pdf/2410.20207'
#url_code: ''
#url_dataset: ''
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: ''
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