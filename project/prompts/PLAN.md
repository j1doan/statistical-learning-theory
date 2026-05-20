# PLAN.md

This file outlines the comprehensive roadmap, dependency tracking, and implementation plan for formalizing **Online Convex Optimization (OCO)** in **Lean 4** using **mathlib**. It serves as the source of truth for current progress, active blockers, and upcoming milestones.

Our objective is to systematically formalize OCO theory from core geometric definitions to asymptotic regret bounds across two major algorithms: Online Gradient Descent (OGD) and Follow-the-Regularized-Leader (FTRL).

* **Convexity & Geometry Foundations (Sections 1 & 2):** Formalizing first-order characterizations of convexity, Lipschitz continuity, and OGD projection/distance-tracking mechanics.
* **Single-Step Regret Dynamics (Section 3):** Establishing algebraic decompositions, distance-progress lemmas, and upper bounds for isolated time steps.
* **Full Regret Decomposition & Inductive Accumulation (Section 4):** Transitioning from single-step bounds to multi-step regret aggregation using telescoping lemmas and inductive proofs.
* **Asymptotic Regret Bounds & Extensions (Sections 5 & 6):**
  * Optimizing step-size selection to prove the final $O(\sqrt{T})$ regret rate for convex Lipschitz losses.
  * Extending the framework to **Follow-the-Regularized-Leader (FTRL)** and proving $O(\log T)$ regret bounds for strongly convex losses.

## Lean 4 Online Gradient Descent Formalization

### 1. Convexity + Lipschitz foundations
- ✓ `convex_def_inner_product_characterization`
- ✓ `lipschitz_continuous_def`
- ✓ `convex_lipschitz_implies_subgradient_bound`
- ✓ `convex_function_first_order_inequality`

### 2. OGD update rule
- ✓ `ogd_update_rule_def`
- ✓ `ogd_projection_step_feasibility`
- ✓ `ogd_projection_nonexpansive_property`
- ✓ `ogd_step_expansion_squared_distance`

### 3. Single-step regret analysis
- X `step_regret_decomposition_inequality`
- X `step_regret_convexity_upper_bound`
- X `step_regret_inner_product_to_distance_relation`
- X `step_ogd_distance_progress_lemma`
- X `dist_ogdStep_le`

### 4. Full regret decomposition
- TODO `regret_decomposition_telescoping_lemma`
- TODO `regret_sum_stepwise_bound`
- TODO `regret_bound_by_initial_distance_and_gradient`
- TODO `ogd_regret_general_bound`

### 5. $O(\sqrt{T})$ regret
- TODO `ogd_regret_sqrt_time_bound`
- TODO `ogd_regret_optimal_step_size_choice`
- TODO `ogd_regret_final_rate_theorem`

### 6. Strongly convex extension
- TODO `strongly_convex_function_def`
- TODO `strongly_convex_implies_quadratic_growth`
- TODO `ogd_linear_convergence_step_lemma`
- TODO `strongly_convex_ogd_regret_log_bound`

## Completion Condition

The project is complete only when:

- All listed lemmas are implemented
- All proofs compile without `sorry`
- Final regret theorems are proven:
  - $O(\sqrt{T})$ regret (convex Lipschitz case)
  - $O(\log T)$ regret (strongly convex case)

# Lessons Learned
- Used `div_div_eq_mul_div` and explicit field simplifications (`mul_div_mul_left`, `mul_div_cancel_right₀`) to handle complex real division manipulations within `ring`.
- Avoided `Finset.sum` telescoping rules by providing an explicit inductive proof on `T` for regret accumulation, resolving the step regret bound gracefully with `add_le_add` and `linarith`.