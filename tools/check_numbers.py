"""Recompute the numbers used in notes/15-22, papers/ and mock/final-*.md.
Run: python3 tools/check_numbers.py   (prints every value; compare with the md files)."""
from math import exp, log, sqrt
e = 1.6e-19; VT = 0.026; ni = 1.45e10; ni2 = ni ** 2; NC = 3.2e19; NV = 1.8e19
eps0 = 8.85e-14; eSi = 11; eox = 4; EG = 1.12; chi = 4.05

def show(label, v): print(f'{label:55s} {v:.4g}')

def wmax(N, es=eSi, ni_=ni):
    return 2 * sqrt(eps0 * es * VT * log(N / ni_) / (e * N))

print('--- Topic 15 / 16 / 17 / 19')
show('T15 phiF NA=1e16', VT * log(1e16 / ni))
show('T15 M3 phiF NA=5e16', VT * log(5e16 / ni))
show('T15/2014 ND from flat band', NC * exp(-(4.259 - 4.05) / VT))
show('T16 Cox 10nm eox4', eps0 * 4 / 1e-6)
Cox = eps0 * 3.9 / 1e-6; d = wmax(1e16, 11.8, 1.5e10); Cd = eps0 * 11.8 / d
show('Ch3Q2 Cox', Cox); show('Ch3Q2 dmax cm', d); show('Ch3Q2 Cdepl', Cd); show('Ch3Q2 Cmin', Cox * Cd / (Cox + Cd))
Cmax, Cmin = 3.45e-7, 7.93e-8; Cd = Cmin * Cmax / (Cmax - Cmin)
show('Ch3Q7 tox cm', eps0 * 3.9 / Cmax); show('Ch3Q7 Cdepl', Cd); show('Ch3Q7 W cm', eps0 * 11.8 / Cd)
show('2014 Cox', 0.885e-12 / (100e-4 * 5e-4)); show('2014 tox cm', eps0 * 4 / (0.885e-12 / 5e-6))
show('2014 Wdepl (not asked)', eps0 * 11 * 5e-6 * (0.885e-12 - 0.14e-12) / (0.885e-12 * 0.14e-12))
A = 2e-4 * 5e-4; Cm = 0.5 * eps0 * 4 / 1e-6 * A; W = wmax(5e16); Cd = eps0 * 11 * A / W
show('2016 Cmax', Cm); show('2016 W', W); show('2016 Cdepl', Cd); show('2016 Cmin', Cm * Cd / (Cm + Cd))
A = 50e-4 * 4e-4; C1 = 2e-12 / A
show('T16 M3 tox', eps0 * 4 / C1); show('T16 M3 W', eps0 * 11 * A * 1.5e-12 / (2e-12 * 0.5e-12))
show('2014 Isat', 410 * 1.77e-7 * 100 / (2 * 5) * 0.09)
show('2015 Q', -(8.85e-12 * 4 / 10e-9) * (1.5 - 1 - 0.05))
k = 500 * (eps0 * 4 / 2e-6) * 10
show('T17 M3 k', k); show('T17 M3 triode', k * (2 * 0.5 - 0.125)); show('T17 M3 sat', 0.5 * k * 4)
Cq8 = 0.5 * 1e-4 / (1e3 * 0.0141); show('Ch3Q8 Cox', Cq8); show('Ch3Q8 tox', eps0 * 4 / Cq8)
print('--- Topic 21 / 22 and papers')
show('2016 pn0E', ni2 / 5e18); show('2016 pnE', ni2 / 5e18 * exp(10)); show('2016 nB', ni2 / 5e16 * exp(10))
show('2016 nB rev', ni2 / 5e16 * exp(-1 / VT)); show('2016 pC0', ni2 / 1e16); show('2016 pC rev', ni2 / 1e16 * exp(-1 / VT))
Vbi = VT * log(5e16 * 1e16 / ni2); wp = sqrt(2 * eps0 * 11 * (Vbi + 1) * 1e16 / (e * 6e16 * 5e16))
show('2016 Vbi', Vbi); show('2016 wp', wp)
IB = e * (40e-4) ** 2 * 4 * ni2 / 5e18 * exp(10) / 0.4e-4; IC = e * (50e-4) ** 2 * 20 * ni2 / 5e16 * exp(10) / (0.8e-4 - wp)
show('2016 IB', IB); show('2016 IC', IC); show('2016 beta', IC / IB)
x = exp(0.6 / VT); show('T21 M3 IC', e * 1e-5 * 10 * ni2 / 1e17 * x / 0.5e-4); show('T21 M3 IB', e * 1e-5 * 5 * ni2 / 1e19 * x / 0.5e-4)
show('2017 1f p', NV * exp(-(chi + EG - 5.035) / VT)); show('2017 1g dp', 6.11e-11 * 5e-4 / (e * 2))
nn = ((1e18 - 1e17) + sqrt((9e17) ** 2 + 4 * ni2)) / 2; show('2017/2018 n comp', nn); show('p comp', ni2 / nn)
show('2018 phip', VT * log(NV / 1e16)); show('2018 Vbi', VT * log(1e34 / ni2))
show('2018 J', e * (50 * 1e5 / 150e-7 + 20 * 1e2 / 100e-7))
show('2016 Ec-EF', VT * log(NC / 2e17)); show('2016 Ec-Ei', VT * log(NC / ni))
show('2015 Ev-EF', VT * log(3.6e18 / NV)); show('2015 NA', 11 * eps0 * 0.7 / (e * 2.06e-5 ** 2)); show('2015 Emax', e * 1e16 * 2.06e-5 / (11 * eps0))
show('2014 EF-Ev', VT * log(NV / 1e17)); show('2014 Ec-EF alt', VT * log(NC * 1e17 / ni2)); show('2014 R', 1e-2 / (e * 1e17 * 200 * 2e-4 * 0.05))

