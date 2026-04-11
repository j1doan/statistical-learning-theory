# AGENTS.md: ML Specialist

## Role & Objective
You are an expert in machine learning methods. Your goal is to complete the tasks below in a modern Jupyter notebook.

## Task
Complete the following objectives:
---
Let X = [0, 1], Y = {−1, +1}, and let hθ(x) = sign(x − θ),
where we use the convention sign(z) = +1 for z ≥ 0 and sign(z) = −1 for z < 0.
We will study sequences with one extra structural assumption beyond what was explicitly
analyzed in lecture.
∆-Separated Threshold-Realizable Sequences. We say a sequence ((xt, yt))T
t=1 is ∆-separated threshold-realizable if there exist θ∗ ∈ [0, 1] and ∆ > 0 such that
yt = hθ∗ (xt) and |xt − θ∗| ≥ ∆ for every round t.
---
1. From continuous thresholds to a finite class.
Design a finite grid G ⊆ [0, 1] whose size depends only on ∆, and consider the associated
finite threshold class
HG = {hθ : θ ∈ G}.
Prove that for every ∆-separated threshold-realizable sequence, there exists some ˜θ ∈ G such
that h˜θ(xt) = yt for all t = 1, . . . , T.
Then use the Halving theorem from lecture to derive a mistake bound of order
O(log(1/∆)) for an explicit online learner.
Your answer should clearly state:
• your choice of grid G,
• the size of G as a function of ∆,
• the resulting mistake bound.
---
2. A positive margin from separation.
View thresholds as linear predictors by choosing a feature map
ϕ : [0, 1] → Rd
and a unit vector u∗ depending on θ∗.
Prove that every ∆-separated threshold-realizable sequence is linearly separable with margin
at least c∆ for some absolute constant c > 0 under your representation, while
∥ϕ(x)∥ ≤ R for all x ∈ [0, 1] for some absolute constant R.
Then use the Perceptron theorem from lecture to derive an explicit mistake bound of order
O(1/∆2).
Your answer should clearly specify your chosen feature map, the margin lower bound, the
norm bound, and the final mistake bound.
---
3. Comparison and interpretation.
Explain why the continuous-threshold impossibility phenomenon does not contradict Part 1.
Then compare the two mistake bounds you obtained in Parts 1 and 2. Why do they scale
differently with ∆? What is each argument measuring about the problem?
---
4. Optional strengthening: audit an AI proof.
An AI assistant gives the following argument:
Because every example is at least ∆ away from the true threshold, continuous
thresholds effectively form a class of size O(1/∆). Therefore any online learner, in-
cluding Perceptron, must make at most O(log(1/∆)) mistakes on every ∆-separated
threshold-realizable sequence.
Identify at least two mathematical problems with this argument. Then write a corrected
statement that is true and prove it.

## Additional Tasks
- You will only append to the notebook using a markdown environment for your proofs
- Look for the cell containing `# Part B: Theory Problem`, below it are (4) cells labeled with their corresponding questions; construct your proofs in these cells only
- DO NOT READ `# Part A: Repository Setup` OR `# Part C: Perceptron — Implementation and Experiments`, these are not relevent to the current scope of GEMINI.md
- Do not delete code or markdown cells; only a human can delete cells
- There is no need to write code
- There is no need to look at the `.png` outputs
- `build_notebook.py` was used to generate the inital notebook as your task is to only generate proofs using markdown and latex; there is no need for you to look at this file

## Notes
- No permissions given to explore outside of hw1/
- You will not have any need to reference any additional files in hw1/
- All code and experiments should be contained in one Jupyter notebook
- Your work will be verified with Claude