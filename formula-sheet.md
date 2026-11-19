# Formula sheet

This is the **Constants** and **Formulae** pages from the past finals (2014 to 2018).

Every past final has the same two pages.

Your final will almost certainly give you the same sheet.

**You look these up. You don't memorise them.**

Except the ones in the next section.

---

## Learn by heart (NOT on the sheet)

In topic order. Each one links to the notes where it is explained.

<br>

**Law of mass action** (Topic 1)

$$n \times p = n_i^2$$

Asked as a proof in 2017 Q1c and 2018 Q2b. See [Topic 1, §5](notes/01-bond-model.md) and [Topic 5](notes/05-fermi-level.md).

<br>

**Charge neutrality** (Topic 2)

$$p + N_D^+ = n + N_A^-$$

Asked in 2018 Q2a, 2014 Q2c, and used for compensation doping (2017 Q1h, 2018 Q2c). See [Topic 2, §2](notes/02-doping-carrier-concentration.md).

<br>

**Drift velocity** (Topic 3)

$$v = \mu E$$

See [Topic 3, §3](notes/03-drift.md).

<br>

**Conductivity, resistivity, resistance** (Topic 3). Convert L and A to cm first.

$$\sigma = e\,(n\,\mu_n + p\,\mu_p) \qquad \rho = \frac{1}{\sigma} \qquad R = \frac{L}{\sigma A}$$

Asked in 2014 Q1d. See [Topic 3, §6](notes/03-drift.md).

<br>

**Built-in field from uneven doping** (Topic 4). Also learn how to derive it.

$$E = -\frac{kT}{e}\,\frac{1}{n}\,\frac{dn}{dx}$$

Set $J_n = 0$, rearrange for $E$, then use the Einstein relation. E points towards low doping. Asked in 2014 Q2b and 2015 Q1c. See [Topic 4, §7](notes/04-diffusion.md).

<br>

**Intrinsic level** (Topic 5)

$$E_i \approx \text{midgap} \qquad n = n_i\,e^{(E_F - E_i)/kT} \qquad p = n_i\,e^{(E_i - E_F)/kT}$$

See [Topic 5, §7](notes/05-fermi-level.md).

<br>

**Workfunction of a semiconductor** (Topic 6)

$$e\phi_s = e\chi + (E_C - E_F)$$

χ = 4.05 eV for Si. It is on the 2017 sheet but not on the others, so know it. Asked in 2014 Q3b, 2015 Q1e, 2017 Q1f, 2018 Q1b. See [Topic 6](notes/06-workfunction.md).

<br>

**Potential energy = charge × voltage** (Topic 7)

$$\Delta E = e\,\Delta V \qquad |E| = \frac{\Delta V}{\Delta x}$$

Bands drop by 1 eV for every 1 V. Asked in 2016 Q1a and 2018 Q1a. See [Topic 7](notes/07-bands-under-field.md).

<br>

**Ohmic or Schottky** (Topic 9)

| | n-type Si | p-type Si |
|---|---|---|
| Ohmic | φ_m < φ_s | φ_m > φ_s |
| Schottky | φ_m > φ_s | φ_m < φ_s |

See [Topic 9](notes/09-metal-semiconductor.md).

<br>

**Diode current with short layers** (Topic 13). Lengths, not diffusion lengths, when the layer is short.

$$J = e\left(D_n \frac{\Delta n_p}{W_p} + D_p \frac{\Delta p_n}{W_n}\right)$$

Asked in 2017 Q1g and 2018 Q2d. See [Topic 13](notes/13-diode-current.md).

<br>

**MOS capacitor** (Topics 15 and 16)

$$C_{ox} = \frac{\varepsilon_0\,\varepsilon_{ox}}{t_{ox}} \qquad C_{max} = C_{ox}\,WL \qquad \frac{1}{C_{min}} = \frac{1}{C_{ox}} + \frac{d_{max}}{\varepsilon_0\varepsilon_{Si}}$$

**Threshold:** $V_{GS} = V_{th}$ when the electron density at the surface equals the hole density in the bulk (nMOS). See [Topic 15](notes/15-mos-capacitor.md) and [Topic 16](notes/16-mos-cv.md).

<br>

**Inversion charge** (Topic 17)

$$Q_n(x) = -C_{ox}\,\big(V_{GS} - V_{th} - V(x)\big)$$

See [Topic 17](notes/17-mosfet-current.md).

<br>

**MOSFET saturation** (Topic 17). Put $V_{DS} = V_{GS} - V_{th}$ into the sheet's I_DS.

$$I_{DS}^{sat} = \frac{\mu C_{ox} W}{2L}(V_{GS} - V_{th})^2$$

See [Topic 17](notes/17-mosfet-current.md).

<br>

**Transconductance and output conductance** (Topics 19 and 22)

$$g_m = \frac{\partial I_{out}}{\partial V_{in}} \qquad g_o = \frac{1}{R_o} = \frac{\partial I_{out}}{\partial V_{out}}$$

$$\text{MOSFET sat: } g_m = \frac{\mu C_{ox} W}{L}(V_{GS} - V_{th}) \qquad \text{BJT: } g_m = \frac{I_C}{V_T},\; R_\pi = \frac{\beta}{g_m},\; R_o = \frac{V_A}{I_C}$$

See [Topic 19](notes/19-mosfet-small-signal.md) and [Topic 22](notes/22-bjt-small-signal.md).

<br>

**BJT** (Topics 20 and 21)

