---
title: Solving difficult SMT instances using abstractions and incremental SMT solving
summary: Bachelor Thesis
tags:
- Formal Methods
- Student
date: "2019-09-16T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Part of the abstraction refinement algorithm developed in my Bachelor Thesis
  #focal_point: Smart

links:
- icon: github
  icon_pack: fab
  name: GitHub
  url: https://github.com/samysweb/ablector
- icon: graduation-cap
  icon_pack: fas
  name: Bachelor Thesis
  url: thesis.pdf
- icon: graduation-cap
  icon_pack: fas
  name: Publication
  url: /publication/ba/
# url_code: ""
# url_pdf: ""
# url_slides: ""
# url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

The satisfiability modulo theory (SMT) problem deals with deciding numerous fragments of the first-order logic constraint by some *Theory* $T$ and can be considered an extension of the satisfiability problem for propositional logic formulae.
A SMT-Theory $T$ usually constraints the behaviour of certain uninterpreted functions or predicates of the first-order logic, but it may also syntactically constrain the language (e.g. by not allowing quantifiers).
Today, solving SMT problems has become a discipline of its own with many solving techniques relying in one way or another on a SAT solver in the background.
With SMT-LIB a unified interface to codify SMT instances has been developed that is supported by most state-of-the-art SMT solvers.

Over the last decade a variety of approximation techniques have been introduced into the world of SMT solving and model checking.
The objective of any such approximation techniques is to speed up the solving process thus reducing computational cost and avoiding exponential runtimes for common usecases.
Usually, over-approximation techniques help in speeding up the solver's runtime for unsatisfiable SMT-instances, while under-approximation techniques help reducing the runtime of satisfiable instances. 

Although abstraction techniques have successfully been used for the array theory as well as the uninterpreted functions theory, there is little work on using over-approximations for the quantifier free bitvector logic (`QF_BV` in SMT-LIB) outside the approach taken with UCLID.
In my bachelor thesis I therefore took up the topic of solving *difficult* bitvector SMT instances, like the ones provided in the *LLBMC family of benchmarks*, using abstractions.