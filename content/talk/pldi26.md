---
title: "Heterogeneous Dynamic Logic: Provability Modulo Program Theories"
summary: "PLDI (Boulder, USA)"
date: 2026-06-19
talk_kind: conference
publishDate: 2026-01-01
authors:
  - admin
links:
 - name: Announcement
   url: "https://pldi26.sigplan.org/program/program-pldi-2026/"
 - name: Paper
   url: /publication/hdl/
---
Formally specifying, let alone verifying, properties of systems involving multiple programming languages is inherently challenging. We introduce Heterogeneous Dynamic Logic (HDL), a framework for combining reasoning principles from distinct (dynamic) program logics in a modular and compositional way. HDL mirrors the architecture of satisfiability modulo theories (SMT): Individual dynamic logics, along with their calculi, are treated as dynamic theories that can be flexibly combined to reason about heterogeneous systems whose components are verified using different program logics. HDL provides two key operations: Lifting extends an individual dynamic theory with new program constructs (e.g., the havoc operation or regular programs) and automatically augments its calculus with sound reasoning principles for the new constructs; and Combination enables cross-language reasoning in a single modality via Heterogeneous Dynamic Theories, facilitating the reuse of existing proof infrastructure. We formalize dynamic theories, their lifting and combination in Isabelle, and prove the soundness of all proof rules. We also prove relative completeness theorems for lifting and combination: Under common assumptions, reasoning about lifted or combined theories is no harder than reasoning about the constituent dynamic theories and their common first-order structure (i.e., the "data theory"). We demonstrate HDL's utility by verifying an automotive case study in which a Java controller (formalized in Java dynamic logic) steers a plant model (formalized in differential dynamic logic). 