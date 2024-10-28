---
title: "Towards Combining the Cognitive Abilities of Large Language Models with the Rigor of Deductive Progam Verification"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Bernhard Beckert
- Jonas Klamroth
- Wolfram Pfeifer
- Patrick Röper
- admin

date: "2024-10-27T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-08-09T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: 12th International Symposium on Leveraging Applications of Formal Methods, Verification and Validation
publication_short: In ISOLA 2024

abstract: |2-
  Recent investigations hint at the ability of large language models (LLMs) to generate formal specifications for given program code. In this work, we systematically discuss and categorize different use cases and application scenarios that combine specification synthesis via LLMs with deductive program verification. We present preliminary quantitative experiments on the capabilities of LLMs to generate correct specifications. To this end, we use a prototypical integration of GPT (versions 3.5 and 4o) with the deductive program verifier KeY and the bounded model checker JJBMC. We evaluated our prototype on a set of Java programs that are partially annotated with specifications written in the Java Modeling Language (JML). We show that GPT 4o generates correct annotations in approximately half of all instances across the investigated scenarios. For the case of faulty specifications, we investigate how a feedback loop can help to improve the original answer. Finally, we present a vision of how Large Language Models may support rigorous formal verification of software systems and describe the necessary next steps in this direction.

# Summary. An optional shortened abstract.
summary: We evaluate the potential of Large Language Models (specifically GPT 3.5 and GPT 4o) for the generation of code annotations in the Java Modelling Language using a prototypical integration of the Java verification tools KeY and JJBMC with OpenAI's API.

tags:
- Formal Methods
- Program Analysis
- Deductive Program Verification
- Large Language Models
- Specification Generation
- Design by Contract
- Java Modeling Languag

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
links:
 - name: DOI
   url: https://doi.org/10.1007/978-3-031-75387-9_15

#url_pdf: ''
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
This work is **forthcoming**, links will be added once available.