print('--- Mock Final 1')
NAi, NDs = 2e17, 5e16
p = ((NAi - NDs) + sqrt((NAi - NDs) ** 2 + 4 * ni2)) / 2; show('M1 Q1b p', p); show('M1 Q1b n', ni2 / p)
show('M1 Q1c Ec-EF', 4.25 - chi); show('M1 Q1c ND', NC * exp(-(4.25 - chi) / VT))
show('M1 Q1d E V/cm', 0.3 / 3e-4)
show('M1 Q1e phis n 1e17', chi + VT * log(NC / 1e17))
show('M1 Q1f J', e * 10 * 2e8 / 2e-4)
A = 50e-4 * 2e-4; Cox = eps0 * 4 / 5e-7; Cmax = Cox * A
W = wmax(1e17); Cdep = eps0 * 11 / W; Cmin = Cox * Cdep / (Cox + Cdep) * A
show('M1 Q2 Cox', Cox); show('M1 Q2 Cmax pF', Cmax * 1e12); show('M1 Q2 W', W); show('M1 Q2 Cmin pF', Cmin * 1e12)
show('M1 Q2 W back', eps0 * 11 * A * (Cmax - Cmin) / (Cmax * Cmin))
k = 400 * Cox * 50 / 2; show('M1 Q2 k', k); show('M1 Q2 triode', k * (1.2 * 0.5 - 0.125)); show('M1 Q2 sat', 0.5 * k * 1.2 ** 2); show('M1 Q2 gm', k * 1.2)
x = exp(0.65 / VT); show('M1 Q3 exp', x)
pE = ni2 / 1e19 * x; nB = ni2 / 1e17 * x; show('M1 Q3 pn0E', ni2 / 1e19); show("M1 Q3 p'n", pE); show('M1 Q3 np0', ni2 / 1e17); show("M1 Q3 n'p", nB)
IC = e * 1e-5 * 15 * nB / 0.5e-4; IB = e * 1e-5 * 2 * pE / 0.3e-4
show('M1 Q3 IC', IC); show('M1 Q3 IB', IB); show('M1 Q3 IE', IC + IB); show('M1 Q3 beta', IC / IB)
gm = IC / VT; show('M1 Q3 gm', gm); show('M1 Q3 Rpi', (IC / IB) / gm); Ro = 60 / IC; show('M1 Q3 Ro', Ro); show('M1 Q3 IC+5V', IC + 5 / Ro)

