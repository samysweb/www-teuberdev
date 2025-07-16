---
title: "Provable Guarantees for Neural Networks"
summary: MeelGroup (Online)
date: 2025-07-16
publishDate: 2025-07-15
authors:
  - admin
---
**Specifying and Verifying What Matters in Cyber-Physical Systems and Beyond**

As neural network (NN) controllers are increasingly introduced into safety-critical domains, we must ensure not just provable, but also meaningful safety guarantees. This talk presents two lines of my work focused on delivering such guarantees.
 
The first part explores the verification of NN controllers for Cyber-Physical Systems. I introduce VerSAILLE (Verifiably Safe AI via Logically Linked Envelopes), which uses Differential Dynamic Logic to derive strong safety specifications for NNs that guarantee infinite-time horizon safety for continuous-time control systems. To verify the derived specifications, I introduce Mosaic, the first sound and complete method for verifying polynomial real-arithmetic specifications on piecewise-linear NNs. These tools scale NNCS verification to infinite-time horizons and well beyond prior baselines, with applications to airborne collision avoidance, adaptive cruise control, and the ABZ'25 case study.
 
The second part of the talk focuses on relational verification, particularly on verifying equivalence properties between NNs. I present a new zonotope-based abstract domain tailored to differential reasoning, which is particularly well-suited for confidence-based properties: a category of properties that are a strong candidate for globally verifiable NN specifications. Our tool VeryDiff demonstrates the power of this approach, achieving a median speedup of over 300x compared to the non-relational verifier alpha,beta-CROWN on NNs for particle beam classification in the context of CERN's LHC.