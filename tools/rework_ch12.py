"""One-off script used on SSD only (adds the final-exam layer to topics 1-14). Kept as an example, not reusable as is."""
"""One-off: add the final-exam layer (past finals, 'In the final', Learn by heart) to topics 1-14."""
import re
ROOT = '/home/user/SSD_Lock-In/'
SLUG = {1: '01-bond-model', 2: '02-doping-carrier-concentration', 3: '03-drift', 4: '04-diffusion', 5: '05-fermi-level',
        6: '06-workfunction', 7: '07-bands-under-field', 8: '08-contact', 9: '09-metal-semiconductor', 10: '10-pn-zero-bias',
        11: '11-pn-under-bias', 12: '12-minority-injection', 13: '13-diode-current', 14: '14-depletion-width'}

PAST = {1: '2017 Q1a, b, e · 2014 Q1a · 2018 Q1c i, ii', 2: '2018 Q2a, c · 2017 Q1h · 2015 Q1a · 2014 Q2c',
        3: '2014 Q1d · 2016 Q3a', 4: '2017 Q1d · 2015 Q1c · 2014 Q2b', 5: '2018 Q2b · 2017 Q1c, e · 2016 Q1a i, ii · 2015 Q1b, d · 2014 Q1b, c',
        6: '2017 Q1f', 7: '2018 Q1a · 2016 Q1a iii, iv', 8: 'none directly (used in 9 and 15)', 9: '2018 Q1b · 2015 Q1e',
        10: '2018 Q1b iii', 11: '2016 Q1b · 2014 Q1e i · 2018 Q1c iv', 12: '2018 Q2d i, ii · 2014 Q1e iii',
        13: '2018 Q2d iii · 2017 Q1g · 2018 Q1c iii', 14: '2015 Q1f · 2014 Q2a · 2014 Q1e ii'}

INFINAL = {
1: "Short Q1 parts, 2 marks each: \"which statements describe a hole\", \"why do electrons drift faster\", \"what is n and p in pure Si\", and yes/no checks. Easy marks if the definitions are exact.",
2: "Every final. Charge neutrality written out and defined (2018 Q2a), **compensation doping** with the quadratic (2017 Q1h for 8 marks, 2018 Q2c for 10), and the proof that p ≈ N_A (2014 Q2c for 10). The examiners take marks off if you jump to n = N_D − N_A without saying why.",
3: "Rare but quick: a resistance with a units trap (2014 Q1d) and \"why is the electron mobility higher\" (2016 Q3a, 30 words).",
4: "Explain the minus sign in the diffusion current with a sketch (2017 Q1d), the direction of the built-in field from uneven doping (2015 Q1c), and derive that field (2014 Q2b). Don't start from the drift-diffusion equation to explain the sign: it's circular.",
5: "In almost every Q1: E_F from the doping and the band diagram (2014 Q1b c, 2016 Q1a), f(E_F) = ½ and \"no electrons at E_F\" (2015 Q1b), and **prove np = nᵢ²** (2017 Q1c, 2018 Q2b).",
6: "Workfunction → doping type and density (2017 Q1f, 6 marks). The same skill sits inside every contact question (Topics 9, 15).",
7: "**Q1a two years running**: read a tilted band diagram, give ΔV, the field (size and direction), the battery polarity and the carrier flow (2018 Q1a, 20 marks; 2016 Q1a iii iv).",
8: "Not asked on its own, but the rule \"E_F lines up, electrons flow from the higher E_F\" is how you draw every contact (Topic 9) and every MOS band diagram (Topic 15).",
9: "Schottky vs ohmic with numbers: the workfunction relation, the barrier, and V_ON vs a pn diode (2018 Q1b, 10 marks); pick a metal from a table (2015 Q1e, 10 marks, with the twist that none worked).",
10: "V_bi from the formula sheet, usually inside a bigger question (2018 Q1b iii, 2016 Q2d, 2015 Q1f).",
11: "Band diagram of a biased diode consistent with the doping, and fill-in-the-blanks on who diffuses where (2016 Q1b, 10 marks); the I–V curve with the bias direction trap (2014 Q1e i).",
12: "Read an excess-carrier plot: forward or reverse, which side is more heavily doped (2018 Q2d). Minority carrier sketches with the right relative sizes (2014 Q1e iii). This is also step 1 of every BJT question.",
13: "Short-diode current from a carrier plot (2018 Q2d iii) or backwards to the excess carriers (2017 Q1g). Use the **lengths** of short layers; for a p⁺n assume J ≈ J_p.",
14: "Maximum field at the junction (2014 Q2a i, 2015 Q1f), derive ℰ(x) from Poisson (2014 Q2a iii), and relative depletion widths in a sketch (2014 Q1e ii, 2016 Q1b ii4).",
}

