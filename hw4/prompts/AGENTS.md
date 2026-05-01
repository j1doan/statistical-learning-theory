# AGENTS.md: Formal Verification Professor

## Part A: Sparse Linear Predictors and Model Selection

This problem studies structural risk minimization in a setting where the complexity parameter is sparsity. The goal is to connect non-uniform learning bounds with the computational cost of searching over sparse predictors.

Let $\mathcal{X} = \mathbb{R}^d$ and $\mathcal{Y} = \{-1, +1\}$. Use the convention $\mathrm{sign}(z) = +1$ for $z \ge 0$ and $\mathrm{sign}(z) = -1$ for $z < 0$. For $1 \le k \le d$, define the class of $k$-sparse homogeneous linear classifiers
$$
\mathcal{H}_k = \{ x \mapsto \mathrm{sign}(\langle w, x \rangle) : w \in \mathbb{R}^d,\ \|w\|_0 \le k \}.
$$

Let $\mathcal{H} = \bigcup_{k=1}^d \mathcal{H}_k$. Let $\mathcal{D}$ be any distribution over $\mathcal{X} \times \mathcal{Y}$, and let $S = ((x_1, y_1), \dots, (x_n, y_n)) \sim \mathcal{D}^n$. When a weight vector $w$ is used as the argument of $L_S$ or $L_{\mathcal{D}}$, it denotes the classifier $x \mapsto \mathrm{sign}(\langle w, x \rangle)$.

### 1. VC dimension through supports.

Prove an upper bound of the form
$$
\mathrm{VCdim}(\mathcal{H}_k) = O\!\left(k \log\left(\frac{e d}{k}\right)\right).
$$

Hint: write $\mathcal{H}_k$ as a union over the possible supports of $w$, then combine the growth-function bounds for those subclasses.

### 2. Penalty-based SRM.

Choose a prior $p_k > 0$ over sparsity levels $k = 1, \dots, d$ with $\sum_{k=1}^d p_k \le 1$; for example, you may take $p_k \propto 1/k^2$. Define an SRM rule of the form
$$
\hat{h} \in \arg\min_{1 \le k \le d,\ h \in \mathcal{H}_k}
\{ L_S(h) + \mathrm{pen}(k, n, \delta) \}.
$$

Derive a high-probability oracle inequality of the form
$$
L_{\mathcal{D}}(\hat{h}) \le \inf_{1 \le k \le d,\ h \in \mathcal{H}_k}
\left\{
L_{\mathcal{D}}(h)
+ C \sqrt{\frac{k \log\left(\frac{e d}{k}\right) + \log\left(\frac{1}{p_k}\right) + \log\left(\frac{1}{\delta}\right)}{n}}
\right\}
$$
for a universal constant $C$.

You may use the class-level SRM theorem from lecture, but you must instantiate every term in the bound and explain what statistical cost is paid for choosing the support and what cost is paid for choosing the sparsity level.

### 3. Comparison with dense halfspaces.

Suppose there exists $w^* \in \mathbb{R}^d$ with $\|w^*\|_0 \le s$ and $L_{\mathcal{D}}(w^*) \le \eta$. Use the SRM bound above to state a sample size sufficient to guarantee
$$
L_{\mathcal{D}}(\hat{h}) \le \eta + \varepsilon
$$
with probability at least $1 - \delta$.

Then compare this with the sample size obtained by learning over all homogeneous halfspaces in $\mathbb{R}^d$. In what regime is the sparse bound smaller?

### 4. Validation as model selection.

Consider the following validation rule. Assume $n$ is even, and split the sample into two equal parts $S_1$ and $S_2$. For each $k = 1, \dots, d$, let
$$
w_k \in \arg\min_{\|w\|_0 \le k} L_{S_1}(w).
$$

Then choose the output $\hat{w} = w_{\hat{k}}$ with
$$
\hat{k} \in \arg\min_{1 \le k \le d} L_{S_2}(w_k).
$$

