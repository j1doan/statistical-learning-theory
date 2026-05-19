# Execution Plan: Learning Theory Proof Pipeline

This document maps out the core theoretical dependencies, lemmas, and black-box assumptions required to solve the problem set. The order below represents the precise chain of logic needed for the proof constructions.

## Foundational Assumptions (The Black-Box Targets)
These are average-case complexity and lattice problems assumed to be computationally intractable. They serve as the ultimate targets for the hardness reductions in Part B.

### $\mathrm{uSVP}$ (Unique Shortest Vector Problem)
* **Definition:** A lattice problem where the task is to find the shortest non-zero vector $v$ in a high-dimensional lattice, given the structural guarantee that $v$ is shorter than any other non-collinear vector by a definitive gap factor $\gamma \ge 1$.
* **Role in Proof:** Establishes that learning intersections of $d^r$ halfspaces (even improperly) is computationally hard in the worst/average case.

### $\mathrm{RSAT}$ (Random Satisfiability Hardness Assumption)
* **Definition:** Based on Feige's Refutation Hypothesis, it assumes no polynomial-time algorithm can reliably distinguish between a uniformly random CNF formula and a CNF formula embedded with a hidden, planted satisfiable structure.
* **Role in Proof:** Establishes that learning intersections of $k(d) = \omega(1)$ halfspaces is hard.

## Chain of Theorems for Part A: Boosting Sparse Linear Predictors

These components must be chained together sequentially to complete the analysis of sparse margin bounds, AdaBoost generalization, and the failure of coordinate bases under unconstrained weights.

### Theorem A.1: The Minimax Theorem (Von Neumann / Yao's Principle)
* **Statement:** For any finite game matrix (or bounded loss over distributions), $\min_P \max_Q \mathbb{E}[L(P,Q)] = \max_Q \min_P \mathbb{E}[L(P,Q)]$.
* **Application (Part A.1):** Converts the existence of a global $\ell_1$-bounded margin classifier over the true distribution into a guarantee that *at least one* coordinate base classifier $b \in \mathcal{B}$ maintains a non-trivial edge $\gamma$ over *any* arbitrary reweighted distribution $Q$.

### Lemma A.2: Equivalence of Weighted Error and Signed Correlation
* **Statement:** For a distribution $D$ over samples, the misclassification error $L_D(b)$ and the signed correlation are related exactly by:
    $$L_D(b) = \frac{1}{2} - \frac{1}{2}\sum_{i=1}^n D_i y_i b(x_i)$$
* **Application (Part A.1):** Provides the mathematical foundation to construct an $O(nd)$ time Weighted ERM weak learner by selecting the feature coordinate that maximizes absolute signed correlation.

### Theorem A.3: AdaBoost Training Error Convergence (Freund & Schapire)
* **Statement:** If a weak learner guarantees an edge of at least $\gamma_t$ at each round $t$, the training error of the boosted ensemble after $T$ rounds is bounded by:
    $$\prod_{t=1}^T 2\sqrt{L_D(b_t)(1-L_D(b_t))} \le e^{-2 \sum_{t=1}^T \gamma_t^2}$$
* **Application (Part A.2):** Used to isolate the exact number of rounds $T = \lceil 2 s^2 B^2 \ln(n) \rceil$ needed to drive the empirical training error to absolute zero.

### Theorem A.4: Vapnik-Chervonenkis (VC) Generalization Bounds for Sparse Classes
* **Statement:** For a hypothesis class $\mathcal{H}$ with VC-dimension $d_{VC}$, the sample complexity to achieve generalization error $\varepsilon$ with probability $1-\delta$ in the realizable case is bounded by $O\left(\frac{d_{VC} \log(1/\varepsilon) + \log(1/\delta)}{\varepsilon}\right)$.
* **Application (Part A.2):** Applied using the sparsity of the final ensemble (since AdaBoost activates at most $T$ coordinates) to bound the VC-dimension as $O(T \log(e d / T))$ and derive the final statistical sample complexity.

### Theorem A.5: Hadamard-type Matrix / Silver-Propeller Sign Matrix Properties
* **Statement:** There exist invertible sign matrices $M \in \{-1, +1\}^{s \times s}$ where column vectors are orthogonal or heavily balanced, meaning that no single row coordinate exhibits a significant correlation with a specially constructed target vector.
* **Application (Part A.3):** Used to construct the explicit adversarial distribution showing that when $\lVert w^\star \rVert_\infty = 2^{\Omega(s)}$, the coordinate edge drops exponentially to $2^{-\Omega(s)}$, proving that boosting fails if the weights are poorly scaled.

