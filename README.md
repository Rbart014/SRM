# F-Class Solid Rocket Motor Static Characterization

**58.1 Ns | 25 mm OD | Single-Grain BATES | Designed in OpenMotor | Custom STM32 DAQ**

A fully documented amateur F-class solid rocket motor static fire test designed to build a complete engineering validation loop. This project includes 1D computational internal ballistics modeling, custom test stand fabrication, embedded C data acquisition development, and empirical thrust curve analysis for simulation calibration.

---

## Overview

| Parameter | Value |
|---|---|
| Motor Class | F (F75) |
| Total Impulse | 58.14 Ns (Actual) / 58.88 Ns (Predicted) |
| Peak Thrust | 93.07 N (Actual) / 134.67 N (Predicted) |
| Burn Time | ~1.40 s (Actual) / 0.72 s (Predicted) |
| Chamber Pressure | 8.24 MPa (Predicted) |
| Propellant Grain | Single-grain BATES (20.8 mm OD) |
| Propellant Length | 100 mm |
| Casing OD | 25 mm |
| Nozzle Throat Diameter | 3.89 mm |
| Nozzle Throat Length | 2.00 mm |
| Nozzle Exit Diameter | 8.20 mm |
| Expansion Ratio | 4.46 |
| DAQ Hardware | STM32 Microcontroller + HX711 |
| Test Stand Frame | 2040 Aluminum Extrusion |

---

## Repository Structure

```text
f-class-static-test/
├── simulation/           # OpenMotor 1D ballistics project files
├── DAQ/             # Custom C drivers for STM32 and HX711
├── test_data/            # Raw load cell CSVs from static firings
├── Cad/             # CAD files for custom metal motor mounts
├── images/               # Thrust curves, stand photos, and diagrams
└── README.md