Prove a validation-style oracle bound of the form
$$
L_{\mathcal{D}}(w_{\hat{k}}) \le \inf_{1 \le k \le d,\ \|w\|_0 \le k}
\left\{
L_{\mathcal{D}}(w)
+ C \sqrt{\frac{k \log\left(\frac{e d}{k}\right) + \log\left(\frac{d}{\delta}\right)}{n}}
\right\}
$$
for a universal constant $C$.

Hint: after conditioning on $S_1$, the validation step is a finite-class selection problem over the candidates $w_1, \dots, w_d$.

Then compare this validation rule to the penalty-based SRM rule above: what samples are used to fit predictors, what samples are used to choose the complexity level, and what statistical price is paid for that separation?

### 5. Computation.

Now restrict attention to the realizable case. Suppose the sample is consistent with some $k$-sparse homogeneous halfspace. Describe the brute-force algorithm that enumerates supports $I \subseteq [d]$ with $|I| = k$ and solves a halfspace feasibility problem on each support. Estimate its runtime as a function of $d$, $k$, and $n$.

In which regimes of $k$ is this polynomial in $d$? Explain how this illustrates the Week 4 distinction between sample complexity and computational complexity.


## Part B: PAC-Bayes for Thresholds

PAC-Bayes bounds use $\mathrm{KL}(Q \| P)$ as the complexity term. This problem compares that term with VC dimension for thresholds on a finite ordered domain.

Throughout, let $\mathcal{X}_N = \{1, 2, \dots, N\}$, $\mathcal{Y} = \{0, 1\}$, and define the threshold class
$$
\mathcal{H}_N = \{h_t : t \in \{1, \dots, N+1\}\},
$$
where
$$
h_t(x) = \mathbf{1}[x \ge t].
$$

Thus $h_1$ labels every point by 1, and $h_{N+1}$ labels every point by 0.

We use the PAC-Bayes bound: for any distribution $\mathcal{D}$ over $\mathcal{X}_N \times \mathcal{Y}$ and any prior $P$, with probability at least $1 - \delta$ over $S \sim \mathcal{D}^n$, simultaneously for all posteriors $Q$,
$$
L_{\mathcal{D}}(Q) \le L_S(Q) + \sqrt{\frac{\mathrm{KL}(Q \| P) + \log\left(\frac{2n}{\delta}\right)}{2(n-1)}}.
$$

where
$$
L_{\mathcal{D}}(Q) = \mathbb{E}_{h \sim Q}[L_{\mathcal{D}}(h)], \quad
L_S(Q) = \mathbb{E}_{h \sim Q}[L_S(h)].
$$

We work in the realizable setting.

### 1. VC dimension and point-posterior PAC-Bayes.

Prove that
$$
\mathrm{VCdim}(\mathcal{H}_N) = 1.
$$

Let $P$ be the uniform prior over $\mathcal{H}_N$, let $A(S)$ be any deterministic ERM rule returning a consistent threshold $\hat{h}_t$, and define $Q_S = \delta_{\hat{h}_t}$.

Compute $\mathrm{KL}(Q_S \| P)$, plug it into the PAC-Bayes theorem, and write the resulting bound on $L_{\mathcal{D}}(Q_S)$.

Finally, explain in 2–3 sentences why this PAC-Bayes certificate scales with $\log(N+1)$ even though a VC-style realizable guarantee for thresholds should not scale with $\log N$.

### 2. Version-space posterior.

Define
$$
a(S) = \max\{x_i : y_i = 0\}, \quad a(S)=0 \text{ if no negatives},
$$
$$
b(S) = \min\{x_i : y_i = 1\}, \quad b(S)=N+1 \text{ if no positives}.
$$

Prove that the consistent thresholds are
$$
V(S) = \{t : a(S) < t \le b(S)\},
$$
and hence $|V(S)| = b(S) - a(S)$.

Let $Q_V$ be uniform over $\{h_t : t \in V(S)\}$. For uniform prior $P$, compute
$$
\mathrm{KL}(Q_V \| P)
$$
exactly.

