# AGENTS.md

## Part A: Kernel Methods

Let $\mathcal{U}$ be a Hilbert space with inner product $\langle\cdot, \cdot\rangle$ and induced norm $\|\cdot\|$, and let $\varphi : \mathcal{X} \to \mathcal{U}$ be a feature map with associated kernel $K(x, x') = \langle\varphi(x), \varphi(x')\rangle$.

For $B > 0$, let $\mathcal{H}_{K,B} = \{x \to \langle w, \varphi(x)\rangle : w \in \mathcal{U}, \|w\| \le B\}$ be the predictors of RKHS norm at most $B$.

For a sample $S = (x_1, \dots, x_n)$ and a real-valued function class $\mathcal{F}$, write the empirical Rademacher complexity:

$$\hat{\mathcal{R}}_S(\mathcal{F}) = \mathbb{E}_{\sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(x_i) \right]$$

where $\sigma_1, \dots, \sigma_n$ are independent uniform signs, and write $\mathcal{R}_{\mathcal{D}}^n(\mathcal{F}) = \mathbb{E}_{S \sim \mathcal{D}^n} [\hat{\mathcal{R}}_S(\mathcal{F})]$.

### 1. Norm-based kernel bound

Prove the empirical bound:

$$\hat{\mathcal{R}}_S(\mathcal{H}_{K,B}) \le \frac{B}{n} \sqrt{\sum_{i=1}^n K(x_i, x_i)}$$

and conclude the distribution-level bound:

$$\mathcal{R}_{\mathcal{D}}^n(\mathcal{H}_{K,B}) \le B \sqrt{\frac{\mathbb{E}[K(X, X)]}{n}}$$

### 2. Representer theorem

The space $\mathcal{U}$ may be infinite-dimensional, yet for any $\lambda > 0$ the regularized objective

$$J(w) = \frac{1}{n} \sum_{i=1}^n \text{loss}(\langle w, \varphi(x_i)\rangle; y_i) + \lambda\|w\|^2$$

can be minimized over finitely many coefficients.

This is the representer theorem: prove that whenever $J$ attains a minimum over $w \in \mathcal{U}$, some minimizer has the form

$$w^* = \sum_{j=1}^n \alpha_j \varphi(x_j), \quad \alpha \in \mathbb{R}^n$$

Then rewrite $J$ as a minimization over $\alpha \in \mathbb{R}^n$ in which the data enter only through the Gram matrix $K_S$, with entries $(K_S)_{ij} = K(x_i, x_j)$.

## Part B: $\ell_1$ Rademacher Complexity

Throughout this part, $\hat{\mathcal{R}}_S$ denotes the empirical Rademacher complexity defined in Part A.

### 1. Convex hulls

Let $\mathcal{F}$ be a finite class of real-valued functions. Its convex hull is defined as:

$$\text{conv}(\mathcal{F}) = \left\{ \sum_{f \in \mathcal{F}} a_f f : a_f \ge 0, \sum_{f \in \mathcal{F}} a_f = 1 \right\}$$

Prove that empirical Rademacher complexity is unchanged by taking the convex hull:

$$\hat{\mathcal{R}}_S(\text{conv}(\mathcal{F})) = \hat{\mathcal{R}}_S(\mathcal{F})$$

### 2. $\ell_1$ linear predictors

Let $\varphi : \mathcal{X} \to \mathbb{R}^d$ satisfy $\|\varphi(x)\|_\infty \le R$ for all $x$, and define:

$$\mathcal{H}_B^1 = \{x \to \langle w, \varphi(x)\rangle : \|w\|_1 \le B\}$$

Derive a logarithmic-in-dimension Rademacher bound for $\mathcal{H}_B^1$.

> **Hint:** Massart’s finite-class lemma bounds the Rademacher complexity of a finite class; the convex-hull identity from the previous problem is what connects $\mathcal{H}_B^1$ to such a class.

### 3. Comparison with sparsity bounds

In Homework 4 you showed that the class of $k$-sparse linear classifiers in $\mathbb{R}^d$ has VC dimension $\mathcal{O}(k \log(ed/k))$. With the VC generalization bound, with probability at least $1 - \delta$ over the draw of $S \sim \mathcal{D}^n$, every $k$-sparse linear classifier $h$ satisfies:

$$L_{\mathcal{D}}^{0/1}(h) - L_S^{0/1}(h) \le C \sqrt{\frac{k \log(ed/k) + \log(1/\delta)}{n}}$$

for a universal constant $C$; structural risk minimization makes the bound adapt to the unknown sparsity level $k$.

