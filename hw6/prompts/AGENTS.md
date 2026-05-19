# AGENTS.md

## Part A: Boosting Sparse Linear Predictors and the $\ell_1$ Margin

Let $\phi : \mathcal{X} \to \{-1, +1\}^d$ be a fixed feature map. For each $j \in [d]$ and $\sigma \in \{-1, +1\}$, define $b_{j,\sigma}(x) = \sigma \phi_j(x)$, and let $\mathcal{B} = \{b_{j,\sigma} : j \in [d], \sigma \in \{-1, +1\}\}$. For a $\{-1, +1\}$-valued predictor $b$, its edge under a distribution $Q$ is $\frac{1}{2} - L_Q(b) = \mathbb{E}_Q \frac{[y b(x)]}{2}$.

Assume $\mathcal{D}$ is realizable with margin by an $s$-sparse predictor: there is $w^\star \in \mathbb{R}^d$ with $\lVert w^\star \rVert_0 \le s$ and $y \langle w^\star, \phi(x) \rangle \ge 1$ for every $(x,y)$ in the support of $\mathcal{D}$. Equivalently, $\frac{w^\star}{\lVert w^\star \rVert_1}$ has $\ell_1$-normalized margin at least $\frac{1}{\lVert w^\star \rVert_1}$. When a finite sample is used, write $S = ((x_1, y_1), \dots, (x_n, y_n))$.

You may use without proof that sparse linear classifiers have VC dimension $O(s \log(e \frac{d}{s}))$, so exact sparse ERM has realizable sample complexity $O\left(\frac{s \log(e \frac{d}{s}) + \log(\frac{1}{\delta})}{\varepsilon}\right)$ up to logarithmic factors, but is computationally difficult when $s$ is part of the input.

### 1. From sparse margin to a weak coordinate.

Assume additionally that $\lVert w^\star \rVert _\infty \le B$. For any distribution $Q$ supported on examples satisfying the margin condition, prove that some $b \in \mathcal{B}$ has
$L_Q(b) \le \frac{1}{2} - \frac{1}{2 \lVert w^\star \rVert_1}$,
and hence
$L_Q(b) \le \frac{1}{2} - \frac{1}{2sB}$.

Then describe an $O(nd)$ weighted ERM weak learner for $\mathcal{B}$ on weighted examples $(x_i, y_i, D_i)_{i=1}^n$. Hint: relate weighted error to the signed correlation $\sum_i D_i y_i b(x_i)$.

### 2. Boosting guarantee and comparison with sparse ERM.

Run AdaBoost over $\mathcal{B}$. At every round, the reweighted distribution is supported on the same margin-realizable sample, so the previous part applies with $\gamma = \frac{1}{2sB}$. Prove the exponential training-error bound, choose $T$ so that the training error is zero, and then use the sparse-linear VC bound, applied with the number of activated coordinates in place of $s$, to obtain a realizable generalization guarantee.

State the resulting sample complexity up to logarithmic factors, and compare it with exact sparse ERM. Your comparison should identify the statistical price paid by boosting, the computational advantage, and the role of $B$.

### 3. Why the coefficient bound matters.

For odd $s = 2m + 1$, set $d = s$. Construct a distribution supported on $s$ labeled examples with $y = +1$ and $\phi(x) \in \{-1, +1\}^s$ such that some $w^\star \in \mathbb{R}^s$ has margin $1$, but every coordinate predictor has edge at most $2^{-\Omega(s)}$. Also show that the realizing vector in your construction satisfies $\lVert w^\star \rVert _\infty = 2^{\Omega(s)}$.

Hint: index rows by $0, (1,+), (1,-), \dots, (m,+), (m,-)$ with weights $q_0 = 1$ and $q_{r,+} = q_{r,-} = 2^{r-1}$. It suffices to build an invertible $s \times s$ sign matrix whose every column has weighted sum $1$; try a base column with $(+, -)$ on every pair, columns that flip one pair, and carry columns with $(-,-)$ on earlier pairs, $(+,+)$ on one pair, and $(+,-)$ later. Prove realizability, compute the best coordinate edge, and explain why this rules out any polynomial-in-$s$ AdaBoost guarantee based only on sparsity.

### 4. Experiment: sparse boosting versus a convex surrogate.

Implement AdaBoost over the coordinate class $\mathcal{B}$. Compare an easy sparse-margin distribution of your choice with the construction from the previous part. Report training error, exponential loss, observed edge, support size, and normalized margin over rounds. Compare AdaBoost with one convex surrogate method, for example logistic regression or hinge-loss minimization with an $\ell_1$ constraint or penalty. Explain what the experiment illustrates about support sparsity, coefficient size, $\ell_1$ margin, and computational tractability.

## Part B: Agnostic Halfspace Hardness via Boosting

Part A used boosting constructively; here boosting is a reduction tool.

