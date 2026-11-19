# Mock Final 1

**Covers:** everything (Topics 1–22). Same layout as the 2014 to 2018 finals: Q1 = 40 marks of short parts across the course, Q2 = MOSFET (30), Q3 = BJT (30). Every part is built on a tutorial or past-final question (shown in brackets) with new numbers or a twist.

**How to use it:**
- Do it on paper, closed book, with only the [formula sheet](../formula-sheet.md).
- 2 hours.
- Mark yourself with the answers at the bottom. Each answer says which topic and § to go back to.

**Constants:** ε₀ = 8.85 × 10⁻¹⁴ F/cm, nᵢ = 1.45 × 10¹⁰ cm⁻³ (nᵢ² ≈ 2.1 × 10²⁰ cm⁻⁶), ε_Si = 11, ε_ox = 4, V_T = 0.026 V, e = 1.6 × 10⁻¹⁹ C, E_G = 1.12 eV, χ = 4.05 eV, N_C = 3.2 × 10¹⁹ cm⁻³, N_V = 1.8 × 10¹⁹ cm⁻³.

---

## Questions

### Q1. Semiconductor basics and devices (2017 Q1, 2018 Q1, 2015 Q1) — 40 marks

**a)** A metal's resistance goes **up** when it is heated. Pure Si's resistance goes **down**. Explain the difference in at most 40 words. (2)

**b)** An n-type Si substrate is doped with 5 × 10¹⁶ cm⁻³ phosphorus atoms. Boron is implanted into it to make a final homogeneous acceptor density of 2 × 10¹⁷ cm⁻³. Calculate the exact hole and electron densities in the implanted region. (6)

**c)** The workfunction of a Si sample is 4.25 V. Determine the doping type and the doping concentration. (6)

**d)** In a uniformly doped Si bar, 3 µm long, E_C drops linearly from 0.9 eV at x = 0 to 0.6 eV at x = 3 µm (no voltage drop at the contacts). Give (i) the potential difference across the bar, (ii) the size and direction of the electric field, (iii) the polarity of the battery. (6)

**e)** Which of Al (φ = 4.1 eV), Ti (4.4 eV) and W (4.8 eV) give an **ohmic** contact on n-type Si with N_D = 10¹⁷ cm⁻³? Prove it. (6)

**f)** In a forward-biased p⁺n diode, the excess hole concentration at the n-side depletion edge is 2 × 10⁸ cm⁻³. The undepleted n region is 2 µm long (shorter than the diffusion length) and D_p = 10 cm²/s. Find the current density. State your assumption. (6)

**g)** Answer yes or no. (1 each)

i) Increasing the temperature increases nᵢ.
ii) In an nMOS in saturation, any extra V_DS drops mostly across the channel.
iii) A depletion-mode nMOS conducts at V_GS = 0.
iv) The base current of an npn BJT in forward active mode is mainly electrons.
v) The Fermi level is flat through a pn diode under forward bias.
vi) In accumulation, the capacitance of a MOS capacitor is set by the oxide only.
vii) Doubling the base width of a short BJT doubles I_C.
viii) In a p⁺n diode the current is mostly holes injected into the n side.

---

### Q2. An n-channel MOSFET (2014 Q3, 2016 Q3, Ch3 Q7, 2016 Q1d) — 30 marks

A MOSFET has W = 50 µm, L = 2 µm, substrate doping 10¹⁷ cm⁻³ and V_th = 0.8 V. Its gate C–V curve (bulk grounded) is **flat at 0.708 pF for V_GS < −0.5 V** and **flat at 0.0857 pF for V_GS > 0.8 V**.

**a)** Is it an n-channel or a p-channel MOSFET? Give the doping type of the source, drain and substrate. (4)

**b)** Extract the oxide thickness. (3)

**c)** Extract the maximum depletion width from the C–V values. Check it against the formula sheet. (4)

**d)** Sketch the band diagram (E_C, E_F, E_V) from the gate into the substrate in (i) accumulation and (ii) at V_GS = V_th. Show the field direction. (6)

**e)** µ_n = 400 cm²/Vs and V_GS = 2.0 V. Find I_DS at V_DS = 0.5 V and at V_DS = 3 V. Say which region each is in. (6)

**f)** Derive g_m in saturation and evaluate it at V_GS = 2.0 V. (4)

**g)** Explain, with a band diagram from source to drain, why I_DS stops rising past pinch-off. (3)

---

### Q3. A short n⁺pn BJT (2016 Q2, 2018 Q3, 2017 Q2) — 30 marks

Emitter: N_D = 10¹⁹ cm⁻³, undepleted width X_E = 0.3 µm, hole diffusion constant D_pE = 2 cm²/s. Base: N_A = 10¹⁷ cm⁻³, undepleted width W_B = 0.5 µm, electron diffusion constant D_nB = 15 cm²/s. Area 10⁻⁵ cm². All layers are shorter than the diffusion lengths. V_BE = 0.65 V forward, BC reverse biased.

