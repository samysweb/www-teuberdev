---
title:  Corrigendum to "An Information-Flow Perspective on Algorithmic Fairness"
type: single
authors:
  - admin
---
Following up on the publication of our AAAI 2024 paper ["An Information-Flow Perspective on Algorithmic Fairness"](http://localhost:1313/publication/aaai24/), [Marco Favier](https://www.uantwerpen.be/en/staff/marco-favier/) kindly notified us about a mistake in our publication:

Section 3.2, in particular Lemma 2, states that *Restricted Information Flow* can be used to prove conditional demographic parity.
This Lemma is wrong, as there exists a counterexample (provided by Marco Favier):
For $G=\\left\\{A,B\\right\\}$ and $U=\\left\\{0,1\right\\}$ both uniformly distributed,
we could analyze Restricted Information Flow w.r.t. the restricted classification $R\\left(A,0\right)=R\left(B,1\right)=0$ and $R\\left(A,1\\right)=R\\left(B,0\\right)=1$.
In this case, we can show noninterference for the following program:

> **if** $R\\left(g,u\\right)=0$ **return** $u$ **else** **return** $1-u$

However, this program does not satisfy conditional demographic parity, as we _exactly_ return $0$ iff $g=A$ and $1$ otherwise (where $g$ is the protected attribute).
This is a concrete counterexample to the statement in Lemma 2.

It is our understanding that this mistake does not concern the other contributions of the paper.
In particular, the results on Quantitative Information Flow (Section 4) are independent of Section 3.2. Similarly, our analysis of German Tax Software relied on unconditional noninterference and is thus not affected either.

We are currently considering whether causality also provides a suitable framework for using Restricted Information Flow w.r.t. Algorithmic Fairness questions and plan to publish a formal corrigendum.