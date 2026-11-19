# Mock Final 3

**Covers:** everything (Topics 1–22). Same layout as the finals: Q1 = 40 marks of short parts, Q2 = the pn diode (30), Q3 = BJT design and BJT vs MOSFET (30). Built on tutorial and past-final questions (shown in brackets) with new numbers or a twist.

**How to use it:**
- Do it on paper, closed book, with only the [formula sheet](../formula-sheet.md).
- 2 hours.
- Mark yourself with the answers at the bottom. Each answer says which topic and § to go back to.

**Constants:** ε₀ = 8.85 × 10⁻¹⁴ F/cm, nᵢ = 1.45 × 10¹⁰ cm⁻³ (nᵢ² ≈ 2.1 × 10²⁰ cm⁻⁶), ε_Si = 11, ε_ox = 4, V_T = 0.026 V, e = 1.6 × 10⁻¹⁹ C, E_G = 1.12 eV, χ = 4.05 eV, N_C = 3.2 × 10¹⁹ cm⁻³, N_V = 1.8 × 10¹⁹ cm⁻³.

---

## Questions

### Q1. Short questions across the course (2015 Q1, 2016 Q1, 2018 Q1, Ch1 Q10–Q15) — 40 marks

**a)** Find the probability that a state 0.1 eV **above** E_F is filled. What is the probability that a state 0.1 eV **below** E_F holds a **hole**? (4)

**b)** Where is the intrinsic level E_i, measured from E_V? Is it exactly midgap? (4)

**c)** A metal with φ_m = 4.6 eV is put on p-type Si with N_A = 10¹⁵ cm⁻³. Is the contact ohmic or Schottky? Prove it and give the barrier (φ_s − φ_m). (6)

**d)** 1 V is applied across a 2 µm n-Si bar (ideal contacts). How far do the bands drop, and what is the field? (4)

**e)** Answer yes or no. (1 each)
i) A p-channel depletion MOSFET has V_th > 0.
ii) The MOSFET channel current in strong inversion is mainly diffusion.
iii) A forward-biased pn diode has a larger depletion width than at zero bias.
iv) In a BJT in saturation, both junctions are forward biased.

**f)** A gate C–V curve is flat at 1.2 pF for V_GS > 0 and flat at 0.3 pF for V_GS < −0.6 V. The gate is 25 µm × 4 µm. Give the MOSFET type, V_th and t_ox. (6)

**g)** Explain why a forward-biased p⁺n junction is a good **hole injector** and a reverse-biased np junction is a good **collector**. (5)

**h)** Sketch the cross section of an nMOS at V_GS > V_th with small V_DS. Show the inversion layer and the depletion regions. (3)

**i)** A short BJT has its base width halved. What happens to I_C, I_B and β at the same V_BE? (4)

---

### Q2. A p⁺n diode (Ch2 Q5, Q9–Q13, 2014 Q2a, 2015 Q1f, 2018 Q2d) — 30 marks

A Si p⁺n diode: N_A = 10¹⁸ cm⁻³, N_D = 10¹⁵ cm⁻³. The n region is 5 µm long (D_p = 10 cm²/s) and the p region is 2 µm long (D_n = 30 cm²/s). Both are shorter than the diffusion lengths. Ideal contacts.

**a)** Sketch the band diagram at zero bias and at 0.5 V forward bias. Calculate V_bi. (6)

**b)** Find the depletion width at 0 V and at 0.5 V forward. Where does it sit? (6)

**c)** Find the maximum electric field at zero bias and say where it is. (4)

**d)** At 0.5 V forward, find the minority carrier concentrations at both depletion edges and sketch the minority carrier profiles through the diode. (6)

**e)** Find J_p, J_n and the total current density at 0.5 V. Take the depletion region into account. (6)

**f)** The n region is made half as long. What happens to J? (2)

---

### Q3. Designing a BJT, and BJT vs MOSFET (2016 Q2, 2015 Q3c, 2014 Q1g, 2018 Q3c) — 30 marks

A short n⁺pn BJT: emitter N_D = 10¹⁹ cm⁻³, X_E = 0.2 µm, D_pE = 3 cm²/s; base N_A = 5 × 10¹⁶ cm⁻³, W_B = 0.4 µm (undepleted), D_nB = 20 cm²/s. Area 2 × 10⁻⁵ cm². Forward active mode, V_BE = 0.7 V.

**a)** Derive β in terms of the doping, widths and diffusion constants, and evaluate it. (6)

**b)** Calculate I_C, I_B and the emitter efficiency γ. (6)

**c)** Without recalculating everything, say what happens to I_C, I_B and β if (i) the emitter doping is doubled (ii) the base width is halved. Justify each. (6)

