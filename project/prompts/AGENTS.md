# AGENTS.md

## Project Overview

This repository formalizes the core theoretical guarantees of **Online Convex Optimization (OCO)** in **Lean 4** using **mathlib**, focusing specifically on the **Online Gradient Descent (OGD)** algorithm.

We formalize:

* **Convexity & Geometry Foundations:** First-order characterizations of convexity and OGD distance-tracking mechanics.
* **Single-Step Regret Dynamics:** Upper bounds and algebraic decompositions of single-step regret.
* **Inductive Regret Accumulation:** Full inductive aggregation of multi-step regret (replacing manual telescoping sums) to establish the optimal step size and the final $O(\sqrt{T})$ regret bound for convex, Lipschitz-continuous losses.

## Important Files

- `AGENTS.md` contains the scope of the project
- `PLANS.md` is a TODO list, a place where current lean proofs are failing, read `AGENTS.md` before `PLANS.md` for reasons outlined below
  - ✓ = marks completed lemmas verified by lean compiler
  - X = marks imcomplete lemmas with incomplete goals, noted in `PLANS.md`
  - TODO - notes lemmas not yet implemented
- `MyProject/Basic.lean` is a stable state of the project; under no circumstance are read/write permissions given to this file
- `MyProject/Workspace.lean` is a unstable state; construct additional lean proofs here as noted in ## Lean 4 Online Gradient Descent Formalization
- `MyProject/Extended.lean` is unstable; no read/write permissions given to this file

## Mathematical Conventions

- Objective:
$$
\min_{x_t \in \mathcal{K}} \sum_{t=1}^T f_t(x_t)
$$

- Regret:
$$
\text{Regret}_T =
\sum_{t=1}^T f_t(x_t)
- \min_{x \in \mathcal{K}} \sum_{t=1}^T f_t(x)
$$

- OGD update:
$$
x_{t+1} = \Pi_{\mathcal{K}}(x_t - \eta_t \nabla f_t(x_t))
$$

## mathlib Usage Policy

- Always search mathlib before proving:
  - convexity lemmas
  - norm inequalities
  - summation/telescoping results
- Prefer:
  - `Finset.sum`
  - `InnerProductSpace`
  - `Convex` API
  - projection lemmas from mathlib

## Formal Constraints
- **No Hallucinations:** If a proof goal is unresolvable with the current context, state "Incomplete Context" rather than inventing a proof step.
- **Strict Logic:** Maintain $P \implies Q$ rigor. Do not skip steps unless explicitly using a "Search" or "Auto" tactic.

## Dependency Rules

- Lemmas may only depend on:
  - previously completed lemmas, or
  - mathlib theorems
- Do **not** assume results not yet proven in this project
- Do not implement Step N+1 before Step N is complete

## KV Cache Optimization & Context Management

To minimize latency and token consumption, adhere to the following persistence guidelines:

- **Reference, Don't Redundantize:** Never re-state a definition, lemma, or state machine specification if it was provided earlier in the session. Refer to it by its unique identifier (e.g., "Referencing Lemma 4.2").
- **Differential Updates:** When modifying a proof script or spec, only output the changed lines. Use a `PATCH` format rather than rewriting the entire file.
- **Implicit State Maintenance:** Assume all mathematical invariants and environmental assumptions from the initial prompt remain in the KV cache. Do not re-verify them unless a contradiction is detected.
- **Memoization of Tactic Sequences:** If a specific sequence of tactics (e.g., `intros; simpl; induction n; auto.`) successfully discharged a goal, cache that sequence and reuse the term "Standard Induction Strategy" for future similar subgoals.

## Agent Behavior Rules

- Do not invent mathematical facts
- Do not skip intermediate reasoning steps
- If stuck:
  - simplify the goal
  - introduce helper lemmas
  - search mathlib
- Prefer correctness over conciseness
- Maintain strict alignment with lemma dependency order
- Keep lemmas small and modular
- Lemmas marked with a ✓ are complete, build upon these lemmas which are not marked with ✓
- Avoid duplication of mathlib results
- Ensure naming is descriptive and consistent
- Update `PLANS.md` only when:
  - adding/removing lemmas
  - changing proof strategy
- When a theorem or lemma is complete, pause for user to manually run lake build
- Feedback will be given based on success or error of Lean InfoView

## Lean 4 Online Gradient Descent Formalization

### 1. Convexity + Lipschitz Foundations
- ✓ `convex_function_first_order_inequality`
- ✓ `ogd_update_rule_def`
- ✓ `ogd_step_expansion_squared_distance`

### 2. Single-Step Regret Analysis
- ✓ `step_regret_convexity_upper_bound`
- ✓ `step_regret_decomposition_inequality`

### 3. Inductive Regret Accumulation & $O(\sqrt{T})$ Rate
- ✓ `ogd_regret_optimal_step_size_choice`
- ✓ `ogd_regret_final_rate_theorem`

### Proof Strategy Rules

- Use `calc` blocks for inequality chains
- Use `have` for intermediate results
- Break proofs into small lemmas whenever possible
- Prefer structure over brevity

## Verification Workflow

### Specification & Modeling
- Prioritize structural clarity and mathlib-compatible definitions.
- Keep definitions and structures minimal, providing only the necessary fields and properties required for the OGD proofs.

### Proof Engineering
- **Lemma Breakdown:** Decompose complex proofs into small, reusable auxiliary lemmas. This allows the compiler to check individual steps efficiently and minimizes long-running tactic states.
- **Failure Analysis:** When a proof script fails, isolate the exact step or missing mathlib lemma (e.g., missing linearity or inner product properties) instead of rewriting the entire proof from scratch.

### Tool Interactions
| Tool | Instruction |
| :--- | :--- |
| **Lean 4 Compiler / Lake** | Use precise tactic blocks (`have`, `calc`, or explicit term-mode proofs). Ensure exact namespaces from `Mathlib` are opened or referenced. |

## Global Execution Rules

- All code must compile in Lean 4 with **no `sorry` or `admit`**
- Do not introduce undefined placeholders
- Every lemma must be fully proven before it is used downstream
- Do not skip steps in proofs
- Prefer mathlib results over re-proving known facts
- Use modular lemmas (small, reusable components)

## Completion Condition

The project is complete only when:

- All listed lemmas are implemented
- All proofs compile without `sorry` or `admit`