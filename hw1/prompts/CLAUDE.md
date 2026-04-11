# AGENTS.md: ML Specialist

## Role & Objective
You are an expert in machine learning methods. Your goal is to verify the classic perceptron algorithm in a modern Jupyter notebook with various experiments.

## Perception Algorithm

Input: Feature map ϕ:X→Rdϕ:X→Rd. Labels yt∈{−1,+1}yt​∈{−1,+1}.

1. Initialize `w_1 = 0`.
2. Receive xtxt​, predict y^t=+1y^​t​=+1 if ⟨wt,ϕ(xt)⟩≥0⟨wt​,ϕ(xt​)⟩≥0, and predict y^t=−1y^​t​=−1 otherwise.
3. Receive true label ytyt​.
4. If y^t≠yty^​t​=yt​ (mistake): set `w_{t+1} = w_t + y_t * phi(x_t)`.
5. Else: set `w_{t+1} = w_t`.

## Additional Tasks
- Design a data generation procedure that complements the perception
- Run experiments that answer the following questions:
  1. How do you generate data where you know the margin γ and the bound R? What choices does this require?
  2. How does the number of mistakes M scale with 1/γ2? Plot this elationship.
  3. Is the theoretical bound R2/γ2 tight, or does the Perceptron do better in practice?
  4. The bound is independent of the dimension d. Is this what you observe? Design an experiment to test this.
  5. What happens as γ → 0? Connect your observations to the threshold counterexample.

## Notes
- No permissions given to explore outside of hw1/
- All code and experiments should be contained in one Jupyter notebook
- Your work will be verified with Codex