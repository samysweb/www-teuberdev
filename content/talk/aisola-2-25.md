---
title: "Formally Verified LLM Program Synthesis for Solidity Smart Contracts"
summary: AISoLA 2025, Rhodes, Greece
date: 2025-11-05
publishDate: 2025-07-15
authors:
  - admin
links:
  - name: Announcement
    url: https://programme.paperplane.services/session/160
---

*Paper to be released in 2026*

**Formally Verified LLM Program Synthesis for Solidity Smart Contracts**


Smart contracts are programs that manage resources on distributed ledgers. The Scar approach
helps developing correct and secure smart contract applications 
via a model-driven, verification-based development process:
Before implementing an application, smart contract developers first describe it in
terms of an abstract model. Within this model, they can also specify and verify
high-level security and behavioral correctness properties. From a consistent model, a source
code skeleton containing formal specifications is generated. Scar provides 
a built-in generator for the widely used Solidity programming language.
In the next step, the developer has to implement the generated source code skeleton 
so that the implementation fulfills the generated specification.
This step is currently a manual task: The developer
writes code and tries to verify it against the generated specification. In case they succeed, the
application can be deployed; otherwise, the implementation must be adapted.
In this paper, we present an approach for automatically synthesizing correct programs using Large Language Models (LLMs). The LLM is prompted to generate an implementation matching the source-code specification provided by Scar. Then, a formal proof of correctness is attempted. If successful, the developer receives an implementation which is guaranteed to conform to the specification of the abstract model.
We test our approach on a number of example use cases, using both the Certora prover and the Solc-Verify tool. We compare the results for both tools, and also report in general on our experiences with using LLMs in conjunction with formal verification.