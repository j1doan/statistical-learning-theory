# AGENTS.md: Formal Verification Specialist

## Role & Objective
You are an expert in formal verification with a specialization in learning theory. Your goal is to prove learning theory mathematics in a comphrehesive exam stlye in a modern Jupyter notebook.

## Task (Part A)
Complete the following objectives.
---
Let

$\mathcal{H}_2 = \left\{ x \mapsto \mathbf{1}\!\left[x \in I_1 \cup I_2\right] \;:\; I_1, I_2 \subseteq \mathbb{R} \text{ are intervals} \right\}$

In other words, a hypothesis in $\mathcal{H}_2$ labels a point by 1 iff it lies in a union of at most two intervals on the real line. Empty intervals are allowed, so this really means “at most two.”

Throughout this part, fix ordered points

$𝑥_1 < 𝑥_2 < … < 𝑥_𝑛$.
---
1. Restriction patterns.

Characterize exactly which binary labelings of $(𝑥_1, …, 𝑥_𝑛)$ can be realized by $\mathcal{H}_2$.

A good answer should not just list examples. It should identify the structural property that distinguishes realizable labelings from impossible ones.
---
2. Exact growth function.

Use your characterization to derive a closed-form formula for the growth function

$\Gamma_{\mathcal{H}_2}(n)$.

You may first use small cases to guess the formula, but your final answer must be a proof.
---
3. VC dimension and mistake bound.

Determine the exact value of

$VCdim(\mathcal{H}_2)$.

Then use your exact growth formula to write down the Halving mistake bound on an 𝑛-point pool in the realizable online transductive setting.

Finally, compare your exact growth formula with the Sauer–Shelah bound obtained from your VC-dimension calculation. Are they equal in this case? What does this tell you about when a VC-dimension-based upper bound can be tight?
---
4. Tightness of Sauer–Shelah.

For arbitrary integers 𝑛 ≥ 𝑑 ≥ 0, give a concrete hypothesis class \mathcal{H} on some domain \mathcal{X} such that

$VCdim(\mathcal{H}) = 𝑑$

and

$\Gamma_H(n) = \sum_{k=0}^{d} \binom{n}{k}$

What does your example show about the Sauer–Shelah bound?
---
5. AI proof audit.

An AI assistant claims:

> On an ordered 𝑛-point sample, a labeling realized by ℋ︀ 2 is determined by the places where the labels switch between 0 and 1. Since a union of at most two intervals can create at most four such switches, one just chooses up to four switch locations among the 𝑛 sample positions. Therefore

> $\sum_{j=0}^{4} \binom{n}{j}$.

> Hence

> $\Gamma_{\mathcal{H}_2}(n) = \sum_{j=0}^{4} \binom{n}{j}$

> and in particular

> $VCdim(\mathcal{H}_2) = 4$.

A flawed argument may still arrive at a true conclusion; analyze the reasoning, not just the final claim.

Explain carefully what is incomplete or incorrect in this argument. Then replace it with a correct statement that is actually supported by your work above.

## Task (Part B)
Complete the following objectives.
---
Let

$\mathcal{H}_{quad} = \left\{ x \mapsto \mathbf{1}\!\left[a x^2 + b x + c \ge 0\right] \;:\; (a,b,c) \in \mathbb{R}^3,\ (a,b,c) \neq (0,0,0) \right\}$

So a hypothesis in $\mathcal{H}_{quad}$ is the indicator of the nonnegative region of a quadratic polynomial.

Throughout this part, again fix ordered points

$𝑥_1 < 𝑥_2 < … < 𝑥_𝑛$.
---
1. A general upper-bound trick.

Prove the following statement.

If there exist an integer $𝐷 \geq 1$ and a transformation

$\phi : \mathcal{X} \to \mathbb{R}^D$

such that every hypothesis $h \in \mathcal{H}$ can be written in the form

$h(x) = \mathbf{1}\!\left[\langle w, \phi(x) \rangle \ge 0\right]$

for some vector $w \in \mathbb{R}^D$, then

$\mathrm{VCdim}(\mathcal{H}) \leq D$.

You may use the Week 2 result that homogeneous halfspaces in $\mathbb{R}^D$ have VC dimension 𝐷.
---
2. Apply the trick to quadratic thresholds.

Find an explicit transformation

$\phi : \mathbb{R} \to \mathbb{R}^3$

such that every hypothesis in \mathcal{H}_{quad} can be written in the form

$h(x) = \mathbf{1}\!\left[\langle w, \phi(x) \rangle \ge 0\right]$, 

for some

$w \in \mathbb{R}^3$.

Then use the previous item to prove an upper bound on

$VCdim(\mathcal{H}_{quad})$.
---
3. Exact restriction patterns.

Characterize exactly which binary labelings of $(𝑥_1, …, 𝑥_𝑛)$ are realizable by $\mathcal{H}_{quad}$.

Your characterization should make clear how the algebraic structure of a quadratic polynomial controls the combinatorics of its restriction to an ordered finite set.
---
4. Exact growth and exact VC dimension.

Use your characterization to compute the exact growth function

$\Gamma_{\mathcal{H}_{quad}}(n)$

and the exact VC dimension of $\mathcal{H}_{quad}$.

Then compare your exact growth formula with the Sauer–Shelah bound obtained from your VC-dimension calculation. Is the VC-based upper bound tight here?

Explain what your answer says about VC dimension as a summary of finite-pool richness.
---
5. AI proof audit.

An AI assistant claims:

> A quadratic polynomial has at most two real roots, so on an ordered sample its labels can change from 0 to 1 or from 1 to 0 at most twice. Therefore one chooses up to two change-points among the 𝑛 − 1 gaps and gets

> $\Gamma_{\mathcal{H}_{quad}}(n) = \sum_{j=0}^{2} \binom{n-1}{j}$.

> In particular,

> $VCdim(\mathcal{H}_{quad}) = 3$.

A flawed argument may still arrive at a true conclusion; analyze the reasoning, not just the final claim.

Explain carefully what is incomplete or incorrect in this argument. Then replace it with a correct theorem that is genuinely justified by your work in this part.

## Constraints
- Complete parts A and B
- - **Jupyter Notebook JSON Structure**: When editing `.ipynb` files directly, special care must be taken with JSON escaping (e.g., `\\` for LaTeX backslashes) to avoid corrupting the notebook format
- You will only append to `pa2.ipynb` using a markdown environment for your proofs
- Look for the cells containing descriptive headers corresponding to each question; construct your proofs in these cells only
- Do not delete code or markdown cells; only a human can delete cells
- There is no need to write code
- There is no need to look at `img` folder
- Adhere to the specific open document format based on JSON syntax required of Jupyter notebook formatting; DO NOT construct scripts to build a notebook e.g., `build_notebook.py`
- **After EVERY run, IMMEDIATELY update this file `plan.md` before doing anything else**; no exceptions
- Do not start the next exploration until the previous one is documented here.
- Nontrivial mistakes will be noted in `errors.md`; verify if these mistakes are indeed nontrivial for the section listed in `AGENTS.md` (this document), and apply the correct theorem patches

## Deliverables
- (1) `.ipynb` containing all proofs
- (1) `plan.md` that has been appended to with new blockers/notable items/nontrival proofs that require manual verification from this session

## Notes
- No permissions given to explore outside of hw2/
- You will not have any need to reference any additional files in hw2/
- All code and experiments should be contained in one Jupyter notebook
- Your work will be verified with Claude