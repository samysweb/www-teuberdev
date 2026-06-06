---
title: "Differential Verification of Neural Networks: Theory and Applications"
summary: "Workshop on Program Equivalence and Relational Reasoning (FLoC, Lisbon, Portugal)"
date: 2026-07-24
talk_kind: contributed
publishDate: 2026-01-01
authors:
  - admin
links:
#  - name: Announcement
#    url: 
---

*Talk on joint work by Philipp Kern and me*


Although techniques for the verification of neural networks (NNs) have seen significant progress in recent years, specifying meaningful properties remains non-trivial.
One promising approach to the specification of neural networks are relational properties which do not specify the behavior of an NN in absolute terms, but impose constraints on related execution traces.

We provide an overview on our recent advances in using differential verification in NN verification by leveraging the abstract domain of Zonotopes.
This approach enables us to reason about changes in behavior locally, at the level of individual neurons of an NN.
We discuss the fundamental ideas of our abstract domain and discuss current and future applications of the differential verification paradigm.