**d)** Including the BC leakage current I_L, show how β changes. (4)

**e)** Give four differences between a MOSFET and a BJT (carrier type, transport, control, input resistance). (4)

**f)** Draw the low-frequency small-signal circuit of the BJT and give the condition for using it. (4)

---

## Answers

<details><summary>Q1 answers</summary>

**a)** f = 1 ÷ (1 + e^(0.1/0.026)) = 1 ÷ (1 + 46.8) = **0.021** (2)

Hole probability at 0.1 eV below = 1 − f = 1 − 1 ÷ (1 + e^(−3.85)) = **0.021**. Same: the Fermi function is symmetric about E_F. (2)

From: Topic 5

<br>

**b)** Setting n = p for intrinsic Si gives E_i = E_G/2 + (kT/2) ln(N_V/N_C) = 0.56 + 0.013 × ln(0.5625) = **0.55 eV** above E_V. Not exactly midgap: N_V < N_C pulls it down by 7.5 meV. (4)

From: Topic 5 §7

<br>

**c)** E_F − E_V = kT ln(N_V/N_A) = 0.026 × ln(1.8 × 10⁴) = 0.255 eV, so E_C − E_F = 0.865 eV. (2)

φ_s = χ + (E_C − E_F) = 4.05 + 0.865 = **4.915 eV** (2)

φ_m = 4.6 < φ_s on **p-type**: holes are pushed away from the surface (depletion): **Schottky**. Barrier φ_s − φ_m = **0.32 eV**. (2)

From: Topic 9

<br>

**d)** The bands drop by **1 eV** from the − end to the + end. |ℰ| = 1 V ÷ 2 × 10⁻⁴ cm = **5 × 10³ V/cm**, pointing from the + contact to the − contact. (4)

From: Topic 7

<br>

**e)** i) **yes** ii) **no** (drift) iii) **no** (smaller) iv) **yes**

From: Topics 18, 17, 14, 20

<br>

**f)** High C at **positive** gate (electron accumulation) → n-substrate → **p-channel** MOSFET. **V_th = −0.6 V**. (3)

A = 25 × 10⁻⁴ × 4 × 10⁻⁴ = 10⁻⁶ cm². C_ox = 1.2 × 10⁻⁶ F/cm². t_ox = 8.85 × 10⁻¹⁴ × 4 ÷ 1.2 × 10⁻⁶ = **2.95 × 10⁻⁷ cm ≈ 3 nm**. (3)

From: Topic 16

<br>

**g)** **Injector:** forward bias lowers the barrier. The injected currents scale as p_n0 ∝ 1/N_D and n_p0 ∝ 1/N_A. With N_A ≫ N_D, almost all the current is **holes** going into the n side. (3)

**Collector:** a reverse-biased junction's current is limited only by the **supply of minority carriers** at its edge. Any extra minority carriers that arrive (e.g. from an injector) are swept across by the field. (2)

From: Topic 20 §2

<br>

**h)** n⁺ source and drain in p-Si. A thin **inversion layer** under the oxide from S to D (slightly thinner at the drain). A **depletion layer** under the inversion layer and around the source and drain (larger around the drain). (3)

From: Topic 17, Ch3 Q5

<br>

**i)** I_C ∝ 1/W_B: **doubles**. I_B is set by the emitter: **unchanged**. So β **doubles**. (4)

From: Topic 21, Equation 36

</details>

<details><summary>Q2 answers</summary>

**a)** V_bi = 0.026 × ln(10¹⁸ × 10¹⁵ ÷ 2.1 × 10²⁰) = **0.76 V** (2)

Zero bias: flat E_F. p⁺ side: E_V just below E_F. n side: E_C a little above E_F (N_D = 10¹⁵, so E_C − E_F = 0.026 ln(3.2 × 10⁴) = 0.27 eV). Bands step down from p to n by eV_bi, the bend mostly on the **n side**. (2)

0.5 V forward: E_F splits by 0.5 eV (n side E_F **up**). The step shrinks to e(V_bi − 0.5) = 0.26 eV. Depletion region narrower. (2)

From: Topic 10, Topic 11

<br>

**b)** N_A ≫ N_D: nearly all the depletion is on the **n side** (w_p = w_n N_D/N_A, 1000× smaller).

w_n(0) = √(2εV_bi N_A ÷ (e(N_A + N_D)N_D)) = **9.6 × 10⁻⁵ cm ≈ 0.96 µm** (3)

w_n(0.5 V) = √(2ε(V_bi − 0.5)N_A ÷ (e(N_A + N_D)N_D)) = **5.6 × 10⁻⁵ cm ≈ 0.56 µm** (3)