Using your Rademacher bound from the previous problem and the uniform convergence theorem, derive the analogous bound for $\mathcal{H}_B^1$: a bound on $L_{\mathcal{D}}^\ell(w) - L_S^\ell(w)$, holding with probability at least $1 - \delta$ over the draw of $S \sim \mathcal{D}^n$, uniformly over $\|w\|_1 \le B$, for a fixed loss $\ell$ that is $G$-Lipschitz in the prediction and bounded in $[0, 1]$.

These two bounds control different loss functionals, so they are not interchangeable guarantees. Compare them across the following criteria:

- Which quantity represents the complexity in each bound, and which one is scale-sensitive?
- What extra step does the $\ell_1$ bound need before it can say anything about $0/1$ error?
- Exhibit a predictor for which the sparsity bound is vacuous (useless) while the $\ell_1$ bound is not.

## Part C: Normalized $\ell_1$ margins and Fixed Boost

In this part, the sample is $S = ((x_1, y_1), \dots, (x_n, y_n))$ with labels $y_i \in \{-1, +1\}$, and $\mathcal{G}$ is a finite base class of binary predictors $g : \mathcal{X} \to \{-1, +1\}$, symmetric in the sense that $-g \in \mathcal{G}$ whenever $g \in \mathcal{G}$.

A coefficient vector $w = (w_g)_{g \in \mathcal{G}}$ parameterizes the real-valued predictor:

$$f_w(x) = \sum_{g \in \mathcal{G}} w_g g(x)$$

with the empirical normalized $\ell_1$ margin defined whenever $\|w\|_1 > 0$ as:

$$\text{margin}_S(w) = \min_{i} \frac{y_i f_w(x_i)}{\|w\|_1}$$

For a distribution $D$ over the $n$ training examples, the weighted error of a predictor $g$ is $\sum_{i} D_i \mathbb{1}[g(x_i) \neq y_i]$.

AdaBoost chooses its step size adaptively to drive training error down quickly. **FixedBoost** instead uses a fixed step size, so the $\ell_1$ scale of the ensemble grows in a controlled way with the number of rounds. This makes the round count an explicit complexity knob and lets boosting be read as a search for a large normalized $\ell_1$ margin, the theme of this part.

> ### FixedBoost Algorithm
> 
> 
> Given a step size $\eta > 0$ and a number of rounds $T$, FixedBoost starts from $w_0 = 0$ and the uniform distribution $D_1$ over the $n$ training examples. For each round $t = 1, \dots, T$:
> * Pick a base predictor $g_t$ maximizing the weighted correlation $\sum_{i} D_{t,i} y_i g_t(x_i)$.
> * Set $w_t = w_{t-1} + \eta e_{g_t}$, adding $\eta$ to the weight of $g_t$.
> * Reweight the examples by $D_{t+1,i} \propto \exp(-y_i f_{w_t}(x_i))$.
> 
> 
> FixedBoost outputs the coefficient vector $w_T$.

### 1. Margin generalization

Assume $S$ is drawn i.i.d. from a population distribution $\mathcal{D}$ over $\mathcal{X} \times \{-1, +1\}$. Prove a population $0/1$ error bound for predictors with empirical normalized margin $\text{margin}_S(w) \ge \gamma$ for some $\gamma > 0$.

Build on the generalization-gap bound from B3, specialized to the ramp surrogate from lecture, rescaled to $\gamma$. State the final bound explicitly in terms of $|\mathcal{G}|$, $n$, $\gamma$, and $\delta$.

### 2. FixedBoost implication

Use the following theorem about FixedBoost as a black box:

> If every distribution $D$ over the training sample admits a base predictor of weighted error at most $\frac{1}{2} - \frac{\gamma}{2}$, then after $T = \mathcal{O}\left(\frac{\log(n)}{\gamma^4}\right)$ rounds, FixedBoost returns coefficients $w_T$ satisfying:
> 
> $$\min_{i} y_i f_{w_T}(x_i) \ge \frac{\gamma}{2} \|w_T\|_1$$
> 
> 

Derive a generalization guarantee for the classifier returned by FixedBoost.

### 3. Weak learning and normalized margin

Encode the sample and base class as the matrix $A \in \{-1, +1\}^{n \times |\mathcal{G}|}$ with $A_{ig} = y_i g(x_i)$. The **weak-learning edge** of a base predictor $g$ under a distribution $D$ over the sample is $\frac{1}{2}$ minus its weighted error, representing its advantage over random guessing under $D$. The sample's **best weak-learning edge** is the largest $\gamma$ such that every distribution $D$ over the sample admits some $g \in \mathcal{G}$ with edge at least $\gamma$.

