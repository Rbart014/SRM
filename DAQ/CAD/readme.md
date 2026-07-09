# Hardware Architecture: Static Test Stand

> Structural design and material specifications for the solid rocket motor static testing platform.

## Overview
The static test stand is engineered to safely secure the rocket motor during ignition and transfer the generated thrust linearly into the load cell for data acquisition. The physical structure balances modularity, rapid prototyping, and thermal resilience.

## Structural Components
* **Frame:** The core skeleton is constructed from **2040 aluminum extrusion**. This provides a rigid, modular backbone that resists bending moments during high-impulse static fires while allowing for easy adjustments to sensor placement.
* **Base & Mounts:** The primary base components and non-critical mounting brackets are 3D printed in **PETG**, chosen for its impact resistance and durability compared to standard PLA.
* **Motor Retention System:** The actual brackets holding the rocket motor are made of petg. They were able to withstand the heat as they never directly touched the rocket, only the screws that were holding the font closure and nozzle in place.

## Sensor Integration
The frame is specifically dimensioned to house the HX711 load cell assembly in direct axial alignment with the motor thrust vector, minimizing off-axis sheer forces and ensuring clean data transmission to the STM32 DAQ system.
