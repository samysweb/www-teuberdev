---
title: "Verification of Autonomous Neural Car Control with KeYmaera X"
summary: "ABZ (Düsseldorf, Germany)"
date: 2025-06-12
publishDate: 2025-06-12
authors:
  - admin
links:
 - name: Announcement
   url: "https://abz-conf.org/site/2025/program/"
 - name: Paper
   url: /publication/abz25/
---
This article presents a formal model and formal safety proofs for the ABZ'25 case study in differential dynamic logic (dL). The case study considers an autonomous car driving on a highway avoiding collisions with neighbouring cars. Using KeYmaera X’s dL implementation, we prove absence of collision on an infinite time horizon which ensures that safety is preserved independently of trip length. The safety guarantees hold for time-varying reaction time and brake force. Our dL model considers the single lane scenario with cars ahead or behind. We demonstrate that dL with its tools is a rigorous foundation for runtime monitoring, shielding, and neural network verification. Doing so sheds light on inconsistencies between the provided specification and simulation environment highway-env of the ABZ'25 study. We attempt to fix these inconsistencies and uncover numerous counterexamples which also indicate issues in the provided reinforcement learning environment.