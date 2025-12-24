---
title: "Of Good Demons and Bad Angels: Guaranteeing Safe Neural Control under Finite Precision"
summary: ANSR Reading Group, Berkeley, California, US (Online)
date: 2025-10-20
publishDate: 2025-07-15
authors:
  - admin
---
**Of Good Demons and Bad Angels: Guaranteeing Safe Neural Control under Finite Precision**

Neural networks (NNs) are increasingly prevalent in safety-critical cyber-physical systems such as cars or aircraft. Therefore, guaranteeing the safety of such NN control systems is crucial. In our work we leverage the logical foundations of Differential Dynamic Logic (dL) and combine them with recent advances in NN verification to verify the infinite-time horizon safety of NN control systems.
Our original dL-based NN verification technique assumed idealized NN semantics ignoring roundoff errors introduced by finite-precision implementations. In contrast, our recent extension also bridges the gap between theoretical guarantees and real-world implementations by incorporating robustness under finite-precision perturbations -- in sensing, actuation, and computation -- into the safety verification. To this end, we model the problem as a hybrid game between a good Demon, responsible for control actions, and a bad Angel, introducing perturbations. This formulation enables formal proofs of robustness with respect to a given (bounded) perturbation. Leveraging this bound, we employ state-of-the-art mixed-precision fixed-point tuners to synthesize sound and efficient implementations, thus providing a complete end-to-end solution to infinite-time horizon safety. We demonstrate our approach on case studies from the automotive and aeronautics domains, producing efficient NN implementations with rigorous infinite-time horizon safety guarantees.