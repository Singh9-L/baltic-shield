# Formal Equations (ODD Protocol) — 11 equations
1. S_i = 0.50 + 0.20*MT_i(RU) - 0.14*Edu_i + 0.08*EC_i + epsilon
2. CoNVaI_m = 0.25*N + 0.30*E + 0.30*NM + 0.15*Bot
4a. CT>=0.6: dB = q*0.3 - (1-q)*0.1 (Central route)
4b. CT<0.6: dB = (0.6*E + 0.4*NM)*trust*S (Peripheral route)
6a. P(S->E) = CoNVaI * deg(i)/D_max * P(exposed)
6b. P(E->B) = S * EC * (1-CT) * trust
6c. P(B->R) = 0.18 (active nudge) / 0.06 (passive)
8. P(edge) = P_base * (0.5+0.5*cos_sim(B_i,B_j)) * deg(j)/D_mean
9. P(bot_detected) = Bernoulli(0.94) if BotAgent
10. P(viral) = Bernoulli(0.89) if velocity > 20/hour
11. f(x)-f(x') = Sum phi_k (SHAP)
