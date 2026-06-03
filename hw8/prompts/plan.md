@agents### Uniform replacement stability

$A$ is $\beta(n)$-stable if, for every $S$, every $i \in [n]$, and replacement $z'_i$,

$$|\ell(A(S), z_i) - \ell(A(S'), z_i)| \le \beta(n).$$

### Theorem: Stability Generalization Bound

If $A$ is $\beta(n)$-stable, then for every distribution $\mathcal{D}$,

$$\mathbb{E}_{S \sim \mathcal{D}^n} L_{\mathcal{D}}(A(S)) \le \mathbb{E}_{S \sim \mathcal{D}^n} L_S(A(S)) + \beta(n).$$

### Regularized Empirical Risk Minimization (RERM)

Regularized empirical risk minimization adds a penalty to resist sudden jumps in parameter selection:

$$A_\lambda(S) = \text{RERM}_\lambda(S) = \arg\min_{w \in \mathcal{W}} L_S(w) + \lambda\Psi(w).$$

Here, $\mathcal{W}$ is the parameter domain, $\lambda > 0$, and $\Psi : \mathcal{W} \to \mathbb{R}$ is the regularizer.

### Uniform Replacement Stability of RERM

The regularized rule is replacement stable with $\beta(n) \le \frac{2R^2}{\lambda n}$. This means that for every one-point replacement $S'$ of $S$:

$$|\ell(A_\lambda(S), z_i) - \ell(A_\lambda(S'), z_i)| \le \frac{2R^2}{\lambda n}.$$

Choosing $\lambda = \Theta\left(\frac{R}{B\sqrt{n}}\right)$ yields:

$$\mathbb{E} L_{\mathcal{D}}(A_\lambda(S)) \le \inf_{\|w\|_2 \le B} L_{\mathcal{D}}(w) + O\left(\frac{BR}{\sqrt{n}}\right).$$

$\text{RERM}$ learns the norm ball through stability, not uniform convergence.

### Convex Lipschitz Bounded Problems

A convex Lipschitz bounded problem satisfies:

* **Convexity:** $\ell(w, z)$ is convex in $w$.
* **Lipschitzness:** $|\ell(w, z) - \ell(w', z)| \le G\|w - w'\|$.
* **Bounded comparison:** There is a comparator set such as $\|w\| \le B$ or $\Psi(w) \le B^2$.

### Parameter Lipschitz Bounds via Scalar Properties

Assume:

* **Scalar convexity:** $\text{loss}(\hat{y}, y)$ is convex in $\hat{y}$.
* **Scalar Lipschitzness:** $|\text{loss}(a, y) - \text{loss}(b, y)| \le g|a - b|$.
* **Feature scale:** $\|\varphi(x)\|_2 \le R$.

Then:

$$|\ell(w, z) - \ell(w', z)| \le g|\langle w - w', \varphi(x) \rangle| \le gR\|w - w'\|_2.$$

Thus, the problem is convex and $G = gR$-Lipschitz in $\|\cdot\|_2$. Scalar Lipschitzness combined with feature scale gives the parameter Lipschitz bound $G = gR$.

### Strong Convexity

$\Psi$ is $\alpha$-strongly convex with respect to $\|\cdot\|$ if for every $w, w'$:

$$\Psi(w') \ge \Psi(w) + \langle \nabla\Psi(w), w' - w \rangle + \frac{\alpha}{2}\|w' - w\|^2.$$

| Regularizer | Strongly convex in |
| --- | --- |
| $\Psi(w) = \frac{1}{2}\lVert w \rVert_2$ | $\lVert \cdot \rVert _2$ |
| $\Psi(w) = \frac{1}{2}\lVert w \rVert_p^2 \quad (1 < p \le 2)$ | $\lVert \cdot \rVert _p$ |
| Negative entropy: $\Psi(w) = \sum_j w_j \log w_j$ | $\lVert \cdot \rVert _1$ |

### Theorem: Stability of RERM

Assume $\ell(w, z)$ is convex and $G$-Lipschitz with respect to $\|\cdot\|$, and $\Psi$ is $\alpha$-strongly convex with respect to $\|\cdot\|$. Let

$$A_\lambda(S) = \arg\min_{w \in \mathcal{W}} L_S(w) + \lambda\Psi(w).$$

Then $A_\lambda$ is replacement stable with:

$$\beta(n) \le \frac{2G^2}{\lambda\alpha n}.$$

### Theorem: Learning from Stable RERM

Assume $\ell$ is convex and $G$-Lipschitz, and $\Psi$ is $\alpha$-strongly convex and nonnegative. Then for every comparator $w \in \mathcal{W}$:

$$\mathbb{E}_{S \sim \mathcal{D}^n} L_{\mathcal{D}}(A_\lambda(S)) \le L_{\mathcal{D}}(w) + \lambda\Psi(w) + \frac{2G^2}{\lambda\alpha n}.$$

### Comparator Geometries and Bounds

| Comparator geometry | Regularizer | Effect |
| --- | --- | --- |
| $\|w\|_2 \le B$ | $\frac{1}{2}\|w\|_2^2$ | Dimension-free Euclidean scale |
| $\|w\|_p \le B$ | $\frac{1}{2}\|w\|_p^2$ | $\alpha = p - 1$, cost $\sim \frac{1}{\sqrt{p - 1}}$ |
| Simplex / $\ell_1$ | Negative entropy: $\sum_j w_j \log w_j$ | Logarithmic dependence on dimension |

### General Norms and Hölder's Inequality

Scalar Lipschitzness followed by Cauchy-Schwarz in $\ell_2$ yields:

$$|\ell(w, z) - \ell(w', z)| \le g|\langle w - w', \varphi(x) \rangle| \le g\|w - w'\|_2\|\varphi(x)\|_2.$$

For a general norm $\|\cdot\|$, the second step generalizes via Hölder’s inequality:

$$\langle u, v \rangle \le \|u\| \cdot \|v\|_*, \quad \text{where } \|v\|_* \coloneqq \sup_{\|u\| \le 1} \langle u, v \rangle.$$

### Weighted Euclidean Geometry

The data scale is measured in the dual norm:

$$\|\varphi(x)\|_{Q,*} = \sqrt{\varphi(x)^\top Q^{-1} \varphi(x)}.$$

If $\|w\|_Q \le B$ and $\|\varphi(x)\|_{Q,*} \le R_Q$, then the excess scale is:

$$O\left(\frac{BR_Q}{\sqrt{n}}\right).$$

### $\ell_p$ Geometry

Hölder bounds the diagonal Hessian term (where the rank-one part $\ge 0$):

$$\langle u, \nabla^2\Psi(w)u \rangle \ge (p - 1)\|u\|_p^2.$$

If $\|w\|_p \le B$ and $\|\varphi(x)\|_q \le R_q$ ($q$ being the conjugate to $p$), the excess scale is:

$$O\left(\frac{BR_q}{\sqrt{(p - 1)n}}\right).$$

### Entropic Geometry ($\ell_1$ / Simplex)

The negative entropy regularizer is $1$-strongly convex in $\|\cdot\|_1$ (so $\alpha = 1$). Here, the strong-convexity gap is $\text{KL}(w' \parallel w)$, and Pinsker's inequality yields:

$$\text{KL}(w' \parallel w) \ge \frac{1}{2}\|w' - w\|_1^2.$$

The dual norm is $\|\cdot\|_\infty$. With $\|\varphi(x)\|_\infty \le R$, the excess scale is:

$$O\left(R\sqrt{\frac{\log d}{n}}\right).$$

### Soft-Margin SVM

Soft-margin SVM is defined as $\ell_2$-regularized hinge loss minimization:

$$A_\lambda(S) = \arg\min_{w \in \mathcal{W}} \frac{1}{n} \sum_{i=1}^n \max(0, 1 - y_i\langle w, x_i \rangle) + \frac{\lambda}{2}\|w\|_2^2.$$

### Convex Lipschitz Bounded Case ($G \le 2, B = 1$)

Consider a loss that is convex (a sum of squares) and $2$-Lipschitz on the unit ball:

$$|\ell(w, z) - \ell(u, z)| = \left|\sum_{j \in I} (w_j - u_j)(w_j + u_j)\right| \le \|w - u\|_2\|w + u\|_2 \le 2\|w - u\|_2.$$

For this convex Lipschitz bounded problem with $G \le 2$ and $B = 1$, the RERM bound is dimension-free:

$$\mathbb{E} L_{\mathcal{D}}(A_\lambda(S)) \le L_{\mathcal{D}}(0) + O\left(\frac{GB}{\sqrt{n}}\right) = O\left(\frac{1}{\sqrt{n}}\right).$$

### Notable Items & Non-Trivial Proofs (Session Updates)
* **Part A (Grid Validation):** In Q3 and Q4, selecting a candidate regularizer $\lambda$ via a dyadic grid discretization up to a factor of 2 leads to a constant factor inflation of the RERM learning term (from $2\sqrt{2} \approx 2.82$ to $5/2 \times \sqrt{2} \approx 3.53$ or $5$ if halving data). The total price of tuning without knowing the optimal scale $\Psi(u)$ includes this inflation, the validation sample splitting, and the validation-selection penalty $\sqrt{\frac{\log(2K)}{n}}$.
* **Part B (Approximate RERM):** In Q3, deriving the learning guarantee of an approximate optimizer $\tilde{w}_S$ using the parameter movement bound $\ell(\tilde{w}_S, z) \le \ell(w_S, z) + G\|\tilde{w}_S - w_S\|$ yields a tight expected risk bound scaling with $G\sqrt{\frac{2\eta}{\lambda\alpha}}$. This avoids the loose constants found when using the generic stability of the approximate RERM directly.
* **Part C (Weighted Euclidean Geometry):** In Q3, optimizing the geometry parameter $Q = \text{diag}(q_1, \dots, q_d)$ to minimize the product of the primal constraint bound $\sum_j q_j b_j^2$ and the dual norm bound $\sum_j r_j^2/q_j$ via Cauchy-Schwarz reveals the best diagonal scale $q_j \propto r_j / b_j$, leading to the optimal excess term $\frac{2g}{\sqrt{n}} \sum_j b_j r_j$.
