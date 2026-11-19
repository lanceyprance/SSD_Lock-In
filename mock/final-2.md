# Mock Final 2

**Covers:** everything (Topics 1–22). Same layout as the finals: Q1 = 40 marks of short parts, Q2 = BJT (30), Q3 = MOSFET (30). Built on tutorial and past-final questions (shown in brackets) with new numbers or a twist.

**How to use it:**
- Do it on paper, closed book, with only the [formula sheet](../formula-sheet.md).
- 2 hours.
- Mark yourself with the answers at the bottom. Each answer says which topic and § to go back to.

**Constants:** ε₀ = 8.85 × 10⁻¹⁴ F/cm, nᵢ = 1.45 × 10¹⁰ cm⁻³ (nᵢ² ≈ 2.1 × 10²⁰ cm⁻⁶), ε_Si = 11, ε_ox = 4, V_T = 0.026 V, e = 1.6 × 10⁻¹⁹ C, E_G = 1.12 eV, χ = 4.05 eV, N_C = 3.2 × 10¹⁹ cm⁻³, N_V = 1.8 × 10¹⁹ cm⁻³.

---

## Questions

### Q1. Carriers, fields and the pn diode (2018 Q2b, 2014 Q1b d, 2014 Q2b, 2015 Q1f, Ch2 Q12) — 40 marks

**a)** Prove the law of mass action n × p = nᵢ² from the formula sheet. (4)

**b)** Si is doped with 5 × 10¹⁵ cm⁻³ boron. Find E_F − E_V and E_C − E_F. (4)

**c)** A bar of the Si in (b) is 2 mm long in the current direction, with a 100 µm × 10 µm cross section. µ_p = 450 cm²/Vs. Find its resistance. (4)

**d)** An n-type layer has N_D(x) = 2 × 10¹⁷ e^(−x/L) with L = 1 µm. Derive the built-in electric field with no bias, give its size and direction. (6)

**e)** An unbiased pn junction has N_A = 10¹⁷ cm⁻³ and N_D = 10¹⁶ cm⁻³. Find V_bi, w_n, w_p and the maximum field. Where is the field maximum? (8)

**f)** The diode in (e) is forward biased at 0.6 V. The undepleted n region is 3 µm long (D_p = 12 cm²/s) and the p region 2 µm long (D_n = 25 cm²/s), both shorter than the diffusion lengths. Find the hole and electron current densities and the total. Which carrier dominates, and why? (8)

**g)** Answer yes or no. (1 each)

i) The probability of finding an electron at E_F is ½.
ii) In an n-type material, the electron density at E = E_F is zero.
iii) The BC depletion region of a BJT in forward active mode is crossed by drift.
iv) A pMOS enhancement device has V_th > 0.
v) C_gd of a MOSFET in saturation is about ½ C_ox W L.
vi) Increasing the emitter doping of an npn increases I_C at the same bias.

---

### Q2. A pnp BJT from its output curves (2017 Q2, 2015 Q3) — 30 marks

A short p⁺np BJT in common emitter mode has flat output curves (region II) at −I_C = 4 mA for I_B = −20 µA and −I_C = 8 mA for I_B = −40 µA, from −V_CE = 1 V upwards. Below −V_CE = 1 V the curves rise steeply (region I).

**a)** Give the bias of each junction in regions I and II. Sketch the band diagram (E_C, E_F, E_V) for region II. (8)

**b)** Sketch the **excess** minority carrier concentration in the emitter, base and collector in region II. Name the minority carrier in each region and give the value at each junction edge. (6)

**c)** Show that β ≈ D_p N_AE X_E ÷ (D_n N_DB W_B). Define every symbol. (4)

**d)** Find β from the curves. Find I_B and I_E for I_C = 2 mA in region II. (3)

**e)** Find g_m and R_π at I_C = 2 mA. (3)

**f)** The Early voltage is 50 V. Sketch the I_B = −20 µA curve with base width modulation, and find I_C at V_CE = −6 V (take the flat part from −1 V). (6)

---

### Q3. A p-channel enhancement MOSFET (2017 Q3, 2014 Q3, Ch3 Q3 Q4 Q8) — 30 marks

The pMOS has t_ox = 8 nm, W/L = 20, V_th = −1 V and µ_p = 150 cm²/Vs.

**a)** Draw the material cross section. Label the doping of every region and the four contacts. (4)

**b)** Sketch the band diagram (E_C, E_F, E_V) from the gate into the substrate at V_GS = V_th. (6)