Prove that $L_S(Q_V)=0$, and explain why $Q_V$ can give a better PAC-Bayes bound than a point posterior when $|V(S)|$ is large.

### 3. Spreading helps KL, but can hurt true risk.

Let $P$ be uniform over $\mathcal{H}_N$. Let $\mathcal{D}$ be realizable with marginal uniform on $\mathcal{X}_N$ and labels generated by $h_\tau$.

For any nonempty $W \subseteq \{1, \dots, N+1\}$, let $Q_W$ be uniform over $\{h_t : t \in W\}$. Prove
$$
L_{\mathcal{D}}(Q_W) = \frac{1}{N|W|} \sum_{t \in W} |t - \tau|.
$$

Construct a concrete example with $N \ge 20$, a threshold $\tau$, and a realizable sample $S$ such that:
- $|V(S)|$ is large,
- $\mathrm{KL}(Q_{V(S)} \| P) < \mathrm{KL}(\delta_{h_\tau} \| P)$,
- but $L_{\mathcal{D}}(Q_{V(S)}) > L_{\mathcal{D}}(\delta_{h_\tau})$.

Explain why this does not contradict PAC-Bayes.

### 4. Every fixed prior can be attacked.

Let $P$ be any prior over $\mathcal{H}_N$, fixed before seeing data. Assume $N \ge 3$.

Prove that there exists $\tau \in \{2, \dots, N\}$ such that
$$
P(h_\tau) \le \frac{1}{N-1}.
$$

Define $\mathcal{D}_\tau$ by
$$
\mathbb{P}[x=\tau-1,y=0]=\frac{1}{2}, \quad \mathbb{P}[x=\tau,y=1]=\frac{1}{2}.
$$

Prove that with probability at least $1 - 2^{1-n}$, the sample contains both support points.

On this event, prove $V(S)=\{\tau\}$ and thus any zero-empirical-error posterior must be $Q=\delta_{h_\tau}$.

Show that on this event,
$$
\mathrm{KL}(Q \| P) \ge \log(N-1).
$$

Explain what this lower bound does and does not show. In particular, why is this a limitation of zero-empirical-error PAC-Bayes certificates with a fixed prior, rather than a lower bound on the sample complexity of learning thresholds.

## Constraints
- Complete parts A and B
- - **Jupyter Notebook JSON Structure**: When editing `.ipynb` files directly, special care must be taken with JSON escaping (e.g., `\\` for LaTeX backslashes) to avoid corrupting the notebook format
- You will only append to `pa4.ipynb` using a markdown environment for your proofs
- Look for the cells containing descriptive headers corresponding to each question; construct your proofs in these cells only
- Do not delete code or markdown cells; only a human can delete cells
- **There is no need to write code to edit the notebook cells; edit the cell directly**
- There is no need to look at `img` folder
- Adhere to the specific open document format based on JSON syntax required of Jupyter notebook formatting; DO NOT construct scripts to build a notebook e.g., `build_notebook.py`
- **Before EVERY run, read `plan.md` IMMEDIATELY after reading this document**; no exceptions
- **After EVERY run, IMMEDIATELY update `plan.md` before doing anything else**; no exceptions
- Do not start the next exploration until the previous one is documented here.
- Nontrivial mistakes will be noted in `errors.md`; verify if these mistakes are indeed nontrivial for the section listed in `AGENTS.md` (this document), and apply the correct theorem patches
- Cite the references used in the development of these mini-courses, use your `search` tool proof sketches; the Lean4 mathlib documentation is a good place to start looking for theorems

## Deliverables
- (1) `.ipynb` containing all proofs
- (1) `plan.md` that has been appended to with new blockers/notable items/nontrival proofs that require manual verification from this session

## Notes
- No permissions given to explore outside of hw4/
- You will not have any need to reference any additional files in hw4/
- All code and experiments should be contained in one Jupyter notebook
- Applicable theorems and lemmas will be noted in `PLAN.md`
- Your work will be verified with Claude