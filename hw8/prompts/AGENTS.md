# AGENTS.md

## Part A: Choosing Regularization by Validation

Let $\mathcal{W}$ be a convex parameter domain, and let $\ell(w, z) \in [0, 1]$ be convex in $w$ and $G$-Lipschitz with respect to a norm $\|\cdot\|$:

$$|\ell(w, z) - \ell(w', z)| \le G\|w - w'\|$$

for all $w, w', z$. Let $\Psi$ be nonnegative and $\alpha$-strongly convex with respect to $\|\cdot\|$.

Split an i.i.d. sample into an independent training sample $T$ of size $n_T$ and validation sample $V$ of size $n_V$. For a finite grid

$$\Lambda = \{\lambda_1, \dots, \lambda_K\} \subset (0, \infty),$$

define, for each $\lambda \in \Lambda$,

$$h_\lambda = A_\lambda(T) \in \arg\min_{w \in \mathcal{W}} L_T(w) + \lambda\Psi(w).$$

Then choose

$$\hat{\lambda} \in \arg\min_{\lambda \in \Lambda} L_V(h_\lambda),$$

and output $h_{\hat{\lambda}}$.

### 1. Validation selection for a finite random candidate set.

Condition on predictors $h_1, \dots, h_K$ that are independent of a validation set $V$ of size $n_V$, and let

$$\hat{k} \in \arg\min_{k \in [K]} L_V(h_k).$$

Prove

$$\mathbb{E}_V L_{\mathcal{D}}(h_{\hat{k}}) \le \min_{k \in [K]} L_{\mathcal{D}}(h_k) + \sqrt{\frac{\log(2K)}{2n_V}}.$$

You may use Hoeffding’s lemma for $[0, 1]$-valued losses.

### 2. Oracle inequality over a grid.

Apply the previous part conditionally on the training sample $T$, and then take expectation over $T$. Prove

$$\mathbb{E} L_{\mathcal{D}}(h_{\hat{\lambda}}) \le \min_{\lambda \in \Lambda} \inf_{u \in \mathcal{W}} \left\{ L_{\mathcal{D}}(u) + \lambda\Psi(u) + \frac{2G^2}{\lambda\alpha n_T} \right\} + \sqrt{\frac{\log(2K)}{2n_V}}.$$

Explain why selecting among $K$ trained RERM rules contributes a validation term of order $\sqrt{\frac{\log K}{n_V}}$.

### 3. Adapting to an unknown comparator scale.

For a comparator $u \in \mathcal{W}$, write $a = \Psi(u)$ and define

$$\lambda_{\text{opt}}(a) = \sqrt{\frac{2G^2}{\alpha a n_T}}$$

whenever $a > 0$.

Suppose $0 < B_{\min} \le B_{\max}$ and the grid $\Lambda$ has the following property: for every $a \in [B_{\min}^2, B_{\max}^2]$, there is a $\lambda \in \Lambda$ satisfying

$$\frac{\lambda_{\text{opt}}(a)}{2} \le \lambda \le 2\lambda_{\text{opt}}(a).$$

Prove that for every $u \in \mathcal{W}$ with $B_{\min}^2 \le \Psi(u) \le B_{\max}^2$,

$$\mathbb{E} L_{\mathcal{D}}(h_{\hat{\lambda}}) \le L_{\mathcal{D}}(u) + \frac{5\sqrt{2}}{2} \frac{G\sqrt{\Psi(u)}}{\sqrt{\alpha n_T}} + \sqrt{\frac{\log(2K)}{2n_V}}.$$

Your proof should explicitly optimize the two-term expression

$$\lambda\Psi(u) + \frac{2G^2}{\lambda\alpha n_T}$$

An up to the factor-2 discretization of $\lambda$.

### 4. A dyadic grid and the price of tuning.

Construct a dyadic grid $\Lambda$ satisfying the property in the previous part for all $a \in [B_{\min}^2, B_{\max}^2]$, where $0 < B_{\min} \le B_{\max}$. State the number of grid points $K$ as a function of $\frac{B_{\max}}{B_{\min}}$.

Assume $n$ is even, set $n_T = n_V = \frac{n}{2}$, and simplify the resulting guarantee. Identify the two statistical terms in the bound: the RERM learning term and the validation-selection term. Identify the additional term caused by not knowing the comparator scale $\Psi(u)$ in advance.

## Part B: Approximate RERM and Optimization Error

Let $\mathcal{W}$ be a convex parameter domain. Assume $\ell(w, z)$ is convex and $G$-Lipschitz with respect to $\|\cdot\|$, and $\Psi$ is nonnegative and $\alpha$-strongly convex with respect to $\|\cdot\|$. For $\lambda > 0$ and a sample $S$ of size $n$, define

$$F_S(w) = L_S(w) + \lambda\Psi(w), \quad w_S \in \arg\min_{w \in \mathcal{W}} F_S(w).$$

Let the actual algorithm return $\tilde{w}_S \in \mathcal{W}$ satisfying the deterministic optimization guarantee

$$F_S(\tilde{w}_S) \le F_S(w_S) + \eta$$

for every sample $S$, where $\eta \ge 0$.

You may use the exact RERM movement bound: if $S$ and $S'$ differ in one example, then

$$\|w_S - w_{S'}\| \le \frac{2G}{\lambda\alpha n}.$$

### 1. Approximate minimizers are close to exact minimizers.

Prove that for every sample $S$,

$$\|\tilde{w}_S - w_S\| \le \sqrt{\frac{2\eta}{\lambda\alpha}}.$$

### 2. Stability of approximate RERM.

Let $S$ and $S'$ differ in one example. Prove that for every test point $z$,

$$|\ell(\tilde{w}_S, z) - \ell(\tilde{w}_{S'}, z)| \le \frac{2G^2}{\lambda\alpha n} + 2G\sqrt{\frac{2\eta}{\lambda\alpha}}.$$

### 3. Learning guarantee with optimization error.

Prove the expected true-risk bound

$$\mathbb{E}_S L_{\mathcal{D}}(\tilde{w}_S) \le L_{\mathcal{D}}(u) + \lambda\Psi(u) + \frac{2G^2}{\lambda\alpha n} + G\sqrt{\frac{2\eta}{\lambda\alpha}}$$

for every comparator $u \in \mathcal{W}$.

### 4. How accurate must the optimizer be?

Suppose $B > 0$ and we want to compete with all $u \in \mathcal{W}$ satisfying $\Psi(u) \le B^2$. Use

$$\lambda = \sqrt{\frac{2G^2}{\alpha B^2 n}}$$

and simplify the bound from the previous part.

Give a sufficient condition on $\eta$ so that

$$G\sqrt{\frac{2\eta}{\lambda\alpha}} \le \frac{GB}{\sqrt{\alpha n}}.$$

State the resulting excess-risk bound under this condition.

### 5. Soft-margin linear classification.

Let

$$\ell(w, (e, y)) = (1 - y\langle w, x \rangle)_+, \quad y \in \{-1, +1\}, \quad \|x\|_2 \le R,$$

and use $\Psi(w) = \frac{1}{2}\|w\|_2^2$.

Specialize the bound from the previous part to compete with all $u$ satisfying $\|u\|_2 \le B$, and state the approximate-RERM bound in terms of $R, B, n,$ and $\eta$. Then give a sufficient condition on $\eta$ under which the optimization-error term is no larger than $\frac{RB}{\sqrt{n}}$.

## Part C: A Weighted Euclidean Geometry

Assume linear prediction with scalar loss convex and $g$-Lipschitz in the prediction. Let $b_1, \dots, b_d > 0$ and $r_1, \dots, r_d > 0$. Suppose

$$\mathcal{C}_b = \{w \in \mathbb{R}^d : |w_j| \le b_j \text{ for all } j\}$$

and $|\varphi_j(x)| \le r_j$ for all $x, j$.

For $Q = \text{diag}(q_1, \dots, q_d)$ with $q_j > 0$, define

$$\|w\|_Q = \sqrt{w^\top Q w}, \quad \Psi_Q(w) = \frac{1}{2}w^\top Q w.$$

You may use that $\Psi_Q$ is $1$-strongly convex with respect to $\|\cdot\|_Q$.

### 1. Geometry quantities.

Prove that

$$\|\varphi(x)\|_{Q,*}^2 \le \sum_{j=1}^d \frac{r_j^2}{q_j}, \quad \sup_{w \in \mathcal{C}_b} \Psi_Q(w) = \frac{1}{2} \sum_{j=1}^d q_j b_j^2.$$

### 2. Fixed $Q$.

Apply the Week 8 theorem and optimize over $\lambda$ to get

$$\mathbb{E} L_{\mathcal{D}}(A_\lambda(S)) \le \inf_{w \in \mathcal{C}_b} L_{\mathcal{D}}(w) + \frac{2g}{\sqrt{n}}\sqrt{\left(\sum_{j=1}^d q_j b_j^2\right)\left(\sum_{j=1}^d \frac{r_j^2}{q_j}\right)}.$$

### 3. Best diagonal geometry.

Optimize the right-hand side over $q_j > 0$ and show that the best excess term is

$$\frac{2g}{\sqrt{n}} \sum_{j=1}^d b_j r_j.$$

## Constraints
- Complete parts A and B and C; create a notebook `pa8.ipynb`
- **Jupyter Notebook JSON Structure**: When editing `.ipynb` files directly, special care must be taken with JSON escaping (i.e., `\\` - double backslash - for LaTeX backslashes) to avoid corrupting the notebook format
- Adhere to the specific open document format based on JSON syntax required of Jupyter notebook formatting; DO NOT construct scripts to build a notebook e.g., `build_notebook.py`
- Use separate cells for headers which are prefixed with `##`, exercise numbers are prefixed with `###` and are also separate from the proof sketches
- For exercises that need experiments, use separate Python cells; comments must reference theorems and lemmas for analysis
- Only append to `pa8.ipynb` using a markdown environment for your proofs, use `$...$`
- Look for the cells containing descriptive headers corresponding to each question; construct your proofs in these cells only
- Do not delete code or markdown cells; only a human can delete cells
- Save matplotlib images (if any) to `img/`
- There is no need to reference at `img/` beyond the inital saving
- **Before FIRST RUN, note the theorems required to investigate the proofs and inquire about it in `plan.md`; do not proceed without user update of `prompts/plan.md`**
- **For each SUBSEQUENT RUN, read `prompts/plan.md` for latest updates to theorems; do not make changes to `.ipynb` without reading**
- Nontrivial mistakes will be noted in `prompts/errors.md`; verify if these mistakes are indeed nontrivial for the section listed in `prompts/AGENTS.md`, and apply the correct theorem patches

## Deliverables
- (1) `pa8.ipynb` containing all proofs
- (1) `prompts/plan.md` that has been appended to with new blockers/notable items/nontrival proofs that require manual verification from this session

## Notes
- No permissions given to explore outside of hw8/
- You will not have any need to reference any additional files in hw6/
- All code and experiments should be contained in one Jupyter notebook
- Applicable theorems and lemmas will be noted in `PLAN.md`
- Your work will be verified with Claude