Prove the exact relationship between the best weak-learning edge and the best normalized $\ell_1$ margin $\max_{w} \text{margin}_S(w)$, using von Neumann's minimax theorem applied to $A$.

### 4. Connection to Homework 6

Explain how this margin-based view refines the sparse-boosting analysis from Homework 6. Your answer should identify:

1. What changes in the comparator.
2. What changes in the generalization argument.

## Part D: FixedBoost Margin Experiment

The base class is the $2d$ signed coordinate predictors on Boolean inputs $x \in \{-1, +1\}^d$: the maps $x \to x_j$ and $x \to -x_j$ for $j \in [d]$. This is a finite symmetric base class in the sense of Part C.

For a labeled sample $((x_1, y_1), \dots, (x_n, y_n))$, form the sign matrix $A$ with $A_{ig} = y_i g(x_i)$, equal to $+1$ when $g$ is correct on example $i$ and $-1$ otherwise. FixedBoost interacts with the data only through $A$: its weighted correlations, ensemble margins, and reweighting are all functions of $A$ alone.

This experiment tests whether FixedBoost drives the normalized $\ell_1$ margin toward the largest value attainable on a given $A$. Designing the data is part of the task: choose how the labeled examples $(x_i, y_i)$ are generated, and describe it precisely enough that someone could reproduce your runs. You may use NumPy, plotting libraries, and a linear-programming solver for the optimal-margin computation, but the FixedBoost loop must be your own.

### 1. Implementation

Implement FixedBoost from scratch, running directly on the matrix $A$, with a fixed step size. Track $\|w_t\|_1$ and the normalized empirical margin over rounds.

> **Note:** You may reuse a boosting harness from Homework 6; state clearly what differs from it.

### 2. Optimal-margin comparison

Formulate the optimal normalized $\ell_1$ margin attainable on a matrix $A$ as a linear program, and solve it. On the same matrix $A$, plot FixedBoost’s normalized-margin trajectory against this optimal value.

Do this for at least two instances:

1. One with a **large optimal margin**.
2. One harder instance where the **optimal margin is small**.

Address the following in your response:

- What structure in $A$ makes the optimal margin large, and what makes it small? (The relationship you proved in C3 is one way to reason about this).
- Construct the two instances accordingly, and report each construction precisely.

### 3. Interpretation

Does FixedBoost’s normalized margin approach the optimal value, and how fast?

Compare the observed behavior with the rate implied by the FixedBoost theorem in C2. Identify at least one place where that theory is loose, vacuous, or silent relative to what you actually observe.

## Constraints
- Complete parts A and B; create a notebook `pa7.ipynb`
- **Jupyter Notebook JSON Structure**: When editing `.ipynb` files directly, special care must be taken with JSON escaping (i.e., `\\` - double backslash - for LaTeX backslashes) to avoid corrupting the notebook format
- Adhere to the specific open document format based on JSON syntax required of Jupyter notebook formatting; DO NOT construct scripts to build a notebook e.g., `build_notebook.py`
- Use separate cells for headers which are prefixed with `##`, exercise numbers are prefixed with `###` and are also separate from the proof sketches
- For exercises that need experiments, use separate Python cells; comments must reference theorems and lemmas for analysis
- Only append to `pa7.ipynb` using a markdown environment for your proofs, use `$...$`
- Look for the cells containing descriptive headers corresponding to each question; construct your proofs in these cells only
- Do not delete code or markdown cells; only a human can delete cells
- Save matplotlib images (if any) to `img/`
- There is no need to reference at `img/` beyond the inital saving
- **Before FIRST RUN, note the theorems required to investigate the proofs and inquire about it in `plan.md`; do not proceed without user update of `prompts/plan.md`**
- **For each SUBSEQUENT RUN, read `prompts/plan.md` for latest updates to theorems; do not make changes to `.ipynb` without reading**
- Nontrivial mistakes will be noted in `prompts/errors.md`; verify if these mistakes are indeed nontrivial for the section listed in `prompts/AGENTS.md`, and apply the correct theorem patches
- Refer to `pa6.ipynb` when "Homework 6" needs to be referenced

## Deliverables
- (1) `pa7.ipynb` containing all proofs
- Custom numpy FixedBoost experimental code for ### Part D
- (1) `prompts/plan.md` that has been appended to with new blockers/notable items/nontrival proofs that require manual verification from this session

## Notes
- No permissions given to explore outside of hw7/
- You will not have any need to reference any additional files in hw6/
- All code and experiments should be contained in one Jupyter notebook
- Applicable theorems and lemmas will be noted in `PLAN.md`
- Your work will be verified with Claude