**c)** Sketch the high-frequency C_GS–V_GS curve. Mark V_th, and give C_max per area. (6)

**d)** At V_GS = −3 V, find the drain voltage at pinch-off and the saturation current. (8)

**e)** Derive g_m in saturation and evaluate it at V_GS = −3 V. (3)

**f)** An nMOS has the same size, oxide and |V_th|, with µ_n = 400 cm²/Vs. Which carries more saturation current at |V_GS| = 3 V, and by how much? Why? (3)

---

## Answers

<details><summary>Q1 answers</summary>

**a)** n = N_C e^((E_F − E_C)/kT), p = N_V e^((E_V − E_F)/kT). Multiply: np = N_C N_V e^((E_V − E_C)/kT) = N_C N_V e^(−E_G/kT). The sheet's nᵢ = √(N_C N_V) e^(−E_G/2kT) gives nᵢ² = N_C N_V e^(−E_G/kT). So **np = nᵢ²**. E_F cancels: it holds for any doping in equilibrium. (4)

From: Topic 5, Topic 1

<br>

**b)** p = N_A = N_V e^(−(E_F − E_V)/kT) → E_F − E_V = 0.026 × ln(1.8 × 10¹⁹ ÷ 5 × 10¹⁵) = **0.21 eV** (2)

E_C − E_F = 1.12 − 0.21 = **0.91 eV** (2)

From: Topic 5

<br>

**c)** σ ≈ e p µ_p = 1.6 × 10⁻¹⁹ × 5 × 10¹⁵ × 450 = 0.36 S/cm (2)

R = L/(σA) = 0.2 cm ÷ (0.36 × 10⁻² × 10⁻³) = **5.6 × 10⁴ Ω** (2)

From: Topic 3

<br>

**d)** J_n = 0 → ℰ = −(kT/e)(1/n)(dn/dx). With n = N_D(x): (1/n)(dn/dx) = −1/L. (3)

ℰ = (kT/e)/L = 0.026 ÷ 10⁻⁴ = **260 V/cm**, constant, pointing **+x** (towards the low doping, so drift opposes the electrons' diffusion to +x). (3)

From: Topic 4 §7

<br>

**e)** V_bi = 0.026 ln(10¹⁷ × 10¹⁶ ÷ 2.1 × 10²⁰) = **0.76 V** (2)

w_n = √(2εV_bi N_A ÷ (e(N_A + N_D)N_D)) = **2.9 × 10⁻⁵ cm** (2)

w_p = w_n N_D/N_A = **2.9 × 10⁻⁶ cm** (2)

|ℰ_max| = eN_D w_n/ε = 1.6 × 10⁻¹⁹ × 10¹⁶ × 2.9 × 10⁻⁵ ÷ 9.74 × 10⁻¹³ = **4.8 × 10⁴ V/cm**, at the **metallurgic junction** x = 0. (2)

From: Topic 14, Topic 10

<br>

**f)** e^(0.6/0.026) = 1.05 × 10¹⁰.

p_n0 = 2.1 × 10²⁰ ÷ 10¹⁶ = 2.1 × 10⁴ → p′_n = 2.2 × 10¹⁴ cm⁻³. n_p0 = 2.1 × 10³ → n′_p = 2.2 × 10¹³ cm⁻³. (2)

J_p = eD_p p′_n/W_n = 1.6 × 10⁻¹⁹ × 12 × 2.2 × 10¹⁴ ÷ 3 × 10⁻⁴ = **1.4 A/cm²** (2)

J_n = eD_n n′_p/W_p = 1.6 × 10⁻¹⁹ × 25 × 2.2 × 10¹³ ÷ 2 × 10⁻⁴ = **0.44 A/cm²** (2)

J = **1.9 A/cm²**. **Holes dominate**: the **lightly doped n side** gets 10× more injected minority carriers. (2)

From: Topic 12, Topic 13

<br>

**g)** i) **yes** ii) **yes** (E_F is in the gap: no states) iii) **yes** iv) **no** v) **no** (≈ 0, pinched off) vi) **no** (I_C is set by the base)

From: Topics 5, 5, 20, 18, 19, 21

</details>

<details><summary>Q2 answers</summary>

**a)** Region I: EB forward, BC **forward** (saturation). Region II: EB forward, BC **reverse** (forward active). (2)

Band diagram (pnp, region II): base E_F as reference. The p⁺ emitter is at a **higher** voltage (forward), so its E_F is **eV_EB lower**. The p collector is at a lower voltage (reverse), so its E_F is **eV_BC higher**. E_V closest to E_F in the p⁺ emitter. Flat bands in each region. Depletion regions mostly on the lighter side, wider at the BC junction. (6)

