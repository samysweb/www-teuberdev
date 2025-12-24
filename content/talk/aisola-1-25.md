---
title: "Replication of the Landscape for LLM-generated Formal Specifications for C Programs"
summary: AISoLA 2025, Rhodes, Greece
date: 2025-11-02
publishDate: 2025-07-15
authors:
  - admin
links:
  - name: Announcement
    url: https://programme.paperplane.services/session/179
---

*Paper to be released in 2026*

**Replication of the Landscape for LLM-generated Formal Specifications for C Programs**

Deductive program verification is an established technique for improving software reliability, but it is not widely adopted due to the manual effort required to create formal specifications. Even if the top-level requirement is specified, auxiliary specifications need to be added, such as loop invariants. Automating the generation of auxiliary formal specifications could significantly improve the feasibility and adoption of formal methods in practice. Recently, large language models (LLMs) have been explored to automate specification generation, but the fragility of LLMs and the variation in benchmark selection complicate the comparison of different approaches. Comparison and replication are further complicated for commercial, black-box LLMs, for instance GPT, which may be changed without notice.

In this work, we survey four recent works on LLM-generated formal specification and verification of C programs and report on replication of their experimental results. All four works use diverse techniques, but share the target program language C, as common in safety-critical systems and therefore prone to subtle bugs, and one set of benchmarks. We evaluate the approaches on performance under a unified experimental setup, and compare the strengths and weaknesses of each approach in automating verification using LLMs. In order to assess the impact of model scaling, we also compare the performance of all four tools using both the GPT-3.5 and the GPT-4.0 models. Moreover, we investigate the reproducibility of results by analyzing the result consistency across model generations, and compare them with those reported in the original studies. Our results indicate 4 to 20% variation of the individual approaches’ performance depending on which model was used (GPT 3.5 and 4o).