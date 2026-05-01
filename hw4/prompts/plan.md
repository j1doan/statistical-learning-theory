**Weighted finite-class bound**

Definition: With probability at least $1 - \delta$ over $S \sim \mathcal{D}^n$, for all $h \in \mathcal{H}$ with $p(h) > 0$,
$$
L_{\mathcal{D}}(h) \le L_S(h) + \sqrt{\frac{\log(1/p(h)) + \log(1/\delta)}{2n}}
$$

Recall the penalty:
$$
\sqrt{\frac{\log(1/p(h)) + \log(1/\delta)}{2n}}
$$

Define complexity

$$
\mathrm{complexity}(h) \coloneqq \log\left(\frac{1}{p(h)}\right).
$$

---

**Kraft inequality**

Definition: Let $d : \mathcal{H} \to \{0,1\}^*$ be a prefix-free description. Then
$$
\sum_{h \in \mathcal{H}} 2^{-|d(h)|} \le 1
$$

---

**Weighted bound**

Definition:
$$
L_{\mathcal{D}}(h) \le L_S(h) + \sqrt{\frac{\mathrm{complexity}(h) + \log(1/\delta)}{2n}}
$$

---

**Minimum Description Length**

Definition:
$$
\mathrm{MDL}_p(S) = \arg\max_{h : L_S(h)=0} p(h)
= \arg\min_{h : L_S(h)=0} |d(h)|
$$

---

**MDL guarantee**

Definition:
$$
L_{\mathcal{D}}(\mathrm{MDL}_p(S)) \le \sqrt{\frac{|d(h^\star)| \cdot \log 2 + \log(1/\delta)}{2n}}
$$

---

**Agnostic PAC learnability**

Definition: There exists a rule $A$ such that for all $\epsilon, \delta > 0$, there exists $n_{\mathcal{H}}(\epsilon,\delta)$ such that for all $\mathcal{D}$ and all $h \in \mathcal{H}$:
$$
\mathbb{P}_{S \sim \mathcal{D}^n}\big[L_{\mathcal{D}}(A(S)) \le L_{\mathcal{D}}(h) + \epsilon\big] \ge 1 - \delta
$$

---

**Non-uniform learnability**

Definition: There exists a rule $A$ such that for all $\epsilon, \delta > 0$, for all $h \in \mathcal{H}$, there exists $n_{\mathcal{H}}(\epsilon,\delta,h)$ such that for all $\mathcal{D}$:
$$
\mathbb{P}_{S \sim \mathcal{D}^n}\big[L_{\mathcal{D}}(A(S)) \le L_{\mathcal{D}}(h) + \epsilon\big] \ge 1 - \delta
$$

---

**Structural Risk Minimization (SRM, Vapnik)**

Definition: From weighted Hoeffding, define the penalty
$$
\epsilon(n,\delta,p(h)) \coloneqq \sqrt{\frac{\mathrm{complexity}(h) + \log(2/\delta)}{2n}},
\quad \mathrm{complexity}(h) = \log(1/p(h))
$$

SRM rule:
$$
\hat{h} = \mathrm{SRM}_p(S) = \arg\min_{h} \{L_S(h) + \epsilon(n,\delta,p(h))\}
$$

---

**Hypothesis-level SRM**

Definition: Let $\mathcal{H}$ be countable and $p:\mathcal{H}\to[0,1]$ satisfy $\sum_{h \in \mathcal{H}} p(h) \le 1$. With probability at least $1-\delta$ over $S \sim \mathcal{D}^n$,
$$
L_{\mathcal{D}}(\hat{h}) \le \inf_{h \in \mathcal{H}} \left\{
L_{\mathcal{D}}(h) + 2\epsilon(n,\delta,p(h))
\right\}
$$

---

**Class-level SRM**

Definition: Let $\mathcal{H} = \bigcup_{r \ge 1} \mathcal{H}_r$ with $\mathrm{VCdim}(\mathcal{H}_r) < \infty$ and priors $p_r \ge 0$, $\sum_r p_r \le 1$. With probability at least $1-\delta$,
$$
L_{\mathcal{D}}(\hat{h}) \le \inf_{r \ge 1,\, h \in \mathcal{H}_r}
\left\{
L_{\mathcal{D}}(h)
+ 2C \sqrt{\frac{\mathrm{VCdim}(\mathcal{H}_r) + \log(1/p_r) + \log(1/\delta)}{n}}
\right\}
$$

---

**Characterization**

Definition: A binary class $\mathcal{H}$ is non-uniformly learnable if and only if
$$
\mathcal{H} = \bigcup_{r=1}^\infty \mathcal{H}_r
\quad \text{with } \mathrm{VCdim}(\mathcal{H}_r) < \infty \ \forall r
$$

---

**Kullback-Leibler divergence between posterior $Q$ and prior $P$**

Definition:
$$
\mathrm{KL}(Q \| P) = \mathbb{E}_{h \sim Q}\left[\log \frac{q(h)}{p(h)}\right]
$$

---

**PAC-Bayes**

Definition: For any prior $P$, with probability at least $1-\delta$ over $S \sim \mathcal{D}^n$, simultaneously for all posteriors $Q$,
$$
L_{\mathcal{D}}(Q) \le L_S(Q) +
\sqrt{\frac{\mathrm{KL}(Q \| P) + \log(2n/\delta)}{2(n-1)}}
$$

---

**Closed-form solution of PAC-Bayes learning rule (Gibbs / Boltzmann posterior)**

Definition:
$$
Q_\lambda(h) \propto P(h)\exp(-L_S(h)/\lambda)
$$