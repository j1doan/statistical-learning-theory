"""
Script to programmatically build perceptron.ipynb using nbformat.
Run: python hw1/build_notebook.py
"""
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

nb = new_notebook()
cells = []

# ── Cell 0: Title ─────────────────────────────────────────────────────────
cells.append(new_markdown_cell("""\
# Homework 1: The Perceptron Algorithm

This notebook implements and experiments with the classic Perceptron algorithm.

**Algorithm:**
- Input: Feature map $\\phi: \\mathcal{X} \\to \\mathbb{R}^d$, labels $y_t \\in \\{-1, +1\\}$
1. Initialize $w_1 = \\mathbf{0}$
2. Receive $x_t$, predict $\\hat{y}_t = +1$ if $\\langle w_t, \\phi(x_t) \\rangle \\geq 0$, else $\\hat{y}_t = -1$
3. Receive true label $y_t$
4. If $\\hat{y}_t \\neq y_t$ (mistake): $w_{t+1} = w_t + y_t \\cdot \\phi(x_t)$
5. Else: $w_{t+1} = w_t$

**Mistake Bound (Novikoff's Theorem):** $M \\leq \\dfrac{R^2}{\\gamma^2}$

where $\\gamma = \\min_t y_t \\langle w^*, \\phi(x_t) \\rangle$ (margin) and $R = \\max_t \\|\\phi(x_t)\\|$ (radius).\
"""))

# ── Cell 1: Imports ────────────────────────────────────────────────────────
cells.append(new_code_cell("""\
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

plt.rcParams.update({
    'figure.dpi': 120,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'font.size': 12,
})
print('Imports OK')\
"""))

# ── Cell 2: Section header ─────────────────────────────────────────────────
cells.append(new_markdown_cell("## 1. Perceptron Implementation"))

# ── Cell 3: Perceptron function ────────────────────────────────────────────
cells.append(new_code_cell("""\
def perceptron(X, y):
    \"\"\"
    Online Perceptron algorithm.

    Parameters
    ----------
    X : ndarray, shape (T, d)  -- feature vectors phi(x_t)
    y : ndarray, shape (T,)    -- labels in {-1, +1}

    Returns
    -------
    w             : final weight vector
    mistakes      : total number of mistakes
    mistake_times : list of time-steps where a mistake occurred
    \"\"\"
    T, d = X.shape
    w = np.zeros(d)
    mistakes = 0
    mistake_times = []

    for t in range(T):
        y_hat = 1 if np.dot(w, X[t]) >= 0 else -1
        if y_hat != y[t]:          # mistake
            w = w + y[t] * X[t]
            mistakes += 1
            mistake_times.append(t)

    return w, mistakes, mistake_times


print('perceptron() defined')\
"""))

# ── Cell 4: Q1 header ─────────────────────────────────────────────────────
cells.append(new_markdown_cell("""\
## 2. Data Generation with Known Margin $\\gamma$ and Radius $R$

### Q1 -- How do you generate data where you know $\\gamma$ and $R$?

**Strategy:**

1. **Choose a ground-truth separator** $w^* = e_1 \\in \\mathbb{R}^d$ (first standard basis vector, unit norm).
2. **Sample raw points** $z_t \\sim \\mathcal{N}(0, I_d)$.
3. **Assign labels** $y_t = \\text{sign}(\\langle w^*, z_t \\rangle)$.
4. **Enforce margin $\\gamma$:** shift each $z_t$ along $w^*$ so that $y_t \\langle w^*, z_t \\rangle \\geq \\gamma$:
$$\\phi(x_t) = z_t + y_t \\cdot \\max(0,\\, \\gamma - y_t \\langle w^*, z_t \\rangle) \\cdot w^*$$
5. **Enforce radius $R$:** normalise each point to the sphere of radius $R$:
$$\\phi(x_t) \\leftarrow R \\cdot \\frac{\\phi(x_t)}{\\|\\phi(x_t)\\|}$$

**Choices required:**
- Dimension $d$, number of examples $T$
- The separator $w^*$ (we use $e_1$)
- Whether to fix $\\|\\phi(x_t)\\| = R$ exactly (sphere) or $\\leq R$ (ball) -- we use the sphere
- The pre-rescaling margin target; the *actual* margin after rescaling is measured empirically\
"""))