$$I_E = I_B + I_C \qquad \beta = \frac{I_C}{I_B} \qquad \gamma = \frac{I_C}{I_E}$$

Short pnp in forward active mode:

$$I_C \approx \frac{eAD_p\,p_{n0}}{W_B}e^{eV_{EB}/kT} \qquad I_B \approx \frac{eAD_n\,n_{p0}}{X_E}e^{eV_{EB}/kT} \qquad \beta \approx \frac{D_p\,N_{AE}\,X_E}{D_n\,N_{DB}\,W_B}$$

See [Topic 21](notes/21-bjt-currents.md).

---

## Constants

As printed on the past finals.

| Symbol | What it is | Value |
|---|---|---|
| $\varepsilon_0$ | permittivity of free space | 8.85 × 10⁻¹² F/m (= 8.85 × 10⁻¹⁴ F/cm) |
| $\mu_0$ | permeability of free space | 4π × 10⁻⁷ H/m |
| $n_i$ | carriers in pure Si, 300 K | 1.45 × 10¹⁰ cm⁻³ |
| $\varepsilon_{Si}$ | dielectric constant of Si | 11 |
| $\varepsilon_{ox}$ | dielectric constant of SiO₂ | 4 |
| $V_T = kT/e$ | thermal voltage, 300 K | 0.026 V |
| $e$ | charge of an electron | 1.6 × 10⁻¹⁹ C |
| $h$ | Planck's constant | 6.63 × 10⁻³⁴ Js |
| $E_G$ | bandgap of Si, 300 K | 1.12 eV |
| $\chi$ | electron affinity of Si (2017 sheet only) | 4.05 eV |
| $N_C$ | effective density of states, conduction band | 3.2 × 10¹⁹ cm⁻³ |
| $N_V$ | effective density of states, valence band | 1.8 × 10¹⁹ cm⁻³ |

**⚠️ Constant traps:**
- The Ch3 tutorial uses ε_Si = 11.8 and ε_ox = 3.9. The booklet uses 12.0 and 4.0. **In the exam, use whatever the paper gives** (11 and 4 on every past final).
- ε₀ is in F/m. Most of the course works in cm, so use **8.85 × 10⁻¹⁴ F/cm**.
- nᵢ² = 2.1 × 10²⁰ cm⁻⁶.

---

## Formulae (on the sheet)

In topic order. Each one gets explained in the topic where we first use it.

<br>

**Schrödinger's equation in 1D** (2014 to 2016 sheets only; never asked)

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi$$

<br>

**Drift and diffusion current densities** (Topics 3 and 4)

$$J_n = e\mu_n n E + eD_n \frac{dn}{dx}$$

$$J_p = e\mu_p p E - eD_p \frac{dp}{dx}$$

<br>

**Einstein relation** (Topic 4)

$$D = \frac{kT}{e}\,\mu$$

<br>

**Poisson equation in 1D** (Topics 4 and 14)

$$\frac{dE}{dx} = \frac{\rho(x)}{\varepsilon}$$

<br>

**Fermi distribution** (Topic 5)

$$f(E) = \frac{1}{1 + e^{(E - E_F)/kT}}$$

<br>

**Intrinsic carrier concentration** (Topic 5)

$$n_i = \sqrt{N_C N_V}\; e^{-E_G / 2kT}$$

<br>

**Electron and hole concentration** (Topic 5)

$$n = N_C\, e^{-(E_C - E_F)/kT} \qquad p = N_V\, e^{(E_V - E_F)/kT}$$

<br>

**Built-in voltage** (Topic 10)

$$V_{bi} = \frac{kT}{e}\ln\left(\frac{N_A N_D}{n_i^2}\right)$$

<br>

**Minority carrier injection under bias V** (Topics 12 and 21). $c = p_n$ or $n_p$, $c_0$ = bulk minority carrier concentration.

$$c = c_0\, e^{eV/kT}$$

<br>

**Current densities for a pn junction with lengths L_n and L_p** (Topic 13)

$$J_n = \frac{eD_n n_{p0}}{L_n}\left(e^{eV/kT} - 1\right) \qquad J_p = \frac{eD_p p_{n0}}{L_p}\left(e^{eV/kT} - 1\right)$$

<br>

**Depletion widths under bias V** (Topic 14)

$$w_n = \left[\frac{2\varepsilon (V_{bi} - V) N_A}{e (N_A + N_D) N_D}\right]^{1/2} \qquad w_p = \left[\frac{2\varepsilon (V_{bi} - V) N_D}{e (N_A + N_D) N_A}\right]^{1/2}$$

<br>

**Maximum depletion width** (Topic 16, MOS capacitor at threshold)

$$W_{depl}^{max} = 2\left[\frac{\varepsilon\,kT\,\ln(N_{sub}/n_i)}{e^2\,N_{sub}}\right]^{1/2}$$

With kT in joules. Or, with kT/e = 0.026 V: $W = 2\left[\frac{\varepsilon\,(kT/e)\ln(N/n_i)}{e\,N}\right]^{1/2}$. (The 2014 sheet prints $eN$ instead of $e^2N$ for this reason.)

<br>

**Current in a MOSFET** (Topic 17). Valid for $V_{DS} \le V_{GS} - V_{th}$.

$$I_{DS} = \frac{\mu C_{ox} W}{L}\left((V_{GS} - V_{th})V_{DS} - \frac{V_{DS}^2}{2}\right)$$
