import Mathlib.Tactic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Algebra.Order.Field.Basic

open scoped RealInnerProductSpace
universe u
variable {E : Type u} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

-- SUBGRADIENT CHARACTERIZATION (convexity form)
def convex_function_first_order_inequality (f : E → ℝ) (g : E) (x : E) : Prop :=
  ∀ y : E, f y ≥ f x + ⟪g, y - x⟫

--  LIPSCHITZ / BOUNDEDHGRADIENT ASSUMPTION
def lipschitz_continuous_def (g : E) (L : ℝ) : Prop :=
  ‖g‖ ≤ L

-- PROJECTION STRUCTURE (nonexpansive map)
structure Projection (E : Type u) [PseudoMetricSpace E] where
  proj : E → E
  nonexpansive : LipschitzWith 1 proj

-- OGD UPDATE RULE
def ogd_update_rule_def (P : Projection E) (η : ℝ) (x g : E) : E :=
  P.proj (x - η • g)

-- FEASIBILITY CONDITION (optimal point fixed by projection)
def ogd_projection_step_feasibility (P : Projection E) (u : E) : Prop :=
  P.proj u = u

-- MAIN ONE-STEP DISTANCE PROGRESS LEMMA
lemma ogd_step_expansion_squared_distance (P : Projection E) (η : ℝ) (x g u : E)
    (hu : ogd_projection_step_feasibility P u) :
    dist (ogd_update_rule_def P η x g) u ^ 2
      ≤ dist x u ^ 2 - 2 * η * ⟪g, x - u⟫ + η ^ 2 * ‖g‖ ^ 2 := by
  -- Apply Nonexpansiveness
  have h_nonexp := P.nonexpansive.dist_le_mul (x - η • g) u
  -- Clean up projection and constant
  rw [hu] at h_nonexp
  replace h_nonexp : dist (ogd_update_rule_def P η x g) u ≤ dist (x - η • g) u := by
    simpa using h_nonexp
  -- Square both sides
  have h_sq : dist (ogd_update_rule_def P η x g) u ^ 2 ≤ dist (x - η • g) u ^ 2 := by
    gcongr
  -- Move from 'dist' to 'norm'
  rw [dist_eq_norm, dist_eq_norm] at h_sq ⊢
  -- Expand quadratic form
  refine h_sq.trans ?_
  rw [sub_right_comm, norm_sub_sq_real]
  -- Simplify algebra
  simp only [inner_smul_right, norm_smul, Real.norm_eq_abs]
  -- η² identity
  have h_eta_sq : (|η| * ‖g‖) ^ 2 = η ^ 2 * ‖g‖ ^ 2 := by
    rw [mul_pow, sq_abs]
  rw [h_eta_sq, real_inner_comm]
  ring_nf
  apply le_refl

-- PROJECTION NONEXPANSIVENESS STEP (auxiliary lemma)
lemma ogd_projection_nonexpansive_property (P : Projection E) (η : ℝ) (x g u : E) :
    dist (ogd_update_rule_def P η x g) (P.proj u) ≤ dist (x - η • g) u := by
  simpa [ogd_update_rule_def]
    using (P.nonexpansive.dist_le_mul (x - η • g) u)


-- CONVEXITY YIELDS STEPWISE REGRET UPPER BOUND
lemma step_regret_convexity_upper_bound (f : E → ℝ) (g x u : E)
    (hconv : convex_function_first_order_inequality f g x) :
    f x - f u ≤ ⟪g, x - u⟫ := by
  -- Apply convexity at u
  have h := hconv u
  -- Rearrange inequality
  have h' : f x - f u ≤ -⟪g, u - x⟫ := by linarith
  -- Use inner product properties to swap arguments
  have hx : ⟪g, x - u⟫ = -⟪g, u - x⟫ := by rw [← inner_neg_right, neg_sub]
  linarith [hx]

