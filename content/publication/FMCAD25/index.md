---
title: "Of Good Demons and Bad Angels: Guaranteeing Safe Control under Finite Precision"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Debasmita Lohar
- Bernhard Beckert

date: "2025-10-06T00:00:00Z"
#doi: "10.1145/3605098.3636008"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-04-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: Formal Methods in Computer-Aided Design 2025
publication_short: In FMCAD 2025

abstract: |2-
  As neural networks (NNs) become increasingly prevalent in safety-critical neural network-controlled cyber-physical systems (NNCSs), formally guaranteeing their safety becomes crucial. For these systems, safety must be ensured throughout their entire operation, necessitating infinite-time horizon verification. To verify the infinite-time horizon safety of NNCSs, recent approaches leverage Differential Dynamic Logic (dL). However, these dL-based guarantees rely on idealized, real-valued NN semantics and fail to account for roundoff errors introduced by finite-precision implementations. This paper bridges the gap between theoretical guarantees and real-world implementations by incorporating robustness under finite-precision perturbations -- in sensing, actuation, and computation -- into the safety verification. We model the problem as a hybrid game between a good Demon, responsible for control actions, and a bad Angel, introducing perturbations. This formulation enables formal proofs of robustness w.r.t. a given (bounded) perturbation. Leveraging this bound, we employ state-of-the-art mixed-precision fixed-point tuners to synthesize sound and efficient implementations, thus providing a complete end-to-end solution. We evaluate our approach on case studies from the automotive and aeronautics domains, producing efficient NN implementations with rigorous infinite-time horizon safety guarantees.

# Summary. An optional shortened abstract.
summary: We extend the differential dynamic logic-based NN verification technique VerSAILLE (NeurIPS'24) to support verification under perturbations and leverage this result to derive end-to-end safety guarantees that carry over to fixed-point arithmetic implementations of  (originally) real-valued NNs.

tags:
- Cyber-Physical Systems
- Neural Network Verification 
- Formal Methods
- Differential Dynamic Logic
- Differential Game Logic
- Infinite-Time Horizon Safety

# Display this page in the Featured widget?
#featured: true

# Custom links (uncomment lines below)
links:
 - name: Teaching Resources
   url: https://github.com/samysweb/versaille

url_pdf: 'https://arxiv.org/pdf/2507.22760'
#url_code: 'https://zenodo.org/records/10385361'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
#url_poster: '/media/pdf/AAAI_24_Poster.pdf'
#url_code: ''
#url_slides: ''
#url_source: ''
#url_video: 'https://www.youtube.com/watch?v=xUysflQIftE&t=3083s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
   #caption: ""
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
