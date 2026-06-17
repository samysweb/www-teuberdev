---
title: "Compositional Neural-Cyber-Physical System Verification in the Interactive Theorem Prover of Your Choice"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Matthew L. Daggitt
- Ekaterina Komendantskaya
- Alistair Sirman
- Alessandro Bruni
- admin
- Josh Smart
- Grant Passmore

date: "2026-05-05T00:00:00Z"
# doi: ""

# Schedule page publish date (NOT publication's date).
# publishDate: "2023-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: Proceedings of the ACM on Programming Languages (ICFP)
publication_short: In ICFP 2026
venue_label: "ICFP'26"

abstract: |2-
  Formal verification of neuro-symbolic cyber-physical systems, such as drones, medical devices and robots, is complicated. Neural components must be trained to be optimal with respect to the available data as well as the safety specifications, and then verified using specialised solvers. Symbolic models of the "cyber" and "physical" behaviour of the system must be constructed and verified in interactive theorem provers (ITPs), often requiring mature mathematical libraries to reason about the interplay of discrete and continuous dynamics, preferably obtaining infinite time-horizon guarantees. Finally, the results of the two already challenging verification tasks need to be integrated into a single proof in a coherent and consistent way, whilst preserving deployability of the resulting model.
  In this paper we present a compositional methodology for constructing such proofs. The Vehicle framework provides a functional, domain-specific language for specifying, training, and verifying neural components. We extend Vehicle to allow integration with any ITP with minimal effort. First, we describe how Vehicle's standard bidirectional type checker can be reused to transpile neural specifications into an intermediate representation targeting multiple theorem provers. Second, we integrate Vehicle with Rocq, Isabelle/HOL, Agda and the industrial prover Imandra; and showcase a generic infinite time-horizon safety proof of a discrete cyber-physical system with a neural network controller in each ITP. Finally, we use the Mathematical Components libraries in Rocq to verify infinite time-horizon safety of a medical device, modelled as a continuous cyber-physical system with a neural controller. To our knowledge, this is the first result of this kind in a general purpose ITP; and a result that was only feasible thanks to the compositionality provided by Vehicle's functional interface. 

# Summary. An optional shortened abstract.
summary: We present a principled approach for connecting neural network verifiers to interactive theorem provers and demonstrate its utility in Neural-Cyber-Physical-Systems verificaiton.

tags:
- Neural Network Verification 
- Interactive Theorem Proving
- Formal Methods
- Cyber-Physical Systems
- Infinite-Time Horizon Safety

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
#  - name: CEUR-
#    url: https://ceur-ws.org/Vol-3442/paper-21.pdf

url_pdf: 'https://arxiv.org/pdf/2605.02790'
url_project: 'https://github.com/vehicle-lang/vehicle'
#url_slides: ''
#url_source: ''
---