From: Topic 20 §3 (and its test, M4)

<br>

**b)** Minority: electrons in the emitter, holes in the base, electrons in the collector. Excess **zero at the contacts**. (2)

- EB junction: Δn′_p = n_p0(e^(eV_EB/kT) − 1) (emitter), Δp′_n = p_n0(e^(eV_EB/kT) − 1) (base, much bigger). (2)
- BC junction: Δp″_n ≈ −p_n0 (base), Δn″_p ≈ −n_p0 (collector): small and negative. (1)
- Straight lines, starting at the depletion edges. (1)

From: Topic 21 §1, drawing checklist

<br>

**c)** I_C ≈ eAD_p p_n0 e^(eV_EB/kT)/W_B and I_B ≈ eAD_n n_p0 e^(eV_EB/kT)/X_E. Divide; the exponentials cancel. With p_n0 = nᵢ²/N_DB and n_p0 = nᵢ²/N_AE:

β = I_C/I_B = (D_p/W_B)(nᵢ²/N_DB) ÷ ((D_n/X_E)(nᵢ²/N_AE)) = **D_p N_AE X_E ÷ (D_n N_DB W_B)** (4)

D_p: hole diffusion constant in the base. D_n: electron diffusion constant in the emitter. N_AE: emitter doping. N_DB: base doping. X_E, W_B: undepleted emitter and base widths.

From: Topic 21, Equation 36

<br>

**d)** β = 4 mA ÷ 20 µA = **200**. I_B = 2 mA ÷ 200 = **10 µA**. I_E = I_C + I_B = **2.01 mA**. (3)

From: Topic 21 §5

<br>

**e)** g_m = I_C/V_T = 2 × 10⁻³ ÷ 0.026 = **77 mS**. R_π = β/g_m = 200 ÷ 0.077 = **2.6 kΩ**. (3)

From: Topic 22, Equation 37

<br>

**f)** R_o = V_A/I_C = 50 ÷ 4 × 10⁻³ = 12.5 kΩ, so g_o = 80 µS. (2)

Sketch: the −20 µA curve with its flat part tilted upwards; extended back it meets −V_A. (2)

I_C = 4 mA + g_o × (6 − 1) V = 4 + 0.4 = **4.4 mA** (−4.4 mA). (2)

From: Topic 22 §4 f

</details>

<details><summary>Q3 answers</summary>

**a)** n-type substrate with a bulk contact underneath. **p⁺** source and drain. Thin gate oxide between them with the gate contact on top. Contacts: S, G, D, B. No channel at V_GS = 0 (enhancement). (4)

From: Topic 18

<br>

**b)** n-substrate: the gate is at **−|V_th|**, so its E_F is **e|V_th| above** the Si E_F. Si bands bend **up** at the surface. At the interface E_F − E_V equals E_C − E_F in the bulk (hole inversion = threshold). Oxide bands tilt. ℰ from the Si to the gate. (6)

From: Topic 15 (n-substrate version), Topic 18

<br>

**c)** n-substrate: electrons **accumulate** at **positive** V_GS, so C_GS is high (C_max) on the right. Going negative, the surface depletes and C drops, reaching C_min at **V_th = −1 V**, where the hole channel forms. Flat at C_min below that. (4)

C_max per area = C_ox = 8.85 × 10⁻¹⁴ × 4 ÷ 8 × 10⁻⁷ = **4.4 × 10⁻⁷ F/cm²** (2)

From: Topic 16 ⭐ table

<br>

**d)** Pinch-off at V_DS = V_GS − V_th = −3 − (−1) = **−2 V**. (2)

µC_ox W/L = 150 × 4.425 × 10⁻⁷ × 20 = 1.33 × 10⁻³ A/V² (3)

I_sat = ½ × 1.33 × 10⁻³ × (−2)² = **2.7 × 10⁻³ A**, quoted as **−2.7 mA** for a pMOS. (3)

From: Topic 17, Equation 33

<br>

**e)** g_m = d I_sat/dV_GS = (µC_ox W/L)(V_GS − V_th) → |g_m| = 1.33 × 10⁻³ × 2 = **2.7 × 10⁻³ S** (3)

From: Topic 19, Equation 34

<br>

**f)** I ∝ µ. The nMOS carries 400/150 = **2.7×** more: **7.1 mA**. Electrons are lighter than holes, so they have a higher mobility. (3)

From: Topic 17, Topic 3

</details>
