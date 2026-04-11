# G-Class KNSB Solid Rocket Motor

**160 Ns | 57.15 mm OD | KNSB Propellant | Designed in SolidWorks | Validated in ANSYS Fluent**

A fully documented amateur G-class solid rocket motor designed from scratch — including propellant grain design, De Laval nozzle sizing, CNC-machined 6061-T6 aluminum hardware, and CFD-validated nozzle flow simulation confirming Mach 3.69 exit conditions.

---

## Overview

| Parameter | Value |
|---|---|
| Motor Class | G (max class) |
| Total Impulse | 160 Ns |
| Average Thrust | 40.0 N |
| Burn Time | 4.0 s |
| Specific Impulse (Isp) | ~130 s |
| Chamber Pressure | 690 psi / 4.757 MPa |
| Propellant | KNSB — KNO3/Sorbitol 65/35 by mass |
| Propellant Mass | 125.5 g |
| Casing OD x Length | 57.15 mm x 92 mm (6061-T6 Al) |
| Nozzle Throat Diameter | 2.87 mm |
| Nozzle Exit Diameter | 8.12 mm |
| Expansion Ratio | 8.0 |
| Exit Mach Number (CFD) | ~3.69 |
| Casing Safety Factor | 7.3x (hoop stress at 690 psi) |

---

## Repository Structure

```
g-class-knsb-motor/
├── cad/                  # SolidWorks part and assembly files
├── cfd/                  # ANSYS Fluent 2026 R1 simulation files
├── drawings/             # Engineering drawings (PDF)
├── analysis/             # Propellant calcs and nozzle sizing scripts
├── grain_mold/           # 3-part ASA grain casting mold (3D print)
├── docs/                 # Design log, references, test plan
└── README.md
```

---

## Design Process

### 1. Propellant & Performance

KNSB (potassium nitrate / sorbitol, 65/35 by mass) was selected for its low burn temperature (~1600 K), predictable burn characteristics, and safe solid-state handling. Propellant density is 1.841 g/cm3. At 690 psi chamber pressure, burn rate is approximately 4.42 mm/s.

A monolithic BATES grain was chosen for its neutral-to-progressive burn profile: 45.0 mm OD x 46.0 mm length, 9.525 mm core diameter, 17.7 mm web thickness — 125.5 g total propellant mass.

### 2. Nozzle Design

The De Laval nozzle was sized using isentropic flow relations targeting Mach 3.69 exit at 690 psi chamber pressure.

- Throat diameter: 2.87 mm (step-drilled, reamed, pin-gauge verified)
- Exit diameter: 8.12 mm | Expansion ratio: 8.0
- Converging half-angle: 60 deg | Diverging half-angle: 15 deg
- Material: High-density machinable graphite

A critical geometry conflict — screw holes at 10 mm from edge intersecting the O-ring groove — was caught during SolidWorks modeling and corrected to 5 mm, preserving the pressure seal.

### 3. Structural Design (SolidWorks 2025)

6061-T6 aluminum casing (Fy = 276 MPa), sized for 690 psi:

- Hoop stress: 38.0 MPa → safety factor 7.3x (smooth wall), ~5.5x at screw holes
- Interior stack: Nozzle 25 mm + Grain 46 mm + Closure 20 mm + 1 mm clearance = 92 mm total

Forward closure includes a 1/8" NPT center port for a 0-2000 psi pressure transducer. Engineering drawings generated for all parts, targeting JLCPCB CNC machining.

### 4. CFD Simulation (ANSYS Fluent 2026 R1)

2D axisymmetric, pressure-based, compressible solver with k-omega SST turbulence model.

Result: Confirmed De Laval flow profile — subsonic inlet → Mach ~1.0 at throat → Mach ~3.69 exit — consistent with isentropic prediction for expansion ratio 8.0.

Notable: Initial geometry import had the nozzle oriented backwards. After correcting the orientation, the simulation produced the expected shock-free supersonic expansion.

![Mach Contour](cfd/Mach_contour.png)

### 5. Grain Casting Mold

Three-part 3D-printable ASA mold for casting KNSB grains, dimensioned with KNSB shrinkage compensation. Components: base plate, support sleeve (45.6 mm ID x 55 mm OD x 60 mm), top centering cap with 4 mm vent holes.

---

## Project Status

- [x] Propellant selection and performance estimation
- [x] Nozzle design (isentropic sizing, expansion ratio 8.0)
- [x] SolidWorks CAD — casing, nozzle, forward closure, assembly
- [x] Engineering drawings — all parts
- [x] CFD simulation — nozzle flow validated (Mach ~3.69 exit)
- [x] Grain casting mold design (3-part ASA)
- [ ] JLCPCB machining order submission
- [ ] Propellant casting
- [ ] Static fire test
- [ ] DAQ system (load cell, pressure transducer, data logger)

---

## Tools

- SolidWorks 2025 — CAD and engineering drawings
- ANSYS Fluent 2026 R1 — CFD (k-omega SST, 2D axisymmetric, compressible)
- Python — nozzle sizing and propellant burn calculations

---

## References

- Nakka, R. — Solid Propellant Rocket Motor Design
- Anderson, J. D. — Modern Compressible Flow
- Sutton & Biblarz — Rocket Propulsion Elements, 8th ed.
- NFPA 1125

---

## Author

**Richardson Barthelemy**
B.S. Mechanical Engineering — FAMU-FSU College of Engineering, Class of 2029
Focus: Propulsion & Aerospace Engineering

---

> Safety Note: This project involves energetic materials. All work is conducted in accordance with applicable regulations. Propellant composition details are intentionally omitted.
