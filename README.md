# Online Regret Bounds in Lean 4

This repository contains a formalization of the $O(\sqrt{T})$ regret bound for Online Gradient Descent (OGD) in [Lean 4](https://lean-lang.org/).

## Overview

The formalization demonstrates that the cumulative regret of an online learner, which selects iterates from a convex set $\mathcal{K}$ and suffers losses from an arbitrary sequence of convex, Lipschitz functions $f_t$, can be bounded by $O(\sqrt{T})$.

## Theoretical Foundation

The proof is structured around the geometric properties of OGD updates:

1.  **Convexity:** First-order characterization via subgradients.
2.  **Lipschitz Continuity:** Boundedness of subgradient norms.
3.  **Projection:** Non-expansiveness of projection onto convex sets.
4.  **Squared Distance Expansion:** Relating the change in distance to the comparator to alignment (inner product) and noise (step-size penalty).
5.  **Inductive Accumulation:** Telescoping distance terms over $T$ time steps to derive the final bound.

## Formalization Structure

The core formalization is located in `MyProject/Basic.lean`. It includes:

*   **Definitions:** Convexity, Lipschitz continuity, Projection, and the OGD update rule.
*   **Lemmas:**
    *   Squared distance expansion.
    *   Projection non-expansiveness.
    *   Step-wise regret bound (convexity upper bound).
    *   Regret decomposition (linking distance progress and inner product).
    *   Optimal step-size balancing.
*   **Theorem:** `ogd_regret_final_rate_theorem` establishing the $O(\sqrt{T})$ rate.

## Toolchain

This project uses the following Lean toolchain:
```
leanprover/lean4:v4.30.0-rc2
```

## Building

To build the project, ensure you have a functional Lean 4 installation and use `lake`:

```bash
lake build
```

---

*Based on the theory documented in `project/assets/regret.htm`.*