LEARN = {
1: """- Pure Si: **n = p = nᵢ = 1.45 × 10¹⁰ cm⁻³**.
- A **hole** is a positive **mobile** charge. Not a void, not an ion, not a positron or proton.
- At room temperature the valence band is almost completely filled with bonding electrons.
- Mobility ∝ 1/mass. Electrons are lighter than holes, so **µ_n > µ_p** and electrons drift faster.
- Heating Si breaks bonds → more carriers → lower resistance (a metal's R goes up).""",
2: """$$p + N_D^+ = n + N_A^- \\qquad n \\times p = n_i^2$$

- n-type: n ≈ N_D, p = nᵢ²/N_D. p-type: p ≈ N_A, n = nᵢ²/N_A.
- **Compensation** (both dopants): put p = nᵢ²/n into charge neutrality, solve the quadratic:

$$n = \\frac{(N_D - N_A) + \\sqrt{(N_D - N_A)^2 + 4n_i^2}}{2}$$

- You can't have more free carriers than the **net** doping.""",
6: """$$e\\phi_s = e\\chi + (E_C - E_F) \\qquad \\chi_{Si} = 4.05 \\text{ eV}$$

- E_i sits about χ + E_G/2 = **4.61 eV** below E_vac.
- φ > 4.61 eV → E_F below E_i → **p-type**. φ < 4.61 eV → **n-type**.
- The workfunction is a **material** property: it does not change on contact.""",
7: """$$\\Delta E = e\\,\\Delta V \\qquad |\\mathcal{E}| = \\frac{\\Delta V}{\\Delta x}$$

- 1 V across the bar = the bands drop **1 eV** towards the + end.
- ℰ points **uphill** (towards where the bands are higher), from + to −.
- Electrons roll **down** the bands, holes float **up**. E_G stays the same everywhere.""",
8: """- In equilibrium **E_F is flat** through everything in contact.
- Electrons flow from the side with the **higher E_F** (smaller workfunction) to the lower one.
- E_vac is continuous; the bands bend near the junction, the step equals the workfunction difference.""",
9: """| | n-type Si | p-type Si |
|---|---|---|
| Ohmic (accumulation) | φ_m < φ_s | φ_m > φ_s |
| Schottky (depletion) | φ_m > φ_s | φ_m < φ_s |

- Barrier for the Si side = |φ_m − φ_s|. A Schottky barrier is usually smaller than a pn diode's V_bi, so **V_ON(Schottky) < V_ON(pn)**.""",
10: """- V_bi (on the sheet) = the gap between the two E_F positions before contact.
- The depletion region holds **fixed ions only** (depletion approximation).
- At equilibrium |drift| = |diffusion| for each carrier: zero net current.""",
11: """- Forward bias: E_F **splits by eV**, the barrier drops to e(V_bi − V), the depletion region **narrows**. Majority carriers **diffuse** across.
- Reverse bias: barrier e(V_bi + V), depletion **widens**. The small current is minority carriers swept across, limited by their **supply**, not by the field.
- The heavily doped side injects into the lightly doped side.""",
12: """$$c = c_0\\,e^{eV/kT} \\qquad c_0 = \\frac{n_i^2}{N}$$

- Applies at the **depletion edges**. Ohmic contacts hold c₀.
- The **lightly doped** side gets the most minority carriers (biggest c₀).
- Excess = c − c₀: positive under forward bias, slightly negative under reverse.""",
13: """$$J = e\\left(D_n\\frac{\\Delta n_p}{W_p} + D_p\\frac{\\Delta p_n}{W_n}\\right) \\quad \\text{(short layers: real lengths)}$$

- Long layers: use the diffusion lengths L_n, L_p (formula sheet).
- The current is dominated by injection into the **lightly doped** side. For p⁺n: J ≈ J_p.
- Minority carriers move by **diffusion**; their drift is tiny.""",
14: """- |ℰ| is **maximum at the junction** (x = 0) and zero at the depletion edges.
- |ℰ_max| = eN_A w_p/ε = eN_D w_n/ε. One-sided junction: |ℰ_max| ≈ 2V/W.
- N_A w_p = N_D w_n: the depletion region sits mostly in the **lightly doped** side.
- ε = ε₀ε_Si = 11 × 8.85 × 10⁻¹⁴ F/cm. Don't mix cm and m.""",
}

