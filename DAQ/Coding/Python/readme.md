# Rocket Motor Thrust Logger GUI

> PC-side data acquisition and visualization software for an F-class solid rocket motor static test stand.

## Overview
This Python application serves as the ground station interface for the custom STM32 hardware. It establishes a serial connection to the microcontroller, reads incoming thrust telemetry, logs it securely to a timestamped CSV, and automatically generates a thrust curve plot for immediate performance analysis post-burn.

## Features
* **Live Telemetry:** Real-time thrust display built with Tkinter, utilizing a dedicated background thread to prevent UI blocking during high-speed serial reads.
* **Automated Data Logging:** Captures live UART data streams (115200 baud) and safely writes to uniquely timestamped CSV files, preventing data loss between static test fires.
* **Auto-Graphing:** Automatically parses the saved CSV and generates a scaled Thrust Curve (Time vs. Newtons) using Matplotlib immediately upon test completion.

## Technical Stack
* **Language:** Python 3
* **Libraries:** `tkinter` (GUI), `pyserial` (Hardware Comm), `matplotlib` (Data Visualization), `threading`, `csv`
* **Hardware Integration:** Designed to interface directly with STM32 UART outputs processing HX711 load cell data.