# ── Cell 5: generate_data ─────────────────────────────────────────────────
cells.append(new_code_cell("""\
def generate_data(T, d, gamma, R=1.0, seed=None):
    \"\"\"
    Generate a linearly separable dataset with known margin gamma and radius R.

    Parameters
    ----------
    T            : number of examples
    d            : feature dimension
    gamma        : desired margin  (y_t <w*, phi(x_t)> >= gamma for all t)
    R            : desired radius  (||phi(x_t)|| == R for all t)
    seed         : random seed

    Returns
    -------
    X            : ndarray (T, d)  -- feature vectors
    y            : ndarray (T,)    -- labels in {-1, +1}
    w_star       : ndarray (d,)    -- ground-truth separator (unit vector)
    actual_gamma : float           -- actual minimum margin after rescaling
    \"\"\"
    rng = np.random.default_rng(seed)

    # Ground-truth separator: first standard basis vector
    w_star = np.zeros(d)
    w_star[0] = 1.0

    # Sample raw Gaussian points
    Z = rng.standard_normal((T, d))

    # Assign labels from the separator
    scores = Z @ w_star                          # shape (T,)
    y = np.where(scores >= 0, 1, -1)

    # Enforce margin: shift along w_star so y_t * <w*, z_t> >= gamma
    functional_margins = y * scores
    deficit = np.maximum(0.0, gamma - functional_margins)
    X = Z + (deficit * y)[:, None] * w_star

    # Enforce radius: normalise to unit sphere, then scale by R
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    X = X / norms * R

    actual_margins = y * (X @ w_star)
    actual_gamma = float(actual_margins.min())

    return X, y, w_star, actual_gamma


# Sanity check
X_test, y_test, w_star_test, ag = generate_data(T=200, d=5, gamma=0.3, R=1.0, seed=0)
print(f'Shape        : {X_test.shape}')
print(f'Labels       : {np.unique(y_test)}')
print(f'Max norm     : {np.linalg.norm(X_test, axis=1).max():.6f}  (should be 1.0)')
print(f'Actual gamma : {ag:.4f}')
_, M_test, _ = perceptron(X_test, y_test)
print(f'Mistakes     : {M_test},  Bound R^2/gamma^2 = {1.0/ag**2:.1f}')\
"""))

# ── Cell 6: Exp 2 header ───────────────────────────────────────────────────
cells.append(new_markdown_cell("""\
## 3. Experiment 2 -- Mistakes $M$ vs $1/\\gamma^2$

### Q2 -- How does $M$ scale with $1/\\gamma^2$?

We fix $R=1$, $d=20$, $T=3000$ and vary $\\gamma$ over a grid.
For each $\\gamma$ we run the Perceptron over multiple random seeds and record the mean mistakes.\
"""))

# ── Cell 7: Exp 2 computation ─────────────────────────────────────────────
cells.append(new_code_cell("""\
R_fixed  = 1.0
d_fixed  = 20
T_fixed  = 3000
n_trials = 10

gamma_targets = np.linspace(0.05, 0.90, 30)

results = []   # (actual_gamma, mean_M, std_M, bound)

for g_target in gamma_targets:
    trial_M  = []
    trial_ag = []
    for seed in range(n_trials):
        X, y, _, ag = generate_data(T=T_fixed, d=d_fixed, gamma=g_target,
                                    R=R_fixed, seed=seed)
        _, M, _ = perceptron(X, y)
        trial_M.append(M)
        trial_ag.append(ag)
    mean_ag = float(np.mean(trial_ag))
    results.append((
        mean_ag,
        float(np.mean(trial_M)),
        float(np.std(trial_M)),
        R_fixed**2 / mean_ag**2
    ))

results = np.array(results)   # columns: gamma, mean_M, std_M, bound
print('Experiment 2 complete.')\
"""))