## Chain of Theorems for Part B: Agnostic Hardness via Boosting

These components are chained in reverse logic (a reduction pipeline) to show that if a proper agnostic learner exists, it can be amplified into a powerful learner that breaks the foundational $\mathrm{uSVP}$ or $\mathrm{RSAT}$ assumptions.

### Theorem B.1: The Structural Intersection-to-Weak-Halfspace Lemma
* **Statement:** If a distribution $\mathcal{D}$ is perfectly realizable by an intersection of $k$ halfspaces ($g \in \mathcal{I}_{d,k}$), then there exists a *single* affine halfspace $h$ that achieves an error of at most:
    $$L_{\mathcal{D}}(h) \le \frac{1}{2} - \frac{1}{2k^2}$$
* **Application (Part B.1):** Serves as the critical weak-learning link. It guarantees that a valid halfspace with a significant edge ($\gamma = \frac{1}{2k^2}$) always exists within the target space.

### Lemma B.2: Agnostic-to-Weak Learner Reduction
* **Statement:** An Agnostic PAC learner for a concept class $\mathcal{H}$ outputs a hypothesis with error at most $\min_{h \in \mathcal{H}} L_{\mathcal{D}}(h) + \varepsilon$. 
* **Application (Part B.2):** By setting the agnostic accuracy parameter to $\varepsilon = \frac{1}{4k^2}$, a proper agnostic halfspace learner is converted into a valid Weak Learner for $\mathcal{I}_{d,k}$ with a guaranteed edge of $\gamma = \frac{1}{4k^2}$.

### Theorem B.3: Linear Threshold Function (LTF) Circuit Bounds
* **Statement:** The VC-dimension of an ensemble formed by taking a majority vote of $T$ affine halfspaces in $\mathbb{R}^d$ is bounded by $\widetilde{O}(Td)$.
* **Application (Part B.3 & B.4):** Used to calculate the sample complexity of the fully boosted intersection learner. This shows that the complete learning pipeline runs in polynomial time if $k(d)$ is polynomially bounded.

## Final Reduction Pipeline (Proof Structure)

To complete the problem set, verify that the chain of theorems operates seamlessly under this structural contradiction:

$$
\begin{aligned}
\text{Proper Agnostic Learner for Halfspaces} 
&\xrightarrow{\text{[Lemma B.2]}} \text{Efficient Weak Learner for } \mathcal{I}_{d,k} \\
&\xrightarrow{\text{[Theorem A.3 \& B.3]}} \text{Efficient Strong PAC Learner for } \mathcal{I}_{d,k} \\
&\xrightarrow{\text{[Section 1 Targets]}} \textbf{Contradiction with uSVP / RSAT Fact}
\end{aligned}
$$

**Conclusion:** Therefore, efficient proper agnostic PAC learning of affine halfspaces is impossible.

## Session Updates & Blockers
- **Part A.4 Experiment:** Implemented a custom `CoordinateAdaBoost` class to track specific metrics like observed edge, exponential loss, and normalized margin over rounds, as Scikit-learn's AdaBoost does not expose these internal metrics easily for coordinate-wise weak learners. The convex surrogate used is `LogisticRegression` with an $\ell_1$ penalty.
- **Part A.3 Construction:** The explicit construction of the hard distribution relies on a specific sign matrix where columns have a weighted sum of 1. The proof shows that the realizing vector $w^\star$ has exponentially large coefficients, which forces the coordinate edge to be exponentially small, thus breaking the polynomial-time guarantee of AdaBoost.
- **Part B.1 Weak Halfspace:** The proof splits into two cases based on the marginal probability of the positive class. If $p$ is small, the constant $-1$ predictor works. If $p$ is large, a probabilistic argument (pigeonhole principle) shows that at least one of the $k$ halfspaces defining the intersection must have a small false positive rate, yielding the required edge.
- **Manual Verification Required:** Please verify the custom AdaBoost implementation in A.4 and the specific matrix construction in A.3. The proofs for B.1-B.4 follow the reduction pipeline directly.