**a)** Sketch the band diagram (E_C, E_F, E_V) in forward active mode. Show eV_BE, eV_BC and the depletion regions. (6)

**b)** Calculate the minority carrier concentrations on both sides of the EB depletion region. (6)

**c)** Calculate I_C, I_B, I_E and β. Neglect the BC leakage. (8)

**d)** Find g_m and R_π. (4)

**e)** The Early voltage is 60 V. Find R_o, and I_C when V_CE is raised by 5 V. (3)

**f)** Explain the physical reason for the finite R_o. (3)

---

## Answers

<details><summary>Q1 answers</summary>

**a)** Heating increases scattering in both, which raises R. A metal's carrier number is fixed, so R goes up. Si's carrier number shoots up as bonds break, which outweighs the scattering, so R goes down. (2)

From: Topic 1 §3

<br>

**b)** Compensation doping: net acceptors N_A − N_D = 1.5 × 10¹⁷. Charge neutrality + mass action:

p² − (N_A − N_D)p − nᵢ² = 0 → p = [(N_A − N_D) + √((N_A − N_D)² + 4nᵢ²)]/2 = **1.5 × 10¹⁷ cm⁻³** (4)

n = nᵢ²/p = **1.4 × 10³ cm⁻³** (2)

From: Topic 2

<br>

**c)** Midgap is χ + E_G/2 = 4.61 eV below E_vac. φ = 4.25 < 4.61, so E_F is **above** E_i: **n-type**. (2)

E_C − E_F = φ − χ = 4.25 − 4.05 = 0.20 eV

N_D = N_C e^(−0.20/0.026) = 3.2 × 10¹⁹ × 4.6 × 10⁻⁴ = **1.5 × 10¹⁶ cm⁻³** (4)

From: Topic 6

<br>

**d)** i) ΔV = 0.3 eV ÷ e = **0.3 V**. (2)

ii) |ℰ| = 0.3 V ÷ 3 × 10⁻⁴ cm = **1000 V/cm** (10⁵ V/m), pointing towards **x = 0** ("uphill", where the bands are higher). (2)

iii) Positive voltage lowers the bands, so **+ at x = 3 µm**, − at x = 0. (2)

From: Topic 7

<br>

**e)** φ_s = χ + kT ln(N_C/N_D) = 4.05 + 0.026 × ln(320) = 4.05 + 0.15 = **4.20 eV**. (3)

Ohmic on **n-type** needs φ_m < φ_s (electrons flow into the Si: accumulation). Only **Al (4.1 eV)** works. Ti and W give Schottky contacts. (3)

From: Topic 9, Topic 6

<br>

**f)** Assume J ≈ J_p (p⁺n: the hole current dominates). Short n region, straight-line profile:

J = eD_p Δp ÷ W_n = 1.6 × 10⁻¹⁹ × 10 × 2 × 10⁸ ÷ 2 × 10⁻⁴ = **1.6 × 10⁻⁶ A/cm²** (6)

From: Topic 13

<br>

**g)** i) **yes** ii) **no** (across the channel–drain depletion region) iii) **yes** iv) **no** (holes) v) **no** (it splits by eV) vi) **yes** vii) **no** (it halves) viii) **yes**

From: Topics 1, 17, 18, 21, 11, 16, 21, 12

</details>

<details><summary>Q2 answers</summary>

**a)** C is high at **negative** gate (hole accumulation), so the substrate is **p-type**: an **n-channel** MOSFET. Source and drain **n⁺**, substrate **p**. (4)

From: Topic 16 §2

<br>

**b)** A = 50 × 10⁻⁴ × 2 × 10⁻⁴ = 10⁻⁶ cm². C_ox = 0.708 × 10⁻¹² ÷ 10⁻⁶ = 7.08 × 10⁻⁷ F/cm².

t_ox = ε₀ε_ox/C_ox = 8.85 × 10⁻¹⁴ × 4 ÷ 7.08 × 10⁻⁷ = **5 × 10⁻⁷ cm = 5 nm** (3)

From: Topic 16, Equation 28

<br>

**c)** W = ε₀ε_Si A (C_max − C_min) ÷ (C_max C_min) = 8.85 × 10⁻¹⁴ × 11 × 10⁻⁶ × 0.622 × 10⁻¹² ÷ (0.708 × 10⁻¹² × 0.0857 × 10⁻¹²) = **1.0 × 10⁻⁵ cm = 0.1 µm** (3)