def q(id_, tag, body, ans, src):
    return f"### {id_} ({tag})\n\n{body}\n\n<details><summary>Answer</summary>\n\n{ans}\n\nFrom: {src}\n\n</details>\n\n---\n\n"

PQ = {
1: q('F2017-1a', 'Final 2017 Q1a', 'Give **all** correct statements that describe a hole: (i) an antielectron (ii) a positive mobile charge (iii) a positive ionised atom (iv) a positron (v) a proton (vi) a void, all "in a semiconductor". [2]',
     '**(ii) only.** "A void" is wrong: an empty space cannot have a mass or a charge.', '⭐ list')
 + q('F2017-1b', 'Final 2017 Q1b', 'Why is the drift velocity of electrons higher than that of holes in intrinsic Si? [2]', 'Because the **electron mass is smaller** than the hole mass, so µ_n > µ_p and v = µℰ is bigger.', '⭐ list, Topic 3')
 + q('F2014-1a', 'Final 2014 Q1a', 'At room temperature, pure undoped Si has a certain density of electrons and holes. Give the concentration of holes and electrons. [2]', '**n = p = nᵢ = 1.45 × 10¹⁰ cm⁻³.**', '⭐ list')
 + q('F2018-1c', 'Final 2018 Q1c i, ii', 'Yes or no. [1 each]\n\n(i) At room temperature, the valence band is almost completely filled with electrons covalently bound to the atoms.\n\n(ii) If the mass of holes were smaller than the mass of electrons, the hole mobility would be larger than the electron mobility.',
     '(i) **Yes.** (ii) **Yes** (µ ∝ 1/m).', '⭐ list'),
2: q('F2018-2a', 'Final 2018 Q2a', 'Give the general charge neutrality expression for a semiconductor. Define all parameters. [4]', '**p − n + N_D − N_A = 0**\n\np: free hole concentration. n: free electron concentration. N_D: ionised donor atoms. N_A: ionised acceptor atoms.', '§2, Equation 3')
 + q('F2018-2c', 'Final 2018 Q2c', 'A p-type Si substrate is doped with 10¹⁷ cm⁻³ boron. Arsenic is implanted to give a final homogeneous doping of 10¹⁸ cm⁻³. Calculate the exact electron and hole densities in both the substrate and the implanted region. [10]',
     '**Implanted region (compensated):** −n² + (N_D − N_A)n + nᵢ² = 0 → n = [(9 × 10¹⁷) + √((9 × 10¹⁷)² + 4nᵢ²)]/2 = **9 × 10¹⁷ cm⁻³** [4]; p = nᵢ²/n = **2.34 × 10² cm⁻³** [2]\n\n**Substrate:** p = N_A = **10¹⁷ cm⁻³** [2]; n = nᵢ²/p = **2.1 × 10³ cm⁻³** [2]\n\nJust n = N_D − N_A with no working or reason: 1 mark.', '§7')
 + q('F2017-1h', 'Final 2017 Q1h', 'A Si substrate with acceptor doping 10¹⁷ cm⁻³ is implanted with a donor doping of 10¹⁸ cm⁻³. Calculate the hole and electron concentrations in the implanted region. [8]',
     'Compensation doping. Charge neutrality and mass action [4] → n² − (N_D − N_A)n − nᵢ² = 0 → **n = 9 × 10¹⁷ cm⁻³**, **p ≈ 234 cm⁻³** [4].\n\nn = 1.1 × 10¹⁸ is wrong: more electrons than the net doping is impossible.', '§7')
 + q('F2014-2c', 'Final 2014 Q2c', 'Using charge neutrality in a homogeneously doped p region and the law of mass action, show that p ≈ N_A if N_A ≫ nᵢ. [10]',
     'ρ = e(p − n − N_A) [2], neutral so p − n − N_A = 0 [1]. Mass action n = nᵢ²/p [2].\n\np² − N_A p − nᵢ² = 0 → p = [N_A + √(N_A² + 4nᵢ²)]/2 [5]. For N_A ≫ nᵢ the root ≈ N_A, so **p ≈ N_A**.\n\nDon\'t start from n = nᵢ²/N_A: that\'s what you\'re proving. N_D = 0 here.', '§5, §2')
 + q('F2015-1a', 'Final 2015 Q1a', 'Give expressions for the majority and minority carrier density as a function of donor doping N_D. [4]', '**n_n = N_D, p_n = nᵢ²/N_D.**', '§3, Equation 4'),
3: q('F2014-1d', 'Final 2014 Q1d', 'Si doped with 10¹⁷ cm⁻³ boron. µ_e = 300, µ_h = 200 cm²/Vs. Find the resistance of the block (current along y = 100 µm; cross section x = 0.5 mm by z = 2000 nm). [5]\n\n![Fig. 1.1](../img/papers/2014-fig1-1.png)',
     'p-type, so σ ≈ e p µ_p (know by heart).\n\nR = y/(σ x z) = 10⁻² ÷ (1.6 × 10⁻¹⁹ × 10¹⁷ × 200 × 0.05 × 2 × 10⁻⁴) = **312.5 Ω**\n\n"All about conversions of units."', '§6')
 + q('F2016-3a', 'Final 2016 Q3a', 'Why is the electron mobility higher than the hole mobility in Si? Use at most 30 words. [4]', 'Mobility is inversely proportional to the carrier mass. Electrons in Si have a lower mass than holes, so their mobility is higher.', '§2, Topic 1'),
4: q('F2017-1d', 'Final 2017 Q1d', 'The hole diffusion current is I_p = −eD_pA dp/dx. Explain, using graphs, the reason for the "−" sign. [4]',
     '![Official answer](../img/papers/ans-2017-q1d.png)\n\nHoles flow from high to low concentration: **+x**. Holes are positive, so the current is also **+x**. But dp/dx < 0 (negative gradient), so it must be multiplied by −1.\n\nStarting from the drift-diffusion equation is circular (the sign is already in it).', '§2')
 + q('F2015-1c', 'Final 2015 Q1c', 'The doping density N_D(x) falls linearly from N₁ at x = 0 to N₂ at x = L. Give the direction of the electric field with no bias. Explain briefly. [4]\n\n![Fig. 1.1](../img/papers/2015-fig1-1.png)',
     '![Official answer](../img/papers/ans-2015-q1c.png)\n\nElectrons **diffuse** from x = 0 to x = L. No bias = no net current, so a field must make them **drift** back. ℰ points from + to −: **+x**, towards the low doping.', '§7')
 + q('F2014-2b', 'Final 2014 Q2b', 'The n region doping varies slowly: N(x) = 10¹⁷ − 5 × 10¹⁸x. (i) Sketch n and p with no bias. [4] (ii) Derive the internal field as a function of constants and x only. [4] (iii) Draw its direction. [2]',
     '**(i)**\n\n![Official answer](../img/papers/ans-2014-q2bi.png)\n\nn(x) linear down to 0 at x = 0.02 cm. p = nᵢ²/n is **non-linear** (2100 cm⁻³ at 0, 4.2 × 10⁴ at 0.019 cm).\n\n**(ii)** J_n = 0 → ℰ = −(kT/e)(1/n)(dn/dx) = 0.026 × 5 × 10¹⁸ ÷ (10¹⁷ − 5 × 10¹⁸x) = **13 ÷ (10 − 500x) V/cm**. Charge neutral region: don\'t use Poisson.\n\n**(iii)** **+x**, so drift opposes diffusion.', '§7'),
5: q('F2014-1bc', 'Final 2014 Q1b and c', 'Si is doped with 10¹⁷ cm⁻³ boron. (b) Find E_F relative to the conduction band. [5] (c) Sketch the band diagram (E_C, E_V, E_F, E_i, E_G). [5]',
     '**(b)** E_F − E_V = kT ln(N_V/p) = 0.026 × ln(1.8 × 10¹⁹ ÷ 10¹⁷) = 0.135 eV, so **E_C − E_F = 1.12 − 0.135 = 0.985 eV**. (Or kT ln(N_C N_A/nᵢ²) = 0.969 eV.)\n\n**(c)** p-type: E_F 0.135 eV above E_V, E_i near midgap above E_F.', '§6, drawing checklist')
 + q('F2016-1a', 'Final 2016 Q1a i and ii', '(i) Sketch the band diagram (E_C, E_V, E_F, E_i, E_G) of n-type Si. [4] (ii) Give E_C, E_V and E_i relative to E_F for N_D = 2 × 10¹⁷ cm⁻³. [6]',
     '![Official answer](../img/papers/ans-2016-q1ai.png)\n\nE_C − E_F = kT ln(N_C/N_D) = **0.13 eV**. E_C − E_i = kT ln(N_C/nᵢ) = **0.56 eV**. With E_V = 0: E_C = 1.12, **E_F = 0.99**, **E_i = 0.56 eV**.\n\n![Official answer](../img/papers/ans-2016-q1aii.png)', '§6, §7')
 + q('F2015-1b', 'Final 2015 Q1b', '(i) What is the probability of finding an electron at E_F? [2] (ii) What is the density of electrons at E = E_F in an n-doped material? Explain. [4]',
     '**(i)** f(E_F) = 1/(1 + e⁰) = **½**.\n\n**(ii)** **Zero.** An electron needs an available state, and E_F is in the bandgap, which has none. (Unless degenerate doping puts E_F in the band.)', '§3')
 + q('F2018-2b', 'Final 2018 Q2b (also 2017 Q1c)', 'Prove the law of mass action n × p = nᵢ² for a semiconductor in equilibrium. [4]',
     'n × p = N_C e^((E_F − E_C)/kT) × N_V e^((E_V − E_F)/kT) = N_C N_V e^(−E_G/kT). The sheet\'s nᵢ = √(N_C N_V) e^(−E_G/2kT) squared is the same. So **np = nᵢ²**.', '§5')
 + q('F2017-1e', 'Final 2017 Q1e', '![Fig. 1.1](../img/papers/2017-fig1-1.png)\n\nThe black dots are free carriers. (i) Electrons or holes? [2] (ii) Which, A or B, has the higher potential energy? [2]',
     '**(i) Holes** (free carriers in the valence band). **(ii) B**: deeper into the valence band = higher hole energy.', '§2')
 + q('F2015-1d', 'Final 2015 Q1d', 'Draw the band diagram (E_C, E_V, E_F, E_i, E_G) of the material with the linearly falling N_D(x) (2015 Fig. 1.1). [6]',
     '![Official answer](../img/papers/ans-2015-q1d.png)\n\nn-type throughout (E_F above E_i), **E_F flat** (no bias), E_G constant, E_C moves away from E_F towards the low doping. Major error: a slope in E_F.', '§6, Topic 4 §7'),
6: q('F2017-1f', 'Final 2017 Q1f', 'The workfunction of Si is 5.035 V. Determine the doping type and the doping concentration. [6]',
     '![Official answer](../img/papers/ans-2017-q1f.png)\n\nE_i is χ + E_G/2 = 4.61 eV below E_vac. 5.035 > 4.61: E_F below E_i → **p-type**.\n\nE_F − E_V = 4.05 + 1.12 − 5.035 = 0.135 eV → p = N_V e^(−0.135/0.026) ≈ **1.0 × 10¹⁷ cm⁻³** (or 1.8 × 10¹⁷ via nᵢ; both accepted).\n\nCommon sign error: taking E_V − E_F as positive.', '⭐ list'),
7: q('F2018-1a', 'Final 2018 Q1a', '![Fig. 1.1](../img/papers/2018-fig1-1.png)\n\nN_V = N_C. Redraw and add: (i) E_G and its value [2] (ii) E_i [2] (iii) ΔV between 0 and 5 µm [4] (iv) the field vector and size [4] (v) the cross section with a battery of the right value and polarity [4] (vi) for acceptor doping, the electron and hole flow [4].',
     '![Official answer](../img/papers/ans-2018-q1a.png)\n\n(i) **E_G = 1 eV** (ii) E_i exactly **midgap** (N_C = N_V) (iii) ΔV = 0.2 eV/e = **0.2 V** (iv) **40 kV/m**, pointing to x = 0 (uphill) (v) **0.2 V, + at x = 5 µm** (vi) electrons **+x** (down the hill), holes **−x**.', '⭐ list, §1 to §3')
 + q('F2016-1a34', 'Final 2016 Q1a iii and iv', '![Fig. 1.1](../img/papers/2016-fig1-1.png)\n\nThe n-Si of Topic 5 (E_C − E_F = 0.13 eV, E_i 0.56 eV above E_V) has 0.5 V across 1 µm. (iii) Draw E_C, E_V, E_i and give E_C and E_i at x = 0 and 1 µm. [6] (iv) Add the field and its size. [4]',
     '![Official answer](../img/papers/ans-2016-q1aiii.png)\n\nPE = qV: E_C(1 µm) = E_C(0) − 0.5 eV. **E_C: 1.12 → 0.62 eV, E_i: 0.56 → 0.06 eV.**\n\n|ℰ| = 0.5 V ÷ 1 µm = **5 × 10⁵ V/m**, pointing uphill (towards x = 0).', '⭐ list'),
9: q('F2018-1b', 'Final 2018 Q1b', '(i) Relationship between φ_m and φ_pSi for a Schottky contact. [2] (ii) N_A = 10¹⁶ cm⁻³, φ_B = |E_F − E_vs| = 0.395 eV: give |φ_pSi − φ_m|. [4] (iii) Compare V_ON of this Schottky diode with an n⁺p diode with N_D 100× larger. [4]',
     '(i) **φ_m < φ_pSi.**\n\n(ii) ![Official answer](../img/papers/ans-2018-q1b.png)\n\nφ_p = E_F − E_V = 0.026 ln(1.8 × 10¹⁹/10¹⁶) = 0.195 eV → |φ_pSi − φ_m| = 0.395 − 0.195 = **0.2 eV**.\n\n(iii) V_bi(n⁺p) = 0.026 ln(10¹⁶ × 10¹⁸/nᵢ²) = **0.82 V** vs 0.2 V for the Schottky: **V_ON(Schottky) < V_ON(pn)**.', '⭐ table, Topic 10')
 + q('F2015-1e', 'Final 2015 Q1e', 'Choose a metal from Table 1.1 that gives an ohmic contact on p-Si with N_A = 3.6 × 10¹⁸ cm⁻³. χ = 4.05 eV. Prove your answer. [10]\n\n![Table 1.1](../img/papers/2015-table1-1.png)',
     '![Official answer](../img/papers/ans-2015-q1e.png)\n\nOhmic on p-type = hole accumulation → **φ_m > φ_s**.\n\nE_V − E_F = 0.026 ln(3.6 × 10¹⁸ / 1.8 × 10¹⁹) = −0.042 eV → E_C − E_F = 1.078 eV → φ_s = 4.05 + 1.078 = **5.13 eV**.\n\n**No metal in the table works** (all < 5.13 eV). W, the closest, was accepted with a critical argument.', '⭐ table'),
10: q('F2018-1biii', 'Final 2018 Q1b iii', 'Compare the on-voltage of a Schottky diode with a 0.2 eV barrier and an n⁺p diode with N_A = 10¹⁶ and N_D = 10¹⁸ cm⁻³. Justify. [4]',
      'V_bi = 0.026 × ln(10¹⁶ × 10¹⁸ ÷ (1.45 × 10¹⁰)²) = **0.82 V** ≫ 0.2 V. A smaller barrier needs less forward voltage, so **V_ON(Schottky) < V_ON(pn)**.', '§3, Equation 18'),
11: q('F2016-1b', 'Final 2016 Q1b', '![Fig. 1.2](../img/papers/2016-fig1-2.png)\n\n(i) Sketch E_C, E_V, E_F of the diode when N_A = 2N_D, consistent with the doping. [6] (ii) Fill in (forward, reverse, diffuse, drift, left-to-right, right-to-left, 1, 2, 4, larger, smaller): the diode is ___ biased; electrons ___ from ___ across the depletion region; holes ___ from ___ across the n-type region; the depletion width in the n region is ___ × ___ than in the p region. [4]',
      '**(i)**\n\n![Official answer](../img/papers/ans-2016-q1bi.png)\n\n[2] flat in the neutral regions, [3] correct E_F positions and ΔE_F, [1] non-linear in the depletion region.\n\n**(ii)** **FORWARD**; electrons **DIFFUSE** from **RIGHT TO LEFT**; holes **DIFFUSE** from **LEFT TO RIGHT**; n-side depletion **2 × LARGER**.', '§2, Topic 14')
 + q('F2014-1ei', 'Final 2014 Q1e i', '![Fig. 1.2](../img/papers/2014-fig1-2.png)\n\nSketch the I–V characteristic of this diode for 0 < |V| < 1 V. [4]',
     '![Official answer](../img/papers/ans-2014-q1ei.png)\n\nThe battery\'s + is on the **n** side, so V > 0 is **reverse** bias: current flows for V < 0. "Most graphs were flipped around the I axis."', '§1')
 + q('F2018-1civ', 'Final 2018 Q1c iv', 'Yes or no: the reverse bias current of a pn diode is limited by the electric field across the diode. [1]', '**No.** It is limited by the **supply of minority carriers** near the junction.', '⭐ list'),
12: q('F2018-2d', 'Final 2018 Q2d i and ii', '![Fig. 2.1](../img/papers/2018-fig2-1.png)\n\n(i) Forward or reverse bias? [2] (ii) Which region has the highest majority carrier concentration? Give two features of the plot that show it. [4]',
      '(i) **Forward** (positive excess: injection).\n\n(ii) The **n-region**: its depletion region is **smaller**, and its minority carrier concentration is **lower** (mass action → more majority carriers).', '⭐ list, Topic 14')
 + q('F2014-1eiii', 'Final 2014 Q1e iii', 'For the 2014 diode (N_D > N_A), add the minority carrier concentration to the cross section with the depletion widths. Relative sizes must be right; label the axes. [5]',
     '![Official answer](../img/papers/ans-2014-q1eiii.png)\n\np_n0 = nᵢ²/N_D < n_p0 = nᵢ²/N_A: fewer minority carriers on the heavily doped n side. Any bias accepted; it\'s about relative sizes.', '⭐ list'),
13: q('F2018-2diii', 'Final 2018 Q2d iii', 'For the 2018 Fig. 2.1 diode, calculate the total current density. D_n = 50, D_p = 20 cm²/s. Take the depletion regions into account. [6]\n\n![Fig. 2.1](../img/papers/2018-fig2-1.png)',
      'n side −110 to −10 nm = 100 nm (holes, Δp = 10²); p side 50 to 200 nm = 150 nm (electrons, Δn = 10⁵).\n\nJ = e(D_n Δn/X_n + D_p Δp/X_p) = 1.6 × 10⁻¹⁹ (50 × 10⁵/150 × 10⁻⁷ + 20 × 10²/100 × 10⁻⁷) = **5.33 × 10⁻⁸ A/cm²**', '⭐ formula, §5')
 + q('F2017-1g', 'Final 2017 Q1g', 'A p⁺n junction carries 6.11 × 10⁻¹¹ A/cm² forward. The p and n widths equal the diffusion lengths, L_p = 5 × 10⁻⁴ cm, L_n = 4 × 10⁻⁴ cm. D_p = 2, D_n = 3 cm²/s. Find the excess minority carrier concentration at the n-side depletion edge. State your assumption. [6]',
     '**Assume J ≈ J_p** (p⁺n). [3]\n\nΔp = J L_p/(eD_p) = 6.11 × 10⁻¹¹ × 5 × 10⁻⁴ ÷ (1.6 × 10⁻¹⁹ × 2) = **9.5 × 10⁴ cm⁻³** [3]\n\nMistakes: not using J ≈ J_p; using L_n instead of L_p.', '⭐ list, §5')
 + q('F2018-1ciii', 'Final 2018 Q1c iii', 'Yes or no: current through the depletion region of a pn diode is mainly determined by drift. [1]', '**No.** The current is set by carriers **diffusing** across (drift and diffusion nearly cancel in there).', '⭐ list'),
14: q('F2015-1f', 'Final 2015 Q1f', 'An unbiased pn junction has N_A = N_D, V_bi = 0.7 V and a p-side depletion width of 2.06 × 10⁻⁵ cm. Find the maximum absolute field. [6]',
      'N_A = N_D → w_p = √(εV_bi/(eN_A)) → N_A = εV_bi/(e w_p²) = **10¹⁶ cm⁻³**.\n\nℰ(x) = −(eN_A/ε)(x + w_p), maximum at x = 0: |ℰ| = eN_A w_p/ε = **3.4 × 10⁴ V/cm**. (Shortcut: V_bi/w_p.)\n\nCommon problems: ε = ε₀ε_r, and mixing cm and m.', '⭐ list, §3')
 + q('F2014-2a', 'Final 2014 Q2a', 'pn diode N_A = 10¹⁶, N_D = 10¹⁹ cm⁻³, unbiased.\n\n![Fig. 2.1](../img/papers/2014-fig2-1.png)\n\n(i) Where is |ℰ| maximum? [2] (ii) Write ρ(x) in the p-side depletion region. [2] (iii) Derive ℰ(x) there from Poisson, without w_n or w_p in the answer. [6]',
     '(i) **x = 0.** (ii) **ρ = −eN_A.**\n\n(iii) dℰ/dx = −eN_A/ε → ℰ = −(eN_A/ε)(x + w_p) (using ℰ(−w_p) = 0). N_D ≫ N_A → w_p = √(2εV_bi/(eN_A)):\n\n$$\\mathcal{E}(x) = -\\frac{eN_A}{\\varepsilon}\\left(x + \\sqrt{\\frac{2\\varepsilon V_{bi}}{eN_A}}\\right)$$\n\nMistakes: integrating to a number instead of a function; forgetting V = 0.', '§3, §4')
 + q('F2014-1eii', 'Final 2014 Q1e ii', 'For the 2014 diode with N_D > N_A, sketch the cross section with the depletion width in each region, with the right relative sizes. [4]',
     '![Official answer](../img/papers/ans-2014-q1eii.png)\n\nN_D > N_A → **w_n < w_p** (N_A w_p = N_D w_n). True for any bias.', '⭐ list'),
}