-- INNER PRODUCT CONTROLLED BY DISTANCE PROGRESS
lemma step_regret_inner_product_to_distance_relation (P : Projection E) (η : ℝ)
    (x g u : E) (hu : ogd_projection_step_feasibility P u) :
    2 * η * ⟪g, x - u⟫
      ≤ dist x u ^ 2 - dist (ogd_update_rule_def P η x g) u ^ 2 + η ^ 2 * ‖g‖ ^ 2 := by
  -- Invoke main squared distance expansion
  have h := ogd_step_expansion_squared_distance (P := P) (η := η) (x := x) (g := g) (u := u) hu
  -- Algebraically rearrange to bound inner product
  linarith

-- ONE-STEP REGRET DECOMPOSITION
lemma step_regret_decomposition_inequality (f : E → ℝ) (g x u : E)
    (hconv : convex_function_first_order_inequality f g x)
    (P : Projection E) (η : ℝ) (hu : ogd_projection_step_feasibility P u)
    (hη_pos : 0 < η) :
    f x - f u ≤ (dist x u ^ 2 - dist (ogd_update_rule_def P η x g) u ^ 2 + η ^ 2 * ‖g‖ ^ 2) / (2 * η) := by
  -- Bound objective difference via subgradient
  have h₁ : f x - f u ≤ ⟪g, x - u⟫ := step_regret_convexity_upper_bound f g x u hconv
  -- Bound subgradient via distance progress
  have h₂ : 2 * η * ⟪g, x - u⟫ ≤ dist x u ^ 2 - dist (ogd_update_rule_def P η x g) u ^ 2 + η ^ 2 * ‖g‖ ^ 2 :=
    step_regret_inner_product_to_distance_relation P η x g u hu
  -- Divide by 2η (valid since η > 0)
  have h₄ : ⟪g, x - u⟫ ≤ (dist x u ^ 2 - dist (ogd_update_rule_def P η x g) u ^ 2 + η ^ 2 * ‖g‖ ^ 2) / (2 * η) := by
    rw [le_div_iff₀ (by linarith)]
    linarith
  -- Combine bounds
  linarith