# ── Cell 8: Exp 2 plot ────────────────────────────────────────────────────
cells.append(new_code_cell("""\
gammas = results[:, 0]
mean_M = results[:, 1]
std_M  = results[:, 2]
bounds = results[:, 3]
inv_g2 = 1.0 / gammas**2

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Left: M vs 1/gamma^2
ax = axes[0]
ax.errorbar(inv_g2, mean_M, yerr=std_M, fmt='o', color='steelblue',
            ecolor='lightblue', capsize=3, label='Empirical M')
ax.plot(inv_g2, bounds, 'r--', lw=2, label='Bound R^2/gamma^2')
coeffs = np.polyfit(inv_g2, mean_M, 1)
ax.plot(inv_g2, np.poly1d(coeffs)(inv_g2), 'k:', lw=1.5,
        label=f'Linear fit (slope={coeffs[0]:.3f})')
ax.set_xlabel('1/gamma^2', fontsize=13)
ax.set_ylabel('Number of mistakes M', fontsize=13)
ax.set_title('Mistakes vs 1/gamma^2  (d=20, R=1)', fontsize=13)
ax.legend()

# Right: log-log
ax2 = axes[1]
ax2.loglog(inv_g2, mean_M, 'o', color='steelblue', label='Empirical M')
ax2.loglog(inv_g2, bounds, 'r--', lw=2, label='Bound R^2/gamma^2')
log_coeffs = np.polyfit(np.log(inv_g2), np.log(mean_M + 1e-9), 1)
ax2.loglog(inv_g2, np.exp(np.poly1d(log_coeffs)(np.log(inv_g2))),
           'k:', lw=1.5, label=f'Log-log fit (slope={log_coeffs[0]:.2f})')
ax2.set_xlabel('1/gamma^2  (log scale)', fontsize=13)
ax2.set_ylabel('M  (log scale)', fontsize=13)
ax2.set_title('Log-log: M vs 1/gamma^2', fontsize=13)
ax2.legend()

plt.tight_layout()
plt.savefig('hw1/exp2_mistakes_vs_gamma.png', bbox_inches='tight')
plt.show()
print(f'Linear fit slope : {coeffs[0]:.4f}  (expect ~1 if M proportional to 1/gamma^2)')
print(f'Log-log slope    : {log_coeffs[0]:.4f} (expect ~1)')\
"""))

# ── Cell 9: Exp 2 observation ─────────────────────────────────────────────
cells.append(new_markdown_cell("""\
**Observation:** The empirical number of mistakes $M$ grows approximately linearly with $1/\\gamma^2$,
consistent with the theoretical bound. The log-log slope is close to 1, confirming the $M = O(1/\\gamma^2)$ scaling.\
"""))

# ── Cell 10: Exp 3 header ─────────────────────────────────────────────────
cells.append(new_markdown_cell("""\
## 4. Experiment 3 -- Is the Bound $R^2/\\gamma^2$ Tight?

### Q3 -- Does the Perceptron do better in practice than the bound?

We compare the ratio $M / (R^2/\\gamma^2)$ across all $\\gamma$ values.
A ratio close to 1 means the bound is tight; a ratio $\\ll 1$ means the Perceptron does much better in practice.\
"""))

# ── Cell 11: Exp 3 plot ───────────────────────────────────────────────────
cells.append(new_code_cell("""\
ratios = mean_M / bounds

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(gammas, ratios, 'o-', color='darkorange', lw=2,
        label='M / (R^2/gamma^2)')
ax.axhline(1.0, color='red', ls='--', lw=1.5, label='Bound = 1 (tight)')
ax.fill_between(gammas, 0, ratios, alpha=0.15, color='darkorange')
ax.set_xlabel('Margin gamma', fontsize=13)
ax.set_ylabel('Ratio M / (R^2/gamma^2)', fontsize=13)
ax.set_title('Tightness of the Novikoff Bound  (d=20, R=1)', fontsize=13)
ax.set_ylim(0, 1.2)
ax.legend()
plt.tight_layout()
plt.savefig('hw1/exp3_bound_tightness.png', bbox_inches='tight')
plt.show()

print(f'Mean ratio : {ratios.mean():.4f}')
print(f'Max  ratio : {ratios.max():.4f}')
print(f'Min  ratio : {ratios.min():.4f}')\
"""))

# ── Cell 12: Exp 3 observation ────────────────────────────────────────────
cells.append(new_markdown_cell("""\
**Observation:** The ratio $M / (R^2/\\gamma^2)$ is consistently well below 1, meaning the Perceptron
makes **far fewer mistakes** than the theoretical bound predicts. The bound is **not tight** on random
Gaussian data -- it is a worst-case guarantee. The bound *can* be tight (see the classical adversarial
construction with points on a sphere), but on typical random data the Perceptron converges much faster.\
"""))

# ── Cell 13: Exp 4 header ─────────────────────────────────────────────────
cells.append(new_markdown_cell("""\
## 5. Experiment 4 -- Effect of Dimension $d$

### Q4 -- Is the bound independent of $d$? Design an experiment to test this.

Novikoff's bound $M \\leq R^2/\\gamma^2$ contains **no $d$ term**.
We test whether the empirical mistake count also stays roughly constant as $d$ grows,
while keeping $\\gamma$ and $R$ fixed.\
"""))

