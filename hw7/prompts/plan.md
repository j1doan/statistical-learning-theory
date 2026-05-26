### Empirical Covering Numbers

An $\alpha$-cover of $\mathcal{F}$ on sample $S = (z_1, \dots, z_n)$ in $\ell_p$ is a finite subset $\mathcal{F}_\alpha \subset \mathcal{F}$ such that every $f \in \mathcal{F}$ has some anchor $g \in \mathcal{F}_\alpha$ with:

$$\left( \frac{1}{n} \sum_{i=1}^n |f(z_i) - g(z_i)|^p \right)^{\frac{1}{p}} \le \alpha$$

The **empirical covering number** is the size of the smallest such cover:

$$\mathcal{N}_p(\mathcal{F}, \alpha, S) = \min \{ |\mathcal{F}_\alpha| : \mathcal{F}_\alpha \text{ is an } \alpha\text{-cover of } \mathcal{F} \text{ on } S \}$$

$$\mathcal{N}_p(\mathcal{F}, \alpha, n) = \sup_{|S|=n} \mathcal{N}_p(\mathcal{F}, \alpha, S)$$

### Covering via pseudo-dimension (Pollard)

If $\mathcal{F} \subset [-a, a]^{\mathcal{Z}}$ and $\text{Pdim}(\mathcal{F}) \le D$, then for $0 < \alpha \le a$:

$$\mathcal{N}_\infty(\mathcal{F}, \alpha, n) \le \left( \frac{en a}{D \alpha} \right)^D$$

### ERM bound via pseudo-dimension

If $0 \le \ell \le a$ and $\text{Pdim}(\mathcal{F}) \le D$, then with probability $\ge 1 - \delta$:

$$L_{\mathcal{D}}(\hat{h}) \le \inf_{h \in \mathcal{H}} L_{\mathcal{D}}(h) + c a \sqrt{\frac{D \log\left(\frac{n}{D}\right) + \log\left(\frac{1}{\delta}\right)}{n}}$$

*(Note: In the standard presentation of this classic generalization bound, the constant $c > 0$ is a universal constant, and the entire expression inside the square root is divided by $n$.)*

### Fat-shattering bound

For every $\alpha > 0$, if the input domain is $\mathcal{X}_R$, then:

$$\text{fat}_\alpha(\mathcal{H}_B) \le \left( \frac{B R}{\alpha} \right)^2$$

### Contraction Principle (Talagrand)

If $\varphi_i : \mathbb{R} \to \mathbb{R}$ is $G$-Lipschitz for each $i$, then for any class $\mathcal{H} \subset \mathbb{R}^{\mathcal{X}}$ and sample $S = (x_1, \dots, x_n)$:

$$\mathbb{E}_{\xi} \left[ \sup_{h \in \mathcal{H}} \frac{1}{n} \sum_{i} \xi_i \varphi_i(h(x_i)) \right] \le G \cdot \mathbb{E}_{\xi} \left[ \sup_{h \in \mathcal{H}} \frac{1}{n} \sum_{i} \xi_i h(x_i) \right]$$

### Norm-constrained generalization bound

For $\mathcal{H}_B = \{x \to \langle w, x \rangle : \|w\|_2 \le B\}$, data with $\|x\|_2 \le R$, and a $G$-Lipschitz loss bounded in $[0, a]$, with probability $\ge 1 - \delta$, $\hat{w} = \text{ERM}_{\mathcal{H}_B}(S)$ satisfies:

$$L_{\mathcal{D}}(\hat{w}) \le \inf_{\|w\|_2 \le B} L_{\mathcal{D}}(w) + \mathcal{O} \left( \frac{GBR}{\sqrt{n}} + a \sqrt{\frac{\log\left(\frac{1}{\delta}\right)}{n}} \right)$$

### Margin generalization bound

With probability $\ge 1 - \delta$:

$$L_{\mathcal{D}}^{0/1}(\hat{w}) \le \inf_{\|w\|_2 \le B} L_{\mathcal{D}}^{\text{mrg}}(w) + \mathcal{O} \left( \sqrt{\frac{B^2 R^2 + \log\left(\frac{1}{\delta}\right)}{n}} \right)$$

### Hinge ERM bound

If $\|x\|_2 \le R$ a.s. and $\hat{w} = \text{ERM}_{\mathcal{H}_B}^{\text{hinge}}(S)$, then with probability $\ge 1 - \delta$:

$$L_{\mathcal{D}}^{0/1}(\hat{w}) \le \inf_{\|w\|_2 \le B} L_{\mathcal{D}}^{\text{hinge}}(w) + \mathcal{O} \left( \frac{BR\sqrt{\log\left(\frac{1}{\delta}\right)}}{n} \right)$$

### Representer Theorem Optimal Form

The optimum weight vector $w^*$ has the form:

$$w^* = \sum_{i=1}^n \alpha_i \varphi(x_i), \quad \text{with } \alpha \in \mathbb{R}^n$$

### Notable Proof Items for Part A & B
- **A.1 Norm-based kernel bound:** Relied on Cauchy-Schwarz inequality, Jensen's inequality on the concave square root function, and orthogonality of independent uniform signs to prove both the empirical and distribution bounds.
- **A.2 Representer theorem:** Used orthogonal projection in Hilbert spaces ($w = w_S + w_\perp$) to rigorously argue that $w_\perp = 0$ for any minimizer $w^*$ under an $L_2$ regularizer.
- **B.1 Convex hulls:** Used the fundamental theorem of linear programming (max of linear function over a probability simplex is achieved at a vertex) to prove that empirical Rademacher complexity is unchanged by taking the convex hull of a finite class.
- **B.2 $\ell_1$ linear predictors:** Showed that the $\ell_1$ bounded class $\mathcal{H}_B^1$ is the convex hull of $2d$ signed coordinate features scaled by $B$, and applied Massart's finite-class lemma to get the $O(\sqrt{\log d / n})$ bound.
- **B.3 Comparison:** Brought in Talagrand's Contraction Lemma to get uniform convergence of the Lipschitz surrogate loss, and highlighted the differences in complexity measure (sparsity vs $\ell_1$ norm), pointing out a dense small-weight predictor where the $\ell_1$ bound remains tight but the $\ell_0$ sparsity bound becomes vacuous.

### Notable Proof Items for Part C
- **C.1 & C.2 Margin bounds:** Used the margin-rescaled ramp surrogate $\ell_\gamma$ to connect continuous bounding with the strict discontinuous 0/1 population risk. By feeding FixedBoost's margin lower-bound theorem ($\min_i y_i f_w(x_i) \ge \frac{\gamma}{2} \|w\|_1$) into the Rademacher bound, derived the generalization gap.
- **C.3 Minimax margin:** Proved that the optimal normalized margin $\gamma^*$ is exactly twice the sample's best weak learning edge ($\gamma_{WL}$) by reducing it to a zero-sum game and applying von Neumann's minimax theorem on the correlation matrix $A$.
- **C.4 Connection to HW6:** Noted that the transition from greedy boosting bounds to margin bounds avoids the structural penalty $d_{VC} \propto T$, explaining why population error continues dropping even as the number of boosting rounds $T \to \infty$.

### Part D FixedBoost Experiment
- The `FixedBoost` algorithm was run natively on the binary matrices $A \in \{-1, +1\}^{n \times 2d}$.
- Encountered a numerical instability early on where the step size $\eta=1.0$ caused margins to scale into the thousands, sending `exp(-margin)` directly to $0.0$.
- Fixed this by introducing a stable `LogSumExp` routine (`logits -= np.max(logits)`) to ensure normalized weight distribution updates, and lowering the step size $\eta=0.01$ to observe smooth deterministic convergence.
- Ran the experiment and observed strong empirical validation that FixedBoost asymptotically approaches the optimal margin calculated by scipy's LP solver, though converging significantly faster than the conservative theory implies.