-- OPTIMAL STEP SIZE ALGEBRAIC IDENTITY
lemma ogd_regret_optimal_step_size_choice (D L T : ℝ) (hD : 0 < D) (hL : 0 < L) (hT : 0 < T) :
    let η := D / (L * Real.sqrt T)
    D^2 / (2 * η) + η * L^2 * T / 2 = D * L * Real.sqrt T := by
  intro η
  -- Simplify root properties
  have h_sqrt : (Real.sqrt T) * (Real.sqrt T) = T := Real.mul_self_sqrt (by positivity)
  have h_L2_T : L^2 * T = (L * Real.sqrt T)^2 := by
    calc L^2 * T
      _ = L^2 * ((Real.sqrt T) * (Real.sqrt T)) := by rw [h_sqrt]
      _ = L^2 * (Real.sqrt T)^2 := by ring
      _ = (L * Real.sqrt T)^2 := by ring
  -- Positivity and non-zero invariants
  have hx_pos : 0 < L * Real.sqrt T := by positivity
  have hD_ne : D ≠ 0 := ne_of_gt hD
  have hx_ne : L * Real.sqrt T ≠ 0 := ne_of_gt hx_pos
  -- First fraction reduction
  have H1 : D^2 / (2 * (D / (L * Real.sqrt T))) = D * (L * Real.sqrt T) / 2 := by
    rw [mul_div_assoc', div_div_eq_mul_div]
    have : D^2 * (L * Real.sqrt T) / (2 * D) = D * (D * (L * Real.sqrt T)) / (D * 2) := by ring
    rw [this, mul_div_mul_left _ _ hD_ne]
  -- Second fraction reduction
  have H2 : (D / (L * Real.sqrt T)) * (L^2 * T) / 2 = D * (L * Real.sqrt T) / 2 := by
    rw [h_L2_T]
    have : (D / (L * Real.sqrt T)) * (L * Real.sqrt T)^2 / 2 = D * (L * Real.sqrt T) * (L * Real.sqrt T) / (L * Real.sqrt T) / 2 := by ring
    rw [this, mul_div_cancel_right₀ _ hx_ne]
  -- Combine
  calc D^2 / (2 * (D / (L * Real.sqrt T))) + (D / (L * Real.sqrt T)) * L^2 * T / 2
    _ = D^2 / (2 * (D / (L * Real.sqrt T))) + (D / (L * Real.sqrt T)) * (L^2 * T) / 2 := by ring
    _ = D * (L * Real.sqrt T) / 2 + D * (L * Real.sqrt T) / 2 := by rw [H1, H2]
    _ = D * L * Real.sqrt T := by ring

omit [InnerProductSpace ℝ E] in
-- INDUCTIVE ACCUMULATION OVER ALL TIME STEPS
lemma ogd_regret_inductive_bound (T : ℕ) (f : ℕ → E → ℝ) (g x : ℕ → E) (u : E) (η : ℝ)
    (h_step : ∀ t, t < T → f t (x t) - f t u ≤ (dist (x t) u ^ 2 - dist (x (t + 1)) u ^ 2 + η ^ 2 * ‖g t‖ ^ 2) / (2 * η)) :
    (∑ t ∈ Finset.range T, (f t (x t) - f t u)) ≤ (dist (x 0) u ^ 2 - dist (x T) u ^ 2 + η ^ 2 * ∑ t ∈ Finset.range T, ‖g t‖ ^ 2) / (2 * η) := by
  induction T with
  | zero => simp
  | succ T ih =>
    -- Expand summation ranges for step T
    rw [Finset.sum_range_succ, Finset.sum_range_succ]
    -- Inductive hypothesis
    have h1 : (∑ t ∈ Finset.range T, (f t (x t) - f t u)) ≤ (dist (x 0) u ^ 2 - dist (x T) u ^ 2 + η ^ 2 * ∑ t ∈ Finset.range T, ‖g t‖ ^ 2) / (2 * η) := by
      apply ih
      intro t ht
      apply h_step t
      linarith
    -- Regret for step T via h_step parameter
    have h2 : f T (x T) - f T u ≤ (dist (x T) u ^ 2 - dist (x (T + 1)) u ^ 2 + η ^ 2 * ‖g T‖ ^ 2) / (2 * η) := by
      apply h_step T
      linarith
    -- Combine inductive sum and final step
    have h3 : (∑ t ∈ Finset.range T, (f t (x t) - f t u)) + (f T (x T) - f T u) ≤
              (dist (x 0) u ^ 2 - dist (x T) u ^ 2 + η ^ 2 * ∑ t ∈ Finset.range T, ‖g t‖ ^ 2) / (2 * η) +
              (dist (x T) u ^ 2 - dist (x (T + 1)) u ^ 2 + η ^ 2 * ‖g T‖ ^ 2) / (2 * η) := add_le_add h1 h2
    -- Algebraically collapse telescoping elements (-dist(x_T) + dist(x_T) = 0)
    have h4 : (dist (x 0) u ^ 2 - dist (x T) u ^ 2 + η ^ 2 * ∑ t ∈ Finset.range T, ‖g t‖ ^ 2) / (2 * η) +
              (dist (x T) u ^ 2 - dist (x (T + 1)) u ^ 2 + η ^ 2 * ‖g T‖ ^ 2) / (2 * η) =
              (dist (x 0) u ^ 2 - dist (x (T + 1)) u ^ 2 + η ^ 2 * ((∑ t ∈ Finset.range T, ‖g t‖ ^ 2) + ‖g T‖ ^ 2)) / (2 * η) := by
      rw [←add_div]
      congr 1
      ring
    linarith

omit [InnerProductSpace ℝ E] in
-- FINAL REGRET BOUND THEOREM WITH OPTIMAL STEP SIZE
lemma ogd_regret_final_rate_theorem (T : ℕ) (f : ℕ → E → ℝ) (g x : ℕ → E) (u : E) (D L : ℝ)
    (hD : 0 < D) (hL : 0 < L) (hT : 0 < T)
    (h_dist : dist (x 0) u ≤ D)
    (h_lipschitz : ∀ t, t < T → ‖g t‖ ≤ L)
    (h_step : ∀ t, t < T → f t (x t) - f t u ≤ (dist (x t) u ^ 2 - dist (x (t + 1)) u ^ 2 + (D / (L * Real.sqrt T)) ^ 2 * ‖g t‖ ^ 2) / (2 * (D / (L * Real.sqrt T)))) :
    (∑ t ∈ Finset.range T, (f t (x t) - f t u)) ≤ D * L * Real.sqrt (T:ℝ) := by
  have hT_real : (0:ℝ) < T := by exact Nat.cast_pos.mpr hT
  set η := D / (L * Real.sqrt T)
  have h_eta_pos : 0 < η := by positivity

  -- Apply Inductive Accumulation
  have h_bound := ogd_regret_inductive_bound T f g x u η h_step

  -- Bound Subgradient Magnitudes (Lipschitz assumption over time T)
  have h_g_sum : (∑ t ∈ Finset.range T, ‖g t‖ ^ 2) ≤ (T:ℝ) * L ^ 2 := by
    calc (∑ t ∈ Finset.range T, ‖g t‖ ^ 2)
      _ ≤ ∑ t ∈ Finset.range T, L ^ 2 := by
        apply Finset.sum_le_sum
        intro t ht
        have h_t_lt : t < T := Finset.mem_range.mp ht
        have hl := h_lipschitz t h_t_lt
        gcongr
      _ = (T:ℝ) * L ^ 2 := by simp

  -- Initial Distance Condition (Domain size invariant D)
  have h_dist_sq : dist (x 0) u ^ 2 ≤ D ^ 2 := by
    have hD_pos : 0 ≤ D := by linarith
    gcongr

  -- Drop non-positive final trailing distance
  have h_dist_T_pos : 0 ≤ dist (x T) u ^ 2 := by positivity

  -- Combine parts to substitute maximum values in the inductive numerator bounds
  have h_num : dist (x 0) u ^ 2 - dist (x T) u ^ 2 + η ^ 2 * ∑ t ∈ Finset.range T, ‖g t‖ ^ 2 ≤ D ^ 2 + η ^ 2 * ((T:ℝ) * L ^ 2) := by
    have h_part1 : dist (x 0) u ^ 2 - dist (x T) u ^ 2 ≤ D ^ 2 := by linarith
    have h_part2 : η ^ 2 * ∑ t ∈ Finset.range T, ‖g t‖ ^ 2 ≤ η ^ 2 * ((T:ℝ) * L ^ 2) := by gcongr
    linarith

  have h_div : (dist (x 0) u ^ 2 - dist (x T) u ^ 2 + η ^ 2 * ∑ t ∈ Finset.range T, ‖g t‖ ^ 2) / (2 * η) ≤ (D ^ 2 + η ^ 2 * ((T:ℝ) * L ^ 2)) / (2 * η) := by
    gcongr

  -- Rearrange division fraction towards substitution of optimal step-size lemma
  have h_split : (D ^ 2 + η ^ 2 * ((T:ℝ) * L ^ 2)) / (2 * η) = D ^ 2 / (2 * η) + η * L ^ 2 * (T:ℝ) / 2 := by
    calc (D ^ 2 + η ^ 2 * ((T:ℝ) * L ^ 2)) / (2 * η)
      _ = D ^ 2 / (2 * η) + η ^ 2 * ((T:ℝ) * L ^ 2) / (2 * η) := by rw [add_div]
      _ = D ^ 2 / (2 * η) + η * L ^ 2 * (T:ℝ) / 2 := by
        congr 1
        have h_eta_ne : η ≠ 0 := ne_of_gt h_eta_pos
        calc η ^ 2 * ((T:ℝ) * L ^ 2) / (2 * η)
          _ = (η * η) * ((T:ℝ) * L ^ 2) / (η * 2) := by ring
          _ = η * (η * ((T:ℝ) * L ^ 2)) / (η * 2) := by ring
          _ = η * ((T:ℝ) * L ^ 2) / 2 := by rw [mul_div_mul_left _ _ h_eta_ne]
          _ = η * L ^ 2 * (T:ℝ) / 2 := by ring

  -- Apply Optimal Step Size identity
  have h_opt := ogd_regret_optimal_step_size_choice D L (T:ℝ) hD hL hT_real
  linarith
