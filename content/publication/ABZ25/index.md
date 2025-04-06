---
title: "Verification of Autonomous Neural Car Control with KeYmaera X"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Enguerrand Prebet
- admin
- André Platzer

date: "2025-06-10T00:00:00Z"
#doi: "10.1145/3605098.3636008"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-04-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: 11th International Conference on Rigorous State Based Methods
publication_short: In ABZ 2025

abstract: |2-
  This article presents a formal model and formal safety proofs for the ABZ'25 case study in differential dynamic logic (dL). The case study considers an autonomous car driving on a highway avoiding collisions with neighbouring cars. Using KeYmaera X's dL implementation, we prove absence of collision on an infinite time horizon which ensures that safety is preserved independently of trip length. The safety guarantees hold for time-varying reaction time and brake force. Our dL model considers the single lane scenario with cars ahead or behind. We demonstrate that dL with its tools is a rigorous foundation for runtime monitoring, shielding, and neural network verification. Doing so sheds light on inconsistencies between the provided specification and simulation environment highway-env of the ABZ'25 study. We attempt to fix these inconsistencies and uncover numerous counterexamples which also indicate issues in the provided reinforcement learning environment.

# Summary. An optional shortened abstract.
summary: We apply differential dynamic (refinement) logic to a case study on neural highway control. After modelling the abstract system we use VerSAILLE and the NCubeV tool [NeurIPS24] to (dis)prove the safety of concrete neural networks. Along the way we uncover numerous interesting results on the highway-env simulation environment including inconsistencies between the provided specification and the actual simulation.

tags:
- Cyber-Physical Systems
- Neural Network Verification 
- Formal Methods
- Differential Dynamic Logic
- Dynamic Logic
- Infinite-Time Horizon Safety
- Case Study

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
links:
 - name: Teaching Resources
   url: https://github.com/samysweb/versaille

url_pdf: '#TODO'
#url_code: 'https://zenodo.org/records/10385361'
#url_dataset: 'https://github.com/samysweb/counterSharp-experiments'
#url_poster: '/media/pdf/AAAI_24_Poster.pdf'
url_code: 'https://github.com/LS-Lab/Verified-Neural-Highway-Control'
#url_slides: ''
url_source: ''
#url_video: 'https://www.youtube.com/watch?v=xUysflQIftE&t=3083s'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
   caption: "The ABZ'25 Case Study Challenge featured a neural network controlled car. Our contribution solves this case study based on the rigorous foundations of differential dynamic logic in combination with neural network verification as described in our recent NeurIPS'24 paper: We prove safety for the abstract model and derive specifications for the neural network."
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