print('--- Mock Final 2')
show('M2 Q1b EF-Ev', VT * log(NV / 5e15)); show('M2 Q1b Ec-EF', EG - VT * log(NV / 5e15))
sig = e * 5e15 * 450; show('M2 Q1c sigma', sig); show('M2 Q1c R', 0.2 / (sig * 100e-4 * 10e-4))
show('M2 Q1d E', VT / 1e-4)
Vbi = VT * log(1e17 * 1e16 / ni2); wn = sqrt(2 * eps0 * 11 * Vbi * 1e17 / (e * 1.1e17 * 1e16)); wp = wn * 1e16 / 1e17
show('M2 Q1e Vbi', Vbi); show('M2 Q1e wn', wn); show('M2 Q1e wp', wp); show('M2 Q1e Emax', e * 1e16 * wn / (eps0 * 11))
x = exp(0.6 / VT); Jp = e * 12 * ni2 / 1e16 * x / 3e-4; Jn = e * 25 * ni2 / 1e17 * x / 2e-4
show('M2 Q1f pn edge', ni2 / 1e16 * x); show('M2 Q1f np edge', ni2 / 1e17 * x); show('M2 Q1f Jp', Jp); show('M2 Q1f Jn', Jn); show('M2 Q1f J', Jp + Jn)
show('M2 Q2 beta', 4e-3 / 20e-6); gm = 2e-3 / VT; show('M2 Q2 gm', gm); show('M2 Q2 Rpi', 200 / gm)
Ro = 50 / 4e-3; show('M2 Q2 Ro', Ro); show('M2 Q2 IC at 6V', 4e-3 + 5 / Ro)
Cox = eps0 * 4 / 8e-7; k = 150 * Cox * 20; show('M2 Q3 Cox', Cox); show('M2 Q3 k', k); show('M2 Q3 Isat', 0.5 * k * 4); show('M2 Q3 gm', k * 2)
show('M2 Q3 nMOS Isat', 0.5 * 400 * Cox * 20 * 4)

print('--- Mock Final 3')
show('M3 Q1a f(0.1)', 1 / (1 + exp(0.1 / VT))); show('M3 Q1a f(-0.1)', 1 / (1 + exp(-0.1 / VT)))
show('M3 Q1c phis p 1e15', chi + EG - VT * log(NV / 1e15))
x = exp(0.5 / VT); show('M3 Q2 exp', x)
pn = ni2 / 1e15 * x; npp = ni2 / 1e18 * x
show('M3 Q2 pn0', ni2 / 1e15); show('M3 Q2 np0', ni2 / 1e18); show("M3 Q2 p'n", pn); show("M3 Q2 n'p", npp)
Vbi = VT * log(1e18 * 1e15 / ni2); show('M3 Q2 Vbi', Vbi)
wn = sqrt(2 * eps0 * 11 * (Vbi - 0.5) * 1e18 / (e * (1e18 + 1e15) * 1e15)); show('M3 Q2 wn at 0.5V', wn)
wn0 = sqrt(2 * eps0 * 11 * (Vbi) * 1e18 / (e * (1e18 + 1e15) * 1e15)); show('M3 Q2 wn at 0V', wn0)
show('M3 Q2 Emax 0V', e * 1e15 * wn0 / (eps0 * 11))
Jp = e * 10 * pn / (5e-4 - wn); Jn = e * 30 * npp / 2e-4
show('M3 Q2 Jp', Jp); show('M3 Q2 Jn', Jn); show('M3 Q2 J', Jp + Jn)
show('M3 Q2 Jp halved', e * 10 * pn / ((5e-4) / 2 - wn))
DnB, WB, DpE, XE, NAB, NDE = 20, 0.4e-4, 3, 0.2e-4, 5e16, 1e19
beta = (DnB * NDE * XE) / (DpE * NAB * WB); show('M3 Q3 beta', beta)
A = 2e-5; x = exp(0.7 / VT); IC = e * A * DnB * ni2 / NAB * x / WB; show('M3 Q3 IC', IC); show('M3 Q3 IB', IC / beta)
show('M3 Q3 gamma', 1 / (1 + 1 / beta))
IL = 2e-9; show('M3 Q3 beta leak', (IC + IL) / (IC / beta - IL))
