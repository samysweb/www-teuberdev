---
title: "From Compositional to Relational Verification of AI-based Systems"
summary: CySec Seminar (TU Wien, Vienna, Austria)
date: 2026-09-14
talk_kind: invited
publishDate: 2026-09-01
authors:
  - admin
links:
 - name: Announcement
   url: "https://cysec.wien/news/2026-09-14_lecture_teuber/"
---

Formally specifying, let alone verifying, properties of systems that combine heterogeneous subsystems is inherently challenging. In the first part of this talk, I will introduce Heterogeneous Dynamic Logic (HDL) as a framework for combining reasoning principles from distinct (dynamic) program logics in a modular and compositional way. HDL mirrors the architecture of satisfiability modulo theories (SMT): Individual dynamic logics, along with their calculi, are treated as dynamic theories that can be combined to reason about heterogeneous systems whose components are verified using distinct proof infrastructures.

The second part of this talk discusses the application of HDL to neural network control systems. Logic-based verification enables us to leverage control theoretic safety proofs for cyber-physical systems for verifying the safety of neural network controllers all the way down to the fixed-point arithmetic level of an FPGA (an FMCAD'25 result that HDL now lets us justify much more directly).

The final part of my talk will broaden the scope and investigate the safety of AI-based systems which lack a comprehensive system model. I will argue that relational verification can provide meaningful best-effort guarantees in this setting and present an abstract interpretation-based approach for the relational verification of neural networks that has applications to neural network equivalence and global robustness.

{{< foldergallery src="media/galleries/tu-vienna-26" >}}
*Pictures: © TU Wien CySec, Clemens Purner 2026*