From: Topic 14

<br>

**c)** |ℰ_max| = eN_D w_n/ε = 1.6 × 10⁻¹⁹ × 10¹⁵ × 9.6 × 10⁻⁵ ÷ 9.74 × 10⁻¹³ = **1.6 × 10⁴ V/cm**, at the **metallurgic junction**. (4)

(Check: for a one-sided junction ℰ_max ≈ 2V_bi/W = 2 × 0.76 ÷ 9.6 × 10⁻⁵ = 1.6 × 10⁴ V/cm ✓.)

From: Topic 14

<br>

**d)** e^(0.5/0.026) = 2.2 × 10⁸.

- n side (holes): p_n0 = 2.1 × 10²⁰ ÷ 10¹⁵ = 2.1 × 10⁵ → p′_n = **4.7 × 10¹³ cm⁻³** (2)
- p side (electrons): n_p0 = 2.1 × 10²⁰ ÷ 10¹⁸ = 210 → n′_p = **4.7 × 10¹⁰ cm⁻³** (2)

Sketch: straight lines from these values at the depletion edges down to p_n0 and n_p0 at the contacts. The n-side line is **1000× higher**. (2)

From: Topic 12

<br>

**e)** Undepleted n region = 5 − 0.56 = 4.44 µm.

J_p = eD_p p′_n ÷ W_n = 1.6 × 10⁻¹⁹ × 10 × 4.7 × 10¹³ ÷ 4.44 × 10⁻⁴ = **0.17 A/cm²** (3)

J_n = eD_n n′_p ÷ W_p = 1.6 × 10⁻¹⁹ × 30 × 4.7 × 10¹⁰ ÷ 2 × 10⁻⁴ = **1.1 × 10⁻³ A/cm²** (2)

J ≈ **0.17 A/cm²**, almost all holes. (1)

From: Topic 13

<br>

**f)** The hole current dominates and J_p ∝ 1/W_n. Undepleted 2.5 − 0.56 = 1.94 µm, so J_p = 0.17 × 4.44/1.94 ≈ **0.39 A/cm²**: a bit more than double (the depletion width doesn't shrink). (2)

From: Topic 13 §6

</details>

<details><summary>Q3 answers</summary>

**a)** I_C ≈ eA D_nB n_p0 e^(V_BE/V_T)/W_B (electrons across the base). I_B ≈ eA D_pE p_n0 e^(V_BE/V_T)/X_E (holes into the emitter). With n_p0 = nᵢ²/N_AB and p_n0 = nᵢ²/N_DE: (3)

β = D_nB N_DE X_E ÷ (D_pE N_AB W_B) = 20 × 10¹⁹ × 0.2 ÷ (3 × 5 × 10¹⁶ × 0.4) = **667** (3)

From: Topic 21, Equation 36

<br>

**b)** e^(0.7/0.026) = 4.9 × 10¹¹. n_p0 = 2.1 × 10²⁰ ÷ 5 × 10¹⁶ = 4200 cm⁻³.

I_C = 1.6 × 10⁻¹⁹ × 2 × 10⁻⁵ × 20 × 4200 × 4.9 × 10¹¹ ÷ 0.4 × 10⁻⁴ = **3.3 × 10⁻³ A** (3)

I_B = I_C/β = **5.0 × 10⁻⁶ A** (2)

γ = 1 ÷ (1 + 1/β) = **0.9985** (1)

From: Topic 21

<br>

**c)** i) **Emitter doping × 2:** I_C unchanged (set by the base); I_B halves (p_n0 ∝ 1/N_DE); β doubles. (2014 Q1g.) (3)

ii) **Base width ÷ 2:** I_C doubles (gradient ∝ 1/W_B); I_B unchanged; β doubles. (3)

From: Topic 21 §2

<br>

**d)** The BC leakage adds to I_C and subtracts from I_B:

β_leak = (I_C + I_L) ÷ (I_B − I_L) > I_C/I_B

So β **increases** (very slightly here, since I_L ≪ I_B). (4)

From: Topic 21 §3

<br>

**e)** (1 each)

| | MOSFET | BJT |
|---|---|---|
| carriers that matter | majority (channel) | minority (base) |
| transport | drift | diffusion |
| control | gate **voltage**, insulated (field effect) | base **current**, ohmic contact |
| input resistance | infinite (DC) | finite, R_π = β/g_m |

From: Topic 20 §5

<br>

**f)** R_π from B to E; current source g_m v_be from C to E; R_o in parallel with it. (2)

Valid for **small** v_be (≪ V_T), so I_C varies **linearly** with v_be. (2)

From: Topic 22 §2, §3

</details>