Let $\mathcal{X}_d = \mathbb{R}^d$ and $\mathcal{Y} = \{-1, +1\}$. Let $\mathcal{H}_d$ be the class of affine halfspaces $h_{w,b}(x) = \operatorname{sign}(\langle w, x \rangle + b)$, with $\operatorname{sign}(z) = +1$ for $z \ge 0$. Let $\mathcal{I}_{d,k}$ be the class of intersections of $k$ halfspaces: the output is $+1$ iff all $k$ halfspaces output $+1$. For a size function $k = k(d)$, polynomial-size means $k(d) \le d^c$ for some fixed constant $c$, and $k(d) = \omega(1)$ means $k(d) \to \infty$.

Use these black-box hardness facts: under standard $\mathrm{uSVP}$ hardness, intersections of $d^r$ affine halfspaces are not efficiently PAC learnable in the realizable case, even improperly, for every fixed $r > 0$; under $\mathrm{RSAT}$, the same is true for intersections of $k(d) = \omega(1)$ affine halfspaces.

### 1. A weak halfspace inside an intersection.

Prove: if $\mathcal{D}$ is realizable by some $g \in \mathcal{I}_{d,k}$, then some affine halfspace has error at most
$\frac{1}{2} - \frac{1}{2k^2}$.

Hint: split on $p = \mathbb{P}[y = +1]$. For small $p$, use the constant $-1$ halfspace; for large $p$, average over the $k$ halfspaces defining the realizing intersection.

### 2. From an agnostic learner to a weak learner.

Suppose, hypothetically, that affine halfspaces are efficiently properly agnostically PAC learnable. Use the previous lemma to construct a weak learner for $\mathcal{I}_{d,k}$ in the realizable case. Give $\gamma$ such that the returned halfspace has error at most $\frac{1}{2} - \gamma$, and explain why the weak learner is polynomial-time when $k(d) \le d^c$ for a fixed constant $c$.

### 3. Boosting the weak learner.

Use AdaBoost and the boosted-halfspace VC bound $\widetilde{O}(Td)$ to obtain a realizable learner for $\mathcal{I}_{d,k}$. At every round, the weighted distribution is supported on examples still realized by the same intersection. State the sample and runtime dependence up to logarithmic factors.

### 4. Consequence for agnostic halfspaces.

Prove the implication: if affine halfspaces are efficiently properly agnostically PAC learnable, then intersections of $k(d) \le d^c$ affine halfspaces are efficiently learnable in the realizable case, for every fixed $c$.

Explain the contradiction with the black-box hardness facts by taking $k(d) = d^r$ under $\mathrm{uSVP}$, or any polynomially bounded $k(d) = \omega(1)$ under $\mathrm{RSAT}$. Conclude the implication for efficient proper agnostic PAC learning of halfspaces.

## Constraints
- Complete parts A and B; create a notebook `pa6.ipynb`
- **Jupyter Notebook JSON Structure**: When editing `.ipynb` files directly, special care must be taken with JSON escaping (i.e., `\\` - double backslash - for LaTeX backslashes) to avoid corrupting the notebook format
- Adhere to the specific open document format based on JSON syntax required of Jupyter notebook formatting; DO NOT construct scripts to build a notebook e.g., `build_notebook.py`
- Use separate cells for headers which are prefixed with `##`, exercise numbers are prefixed with `###` and are also separate from the proof sketches
- For exercises that need experiments, use separate Python cells; comments must reference theorems and lemmas for analysis
- Only append to `pa6.ipynb` using a markdown environment for your proofs, use `$...$`
- Look for the cells containing descriptive headers corresponding to each question; construct your proofs in these cells only
- Do not delete code or markdown cells; only a human can delete cells
- Save matplotlib images (if any) to `img/`
- There is no need to reference at `img/` beyond the inital saving
- **Before FIRST RUN, note the theorems required to investigate the proofs and inquire about it in `plan.md`; do not proceed without user update of `prompts/plan.md`**
- **For each SUBSEQUENT RUN, read `prompts/plan.md` for latest updates to theorems; do not make changes to `.ipynb` without reading**
- Nontrivial mistakes will be noted in `prompts/errors.md`; verify if these mistakes are indeed nontrivial for the section listed in `prompts/AGENTS.md`, and apply the correct theorem patches

## Deliverables
- (1) `pa6.ipynb` containing all proofs
- Scikit-learn Adaboost experimental code for A2, A4, B3
- (1) `prompts/plan.md` that has been appended to with new blockers/notable items/nontrival proofs that require manual verification from this session

## Notes
- No permissions given to explore outside of hw6/
- You will not have any need to reference any additional files in hw6/
- All code and experiments should be contained in one Jupyter notebook
- Applicable theorems and lemmas will be noted in `PLAN.md`
- Your work will be verified with Claude