Formula sheet: 2√(ε (kT/e) ln(N/nᵢ) ÷ (eN)) = 2√(9.74 × 10⁻¹³ × 0.026 × 15.75 ÷ (1.6 × 10⁻¹⁹ × 10¹⁷)) = 1.0 × 10⁻⁵ cm. ✓ (1)

From: Topic 16, Equations 29 and 30

<br>

**d)** i) **Accumulation (V_GS < 0):** gate E_F **up** by e|V|; oxide bands tilt; Si bands bend **up** at the surface (E_V nearer E_F, holes pile up); ℰ from Si to gate. (3)

ii) **V_GS = V_th:** gate E_F **down** by eV_th; Si bands bend **down**; at the surface E_C − E_F equals E_F − E_V in the bulk; ℰ from gate into Si. (3)

From: Topic 15, drawing checklist

<br>

**e)** µC_ox W/L = 400 × 7.08 × 10⁻⁷ × 25 = 7.08 × 10⁻³ A/V². Pinch-off at V_DS = 2.0 − 0.8 = 1.2 V.

- V_DS = 0.5 V < 1.2 V: **triode**. I = 7.08 × 10⁻³ × (1.2 × 0.5 − 0.125) = **3.4 × 10⁻³ A** (3)
- V_DS = 3 V > 1.2 V: **saturation**. I = ½ × 7.08 × 10⁻³ × 1.2² = **5.1 × 10⁻³ A** (3)

From: Topic 17, Equations 32 and 33

<br>

**f)** I_sat = (µC_ox W/2L)(V_GS − V_th)² → g_m = dI/dV_GS = (µC_ox W/L)(V_GS − V_th) = 7.08 × 10⁻³ × 1.2 = **8.5 × 10⁻³ S** (4)

From: Topic 19, Equation 34

<br>

**g)** Past pinch-off the drain end of the channel is depleted: a reverse-biased channel–drain junction. Extra V_DS drops there (steep drop at the drain end of the S → D band diagram). The slope in the channel and the **source–channel barrier** hardly change, so the supply of electrons and the current stay the same. (3)

From: Topic 17 §5

</details>

<details><summary>Q3 answers</summary>

**a)** Base E_F as the reference. Emitter E_F **eV_BE above**, collector E_F **eV_BC below**. E_C closest to E_F in the n⁺ emitter. Flat bands in each region, no slope in the base. Depletion narrow at the forward EB junction (mostly in the base), wider at the reverse BC junction (mostly in the lighter side). (6)

From: Topic 20 §3

<br>

**b)** e^(0.65/0.026) = e²⁵ = 7.2 × 10¹⁰.

- Emitter (holes): p_n0 = 2.1 × 10²⁰ ÷ 10¹⁹ = 21 cm⁻³ → p′_n = **1.5 × 10¹² cm⁻³** (3)
- Base (electrons): n_p0 = 2.1 × 10²⁰ ÷ 10¹⁷ = 2100 cm⁻³ → n′_p = **1.5 × 10¹⁴ cm⁻³** (3)

From: Topic 21, ⭐ boundary table

<br>

**c)**

I_C = eA D_nB n′_p ÷ W_B = 1.6 × 10⁻¹⁹ × 10⁻⁵ × 15 × 1.51 × 10¹⁴ ÷ 0.5 × 10⁻⁴ = **7.3 × 10⁻⁵ A** (3)

I_B = eA D_pE p′_n ÷ X_E = 1.6 × 10⁻¹⁹ × 10⁻⁵ × 2 × 1.51 × 10¹² ÷ 0.3 × 10⁻⁴ = **1.6 × 10⁻⁷ A** (3)

I_E = I_C + I_B = **7.3 × 10⁻⁵ A**. β = I_C/I_B = **450** (2)

Check: β = D_nB N_DE X_E ÷ (D_pE N_AB W_B) = 15 × 10¹⁹ × 0.3 ÷ (2 × 10¹⁷ × 0.5) = 450 ✓

From: Topic 21, Equations 35 and 36

<br>

**d)** g_m = I_C/V_T = 7.27 × 10⁻⁵ ÷ 0.026 = **2.8 × 10⁻³ S** (2)

R_π = β/g_m = 450 ÷ 2.8 × 10⁻³ = **1.6 × 10⁵ Ω** (2)

From: Topic 22, Equation 37

<br>

**e)** R_o = V_A/I_C = 60 ÷ 7.27 × 10⁻⁵ = **8.3 × 10⁵ Ω**. ΔI_C = 5 ÷ 8.3 × 10⁵ = 6 µA, so I_C ≈ **7.9 × 10⁻⁵ A**. (3)

From: Topic 22 §4 f

<br>

**f)** Base width modulation: larger V_CE → larger reverse |V_CB| → the BC depletion region reaches further into the base → smaller undepleted W_B → steeper electron gradient → larger I_C. (3)

From: Topic 22 §1

</details>
