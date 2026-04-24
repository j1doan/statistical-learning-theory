# AGENTS.md: Formal Verification Professor

## Task (Part A)
In lecture we proved the following i.i.d. growth-function ERM guarantee. Let ̂ ℎ ∈ argmin_{ℎ ∈ ℋ︀} 𝐿_𝑛(ℎ). Then with high probability over 𝑆∼𝒟︀^𝑛, we have $$L_D(\hat{h}) \le \inf_{h \in \mathcal{H}} L_D(h)+ O\!\left(\frac{\log \Gamma_{\mathcal{H}}(2n) + \log\!\left(\frac{1}{\delta}\right)}{n}\right)$$.
The learning-theoretic structure of the proof was covered in lecture, but several concentration inequalities were used without proof. The inequalities to learn in this mini-course are:
- Hoeffding’s inequality
- Hoeffding’s inequality for sampling without replacement
- McDiarmid’s inequality
- Bernstein’s inequality (an additional result worth knowing).
---
Goal. Create a short mini-course that teaches you these four concentration inequalities well enough to complete the new ERM proof end-to-end. The mini-course should be a single coherent document, written so that someone unfamiliar with the material could learn from it. Organize it in roughly the following order:
1. The concept of concentration. Explain what concentration inequalities are as a class of statements: what kind of random quantity they describe, what it means for such a quantity to concentrate, and why we should expect this phenomenon for sums and well-behaved functions of many independent random variables. Use at least one concrete example to ground the discussion. What is the intuition behind concentration inequalities?
2. The common technique. Present the moment-generating-function method that underlies the proofs of Hoeffding and Bernstein, including the Chernoff bound as a general template. Explain why bounding the MGF translates into a tail bound and what one needs to control about the MGF to obtain a useful bound. McDiarmid’s inequality uses the bounded- differences / martingale variant of the same idea; introduce that variant here or in the proofs section, wherever it reads more naturally.
3. Statements, assumptions, and consequences. For each of the four inequalities, give a precise statement, state the assumptions under which it holds, and explain what kind of random quantity it controls and how strong the resulting tail bound is. Compare the four concentration inequalities. In particular, make clear what additional structure Bernstein exploits beyond Hoeffding, and what changes when sampling is without replacement.
4. Proofs. Derive each of the four inequalities. Use the MGF method developed in the previous section wherever it applies, and the bounded-differences variant for McDiarmid. Is there a common template that can unify the proofs?
5. Connection to the Week 3 ERM proof. Combine the previous results to give a full proof of the i.i.d. ERM guarantee stated above.
**Reference.** Provide detailed references for all results you used, and make sure everything can be checked against these references.
**Format.** Submit one coherent write-up. Tables, diagrams, and proof-dependency maps are welcome where they help.

## Task (Part B)
This lecture proved the growth-function ERM guarantee displayed in Part A and, via Sauer-Shelah, the VC corollary, $$L_D(\hat{h}) \le \inf_{h \in \mathcal{H}} L_D(h)+ O\!\left(\sqrt{\frac{d \log\!\left(\frac{2en}{d}\right) + \log\!\left(\frac{1}{\delta}\right)}{n}}\right)$$ where 𝑑 = VCdim(ℋ︀). This establishes one direction of the Fundamental Theorem of PAC learning: if VCdim(ℋ︀) < ∞, then ℋ︀ is PAC learnable. The sample complexity this yields
matches the Fundamental Theorem’s tight bound up to a logarithmic factor. The converse direction, that VCdim(ℋ︀) = ∞ implies ℋ︀ is not PAC learnable, was stated in lecture but not proved. The standard route to this lower bound is the No-Free-Lunch theorem.
```
Theorem. No-Free-Lunch (Updated)
Let 𝐴 be any learning algorithm for binary classification with the 0-1 loss over a domain 𝒳︀, and let 𝑛 be any integer with 𝑛 < |𝒳︀|/2. Then there exists a distribution 𝒟︀ over 𝒳︀ × {0, 1} such that (i) some function 𝑓∗ :𝒳︀ → {0, 1} satisfies 𝐿_𝒟︀ (𝑓∗) = 0, and (ii) with probability at least 1/7 over 𝑆∼𝒟︀^𝑛, the learner’s output satisfies 𝐿_𝒟︀ (𝐴(𝑆)) ≥ 1/8.
```
---
Goal: In this part you will prove NFL, use it to close the lower-bound direction, and demonstrate the construction concretely on objects you choose yourself. Also, you will compare the original and updated versions of NFL. Complete the following tasks:
1. Proof. Prove the NFL theorem above. Before writing the proof, study the statement carefully and identify which objects are universally quantified and which are chosen by the adversary. The standard proof uses an averaging argument over the labelings of a 2𝑛-point subset of 𝒳︀, followed by the probabilistic method to extract a single bad labeling.
2. Application: closing the Fundamental Theorem. State the corollary that NFL implies the lower-bound direction of the Fundamental Theorem for PAC learning. Then make the application concrete: choose a hypothesis class with infinite VC dimension, prove that its VC dimension is indeed infinite, and apply the corollary explicitly to that class.
3. Worked construction. The NFL proof guarantees the existence of a bad distribution but does not exhibit one. Provide a concrete example of a learning rule and a domain, and explicitly construct a bad distribution and target labeling for which the rule fails with at least constant probability. Verify the failure by calculation.
4. Comparison to the original No-Free-Lunch theorem. In the first lecture we proved a different version of NFL: for any finite domain 𝒳︀ and any deterministic learner 𝐴, there exist a function 𝑓 :𝒳︀ → {0, 1} and an enumeration 𝑥1, …, 𝑥𝑛 of 𝒳︀ (𝑛 = |𝒳︀|) such that 𝐴 makes 𝑛 mistakes on the sequence (𝑥_𝑡, 𝑓(𝑥_𝑡))_{𝑡=1}^{n}. Compare the original and updated versions. At minimum, identify the learning setting each one lives in, the kind of adversary each one allows (in particular, whether the adversary is adaptive or oblivious), and the form of the conclusion (deterministic vs probabilistic, number of mistakes vs population loss). Explain what each version is telling us and why both are called “No-Free-Lunch” despite being quantitatively very different statements.

## Constraints
- Complete parts A and B
- - **Jupyter Notebook JSON Structure**: When editing `.ipynb` files directly, special care must be taken with JSON escaping (e.g., `\\` for LaTeX backslashes) to avoid corrupting the notebook format
- You will only append to `pa3.ipynb` using a markdown environment for your proofs
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
- Note all your theorems in `plan.md`

## Deliverables
- (1) `.ipynb` containing all proofs
- (1) `plan.md` that has been appended to with new blockers/notable items/nontrival proofs that require manual verification from this session

## Notes
- No permissions given to explore outside of hw3/
- You will not have any need to reference any additional files in hw3/
- All code and experiments should be contained in one Jupyter notebook
- Your work will be verified with Claude