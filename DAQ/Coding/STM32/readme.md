# Rocket Motor DAQ Firmware

> Custom STM32 firmware for data acquisition on an F-class solid rocket motor static test stand.

## Overview
This project interfaces an STM32 microcontroller with an HX711 load cell amplifier to capture high-fidelity thrust data during static fires. It converts raw 24-bit ADC counts into real-time thrust measurements (Newtons) for performance analysis.

## Features
* **Precision DAQ:** Custom bit-banging C driver for the HX711 24-bit ADC.
* **Live Calibration:** Implements automated taring and applies a calibrated scale factor (`10435.78`).
* **Serial Streaming:** Transmits formatted floating-point data over UART (115200 baud) for live PC logging.

## Hardware Stack
* STM32 Microcontroller
* HX711 Load Cell Amplifier
* 2040 Aluminum Extrusion Frame
* Custom Metal Motor Retainers
