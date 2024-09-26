---
title: "Provably Safe Neural Network Controllers via Differential Dynamic Logic"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Stefan Mitsch
- André Platzer

date: "2024-12-10T00:00:00Z"
#doi: "10.1145/3605098.3636008"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-02-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: Thirty-Eighth Annual Conference on Neural Information Processing Systems
publication_short: In NeurIPS 2024

abstract: |2-
  While neural networks (NNs) have a large potential as goal-oriented controllers for Cyber-Physical Systems, verifying the safety of neural network based control systems (NNCSs) poses significant challenges for the practical use of NNs -- especially when safety is needed for unbounded time horizons. One reason for this is the intractability of NN and hybrid system analysis. We introduce VerSAILLE (Verifiably Safe AI via Logically Linked Envelopes): The first approach for the combination of differential dynamic logic (dL) and NN verification. By joining forces, we can exploit the efficiency of NN verification tools while retaining the rigor of dL. We reflect a safety proof for a controller envelope in an NN to prove the safety of concrete NNCS on an infinite-time horizon. The NN verification properties resulting from VerSAILLE typically require nonlinear arithmetic while efficient NN verification tools merely support linear arithmetic. To overcome this divide, we present Mosaic: The first sound and complete verification approach for polynomial real arithmetic properties on piece-wise linear NNs. Mosaic lifts off-the-shelf tools for linear properties to the nonlinear setting. An evaluation on case studies, including adaptive cruise control and airborne collision avoidance, demonstrates the versatility of VerSAILLE and Mosaic: It supports the certification of infinite-time horizon safety and the exhaustive enumeration of counterexample regions while significantly outperforming State-of-the-Art tools in closed-loop NNV.

# Summary. An optional shortened abstract.
summary: We present the first approach for the combination of differential dynamic logic (dL) and NN verification. By joining forces, we can exploit the efficiency of NN verification tools while retaining the rigor of dL. This yields infinite-time horizon safety guarantees for neural network control systems.

tags:
- Cyber-Physical Systems
- Neural Network Verification 
- Formal Methods
- Differential Dynamic Logic
- Dynamic Logic
- Infinite-Time Horizon Safety

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
#  - name: CEUR-
#    url: https://ceur-ws.org/Vol-3442/paper-21.pdf

url_pdf: 'https://arxiv.org/abs/2402.10998'
#url_code: 'https://zenodo.org/records/10385361'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
#url_poster: '/media/pdf/AAAI_24_Poster.pdf'
url_project: 'https://github.com/samysweb/NCubeV'
url_slides: 'https://github.com/samysweb/VerSAILLE/blob/c489a056defa09012c7c9077db57209246d4ee99/documents/Teuber-SAIV-2024.pdf'
url_source: ''
#url_video: 'https://www.youtube.com/watch?v=xUysflQIftE&t=3083s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
   caption: 'Overview of the approach'
   #Based on a valid dL-contract, VerSAILLE produces NN verification properties that allow the verification of infinite-time safety. In order to verify such properties, we require a tool for the verification of nonlinear properties on neural network -- this is the task of our new tool Mosaic.
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
