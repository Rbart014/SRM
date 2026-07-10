# OpenMotor 1D Internal Ballistics Simulation

This directory contains the computational simulation files used to predict the internal ballistics and thrust curve of the F-Class (F75) solid rocket motor prior to static testing. 

The primary tool used was **OpenMotor**, an open-source 1D internal ballistics solver for experimental solid rocket motors.

## Simulation Input Parameters

The initial predictive model was built using the following theoretical and geometric parameters:

| Component | Parameter | Value |
| :--- | :--- | :--- |
| **Propellant** | Type | KNSB (Potassium Nitrate / Sorbitol) |
| **Grain Geometry** | Configuration | Single-Grain BATES |
| | Outer Diameter (OD) | 0.819 in |
| | Length | 3.94 in |
| **Nozzle Geometry** | Throat Diameter | 0.153 in |
| | Throat Length | 0.079 in |
| | Exit Diameter | 0.323 in |
| | Expansion Ratio | 4.46 |
| | Convergence Half-Angle | 25° |
| | Divergence Half-Angle | 15° |
| **Assumptions** | C-Star Efficiency | 0.90 (Conservative sub-scale estimate) |

## Predicted vs. Empirical Calibration

The files currently in this directory represent the **pre-test predictive model**. 

Upon physical static testing, a significant deviation in the burn rate was observed. The OpenMotor simulation predicted a highly progressive burn over **0.72 seconds** with a peak chamber pressure of **1233 psi**. 

Empirical testing yielded a much longer, regressive burn over **~1.40 seconds**. Post-fire hardware inspection confirmed **0.000 in of nozzle throat erosion**, isolating the predictive failure entirely to the propellant characterization within the software.

## Files in this Directory
* `F78_Predictive_Model.eng` - The simulated thrust curve data exported from OpenMotor.
* `motor_sim.omtr` - The OpenMotor project save file.
