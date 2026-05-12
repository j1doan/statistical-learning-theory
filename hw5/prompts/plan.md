
Planned Theorem/Reference Checklist for hw5

Part A.1 (statistical/sample complexity + brute-force runtime)
- VC dimension bound: VCdim(H_{d,k}) ≤ O(k log(e d / k)) for k ≤ d/2; VCdim(H_{d,k}) ≤ O(d) otherwise.
- Agnostic sample complexity: m = O((VCdim + log(1/δ))/ε²) for ERM with 0-1 loss.
- Structural risk minimization/validation: hold-out validation guarantees for model selection among hypothesis classes.
- Brute-force support enumeration: number of supports ≤ ∑_{i=0}^k (d choose i); linear feasibility over chosen support.

Part A.2 (set cover → agreement hardness)
- Set Cover decision hardness (NP-complete).
- Learner-to-agreement reduction theorem from Week 5 (hardness of agnostic proper learning from agreement hardness).
- Construction lemma: encoding set cover as sparse homogeneous linear classifier agreement with multiplicities.
- Sign convention: sign(0) = +1 (as per statement) for classifiers.

Part A.3 (experiment)
- No specific external theorems; empirical comparison guidelines.
- Runtime scaling comparison between exhaustive k-sparse 0-1 search and ℓ1-constrained surrogate (e.g., hinge/logistic).
- Validation/hold-out error comparison principles.

Part B.1 (hinge with ℓ1 constraint as LP)
- Linearization trick: w_j = w_j^+ − w_j^−, |w|_1 = ∑ (w_j^+ + w_j^-).
- Slack variables for hinge: ξ_i ≥ 0, constraints 1 − y_i⟨w, x_i⟩ ≤ ξ_i.
- LP feasibility/duality not required beyond standard form.

Part B.2 (surrogate comparator counterexample)
- Population hinge risk computation for two-point distribution.
- Relation between hinge minimizers and 0-1 risk; explicit minimizers for p ∈ (0, 1/2), M > (1−p)/p.

Part B.3 (fixed-feature parity barrier)
- Parity matrix H with rows indexed by I ⊆ [d], columns by x ∈ {−1, +1}^d, entries χ_I(x).
- Orthogonality/rank: rows of H are orthogonal ⇒ rank(H) = 2^d.
- Factorization lemma: H = W Φ where Φ encodes feature map; rank bound forces D ≥ 2^d.
- Matching upper bound: feature map φ(x) = (χ_I(x))_{I⊆[d]} represents all parities.

Part B.4 (same predictors, different optimization geometry)
- Linear predictors equality: f_β(x) = ⟨β, x⟩ equals two-layer linear net f_{u,v}(x) = v⟨u, x⟩ via factorization β = v u.
- Convexity of L_lin (quadratic in β).
- Nonconvexity example for L_net via Jensen violation on a concrete S.
- Global minima correspondence: any factorization of β* gives global minimizer of L_net.

Open: Need to place proofs in corresponding pa5.ipynb markdown cells; no theorems currently blocked.

Update 2026-05-10: Draft solutions and experiment scaffold inserted into pa5.ipynb (all parts A.1–A.3, B.1–B.4). No additional blockers identified yet. Pending: run/validate code cells and finalize formatting if needed.