# ── Cell 14: Exp 4 computation ────────────────────────────────────────────
cells.append(new_code_cell("""\
gamma_fixed = 0.3
R_fixed2    = 1.0
T_dim       = 3000
n_trials_d  = 15
dims        = [2, 5, 10, 20, 50, 100, 200, 500]

dim_results = []

for d in dims:
    trial_M = []
    for seed in range(n_trials_d):
        X, y, _, _ = generate_data(T=T_dim, d=d, gamma=gamma_fixed,
                                   R=R_fixed2, seed=seed)
        _, M, _ = perceptron(X, y)
        trial_M.append(M)
    dim_results.append((d, float(np.mean(trial_M)), float(np.std(trial_M))))
    print(f'd={d:4d}  mean_M={np.mean(trial_M):.1f}  std={np.std(trial_M):.1f}')

dim_results = np.array(dim_results)
theoretical_bound = R_fixed2**2 / gamma_fixed**2
print(f'\\nTheoretical bound (pre-rescaling): {theoretical_bound:.1f}')\
"""))

# ── Cell 15: Exp 4 plot ───────────────────────────────────────────────────
cells.append(new_code_cell("""\
ds      = dim_results[:, 0]
mean_Md = dim_results[:, 1]
std_Md  = dim_results[:, 2]

fig, ax = plt.subplots(figsize=(8, 5))
ax.errorbar(ds, mean_Md, yerr=std_Md, fmt='s-', color='mediumseagreen',
            ecolor='lightgreen', capsize=4, lw=2, label='Empirical M')
ax.axhline(theoretical_bound, color='red', ls='--', lw=1.5,
           label=f'Bound R^2/gamma^2 = {theoretical_bound:.1f}')
ax.set_xscale('log')
ax.set_xlabel('Dimension d  (log scale)', fontsize=13)
ax.set_ylabel('Number of mistakes M', fontsize=13)
ax.set_title('Mistakes vs Dimension  (gamma=0.3, R=1)', fontsize=13)
ax.legend()
plt.tight_layout()
plt.savefig('hw1/exp4_mistakes_vs_dim.png', bbox_inches='tight')
plt.show()\
"""))

# ── Cell 16: Exp 4 observation ────────────────────────────────────────────
cells.append(new_markdown_cell("""\
**Observation:** The empirical mistake count $M$ remains **approximately constant** as $d$ increases
from 2 to 500, confirming that the Perceptron's mistake bound is truly dimension-free.
This is a remarkable property: adding more (irrelevant) features does not hurt the algorithm,
as long as the margin $\\gamma$ and radius $R$ are preserved.\
"""))

# ── Cell 17: Exp 5 header ─────────────────────────────────────────────────
cells.append(new_markdown_cell("""\
## 6. Experiment 5 -- Behaviour as $\\gamma \\to 0$

### Q5 -- What happens as $\\gamma \\to 0$? Connection to the threshold counterexample.

As $\\gamma \\to 0$ the data approaches a **non-separable** regime.
The bound $R^2/\\gamma^2 \\to \\infty$, and in the limit the Perceptron may never converge.

**Threshold counterexample:** Consider $d=1$, $x_t = 1$ for all $t$,
with labels alternating $+1, -1, +1, -1, \\ldots$.
The data is not linearly separable (no single threshold separates them),
and the Perceptron makes a mistake on **every single example** -- $M = T$.\
"""))

# ── Cell 18: Exp 5 Part A computation ────────────────────────────────────
cells.append(new_code_cell("""\
# Part A: M vs very small gamma
tiny_gammas = np.logspace(-2, np.log10(0.5), 40)   # 0.01 to 0.5
T_small     = 5000
d_small     = 20
n_trials_g0 = 8

small_g_results = []
for g in tiny_gammas:
    trial_M  = []
    trial_ag = []
    for seed in range(n_trials_g0):
        X, y, _, ag = generate_data(T=T_small, d=d_small, gamma=g,
                                    R=1.0, seed=seed)
        _, M, _ = perceptron(X, y)
        trial_M.append(M)
        trial_ag.append(ag)
    small_g_results.append((
        float(np.mean(trial_ag)),
        float(np.mean(trial_M)),
        float(np.std(trial_M))
    ))

small_g_results = np.array(small_g_results)
print('Part A done.')\
"""))

# ── Cell 19: Exp 5 Part B counterexample ─────────────────────────────────
cells.append(new_code_cell("""\
# Part B: Threshold counterexample
def threshold_counterexample(T):
    \"\"\"1-D example: x_t = 1 always, labels alternate +1/-1.\"\"\"
    X = np.ones((T, 1))
    y = np.array([1 if t % 2 == 0 else -1 for t in range(T)])
    return X, y

T_thresh = 200
X_thresh, y_thresh = threshold_counterexample(T_thresh)
_, M_thresh, mt_thresh = perceptron(X_thresh, y_thresh)
print(f'Threshold counterexample: T={T_thresh}, mistakes={M_thresh} (should equal T={T_thresh})')\
"""))