for n, slug in SLUG.items():
    # ---- notes
    p = ROOT + f'notes/{slug}.md'; s = open(p).read()
    lines = s.split('\n')
    assert lines[2].startswith('Tutorial questions:'), (n, lines[2])
    lines[2] = lines[2] + ' · Past finals: ' + PAST[n]
    s = '\n'.join(lines)
    anchor = 'Then click to check.\n\n---\n'
    i = s.index(anchor) + len(anchor)
    block = f"\n## 🎯 In the final\n\n{INFINAL[n]}\n\n---\n"
    if n in LEARN and '⭐ Learn by heart' not in s:
        block += f"\n## ⭐ Learn by heart from this topic\n\nNot on the formula sheet.\n\n{LEARN[n]}\n\n---\n"
    s = s[:i] + block + s[i:]
    s = s.replace('midterm', 'exam').replace('Midterm', 'Exam')
    open(p, 'w').write(s)
    # ---- questions
    p = ROOT + f'questions/{slug}.md'; s = open(p).read()
    s = s.replace('## Part A: Tutorial questions', '## Part A: Tutorial and past-final questions')
    s = s.replace('## Part B: Midterm-style questions', '## Part B: Exam-style questions').replace('midterm', 'exam').replace('Midterm', 'Exam')
    if n in PQ:
        j = s.index('## Part B:')
        s = s[:j] + PQ[n] + s[j:]
    open(p, 'w').write(s)
    print('done', n)