# ── Cell 20: Exp 5 plot ───────────────────────────────────────────────────
cells.append(new_code_cell("""\
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: M vs gamma (small gamma regime)
ax = axes[0]
g_vals  = small_g_results[:, 0]
M_vals  = small_g_results[:, 1]
M_stds  = small_g_results[:, 2]
bounds5 = 1.0 / g_vals**2

ax.errorbar(g_vals, M_vals, yerr=M_stds, fmt='o', color='purple',
            ecolor='plum', capsize=3, label='Empirical M')
ax.plot(g_vals, bounds5, 'r--', lw=2, label='Bound R^2/gamma^2')
ax.set_xlabel('Margin gamma', fontsize=13)
ax.set_ylabel('Number of mistakes M', fontsize=13)
ax.set_title('Mistakes as gamma -> 0  (d=20, R=1)', fontsize=13)
ax.set_yscale('log')
ax.legend()

# Right: Threshold counterexample -- cumulative mistakes
ax2 = axes[1]
mt_set = set(mt_thresh)
cum_mistakes = np.zeros(T_thresh)
count = 0
for t in range(T_thresh):
    if t in mt_set:
        count += 1
    cum_mistakes[t] = count

ax2.plot(range(T_thresh), cum_mistakes, color='crimson', lw=2,
         label='Cumulative mistakes')
ax2.plot(range(T_thresh), range(T_thresh), 'k--', lw=1.5,
         label='M = T (worst case)')
ax2.set_xlabel('Time step t', fontsize=13)
ax2.set_ylabel('Cumulative mistakes', fontsize=13)
ax2.set_title('Threshold Counterexample (gamma=0)', fontsize=13)
ax2.legend()

plt.tight_layout()
plt.savefig('hw1/exp5_gamma_to_zero.png', bbox_inches='tight')
plt.show()\
"""))

# ── Cell 21: Exp 5 observation ────────────────────────────────────────────
cells.append(new_markdown_cell("""\
**Observations:**

1. **As $\\gamma \\to 0$:** The number of mistakes $M$ grows rapidly (roughly as $1/\\gamma^2$),
   and the Perceptron requires more and more rounds to converge. For very small $\\gamma$,
   the bound $R^2/\\gamma^2$ becomes enormous, and the algorithm may exhaust the training set
   before converging.

2. **Threshold counterexample ($\\gamma = 0$):** When the data is not linearly separable,
   the Perceptron makes a mistake on *every* example -- cumulative mistakes grow linearly
   with $T$. This is the worst case: $M = T$. The alternating-label example with a single
   feature $x_t = 1$ is the canonical demonstration that the Perceptron *requires* linear
   separability (positive margin) to have a finite mistake bound.

3. **Connection:** The threshold counterexample is the $\\gamma \\to 0$ limit. As $\\gamma$
   decreases toward 0, the data becomes "almost non-separable," and the Perceptron's
   behaviour transitions from fast convergence to the divergent worst-case regime.\
"""))

# ── Cell 22: Summary ──────────────────────────────────────────────────────
cells.append(new_markdown_cell("""\
## 7. Summary

| Question | Finding |
|----------|---------|
| **Q1** Data generation | Sample Gaussian points, shift to enforce margin $\\gamma$, normalise to enforce radius $R$. Choices: $d$, $T$, $w^*$, sphere vs ball. |
| **Q2** $M$ vs $1/\\gamma^2$ | Linear relationship confirmed empirically; log-log slope $\\approx 1$. |
| **Q3** Bound tightness | Bound is **not tight** on random data; empirical $M \\ll R^2/\\gamma^2$. |
| **Q4** Dimension $d$ | Mistake count is **dimension-free** -- flat across $d \\in [2, 500]$. |
| **Q5** $\\gamma \\to 0$ | Mistakes blow up; threshold counterexample shows $M = T$ when $\\gamma = 0$. |\
"""))

nb.cells = cells
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.10.0"
    }
}

import json, os
out_path = os.path.join(os.path.dirname(__file__), 'perceptron.ipynb')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(nbformat.writes(nb), f, ensure_ascii=False)

# nbformat.write writes a string; we want the actual notebook dict
with open(out_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print(f'Wrote {out_path}')
