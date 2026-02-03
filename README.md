# Spacecraft Systems – Micro:bit V2 Project

This repository contains my solutions to a 1st year coursework assignment on physical computing and programming at **Northumbria University**.

## Overview  
This group project simulates a **Spacecraft Systems Monitor** using **Microsoft Micro:bit V2** microcontrollers. Inspired by real spacecraft subsystems, it visualizes and manages mock sensor data for key operational areas including **Life Support**, **Power Systems**, and **Navigation**.  

The project demonstrates an integration of hardware inputs, real-time data display, and inter-device communication. It provides a hands-on introduction to embedded systems programming, teamwork, and modular software design.  

---

## Features  

### Life Support  
- Measures and displays simulated **O₂ and CO₂ levels**.  
- Monitors **cabin pressure** from a sensor or predefined input values.  
- Alerts when readings fall outside safe thresholds (LED or sound indicator).  

### Power Systems  
- Displays **battery percentage** over time.  
- Tracks **solar input** (light sensor) and **power consumption**.  
- Adjusts energy balance simulation dynamically.  

### Navigation  
- Shows spacecraft **heading, speed, and altitude** on the Micro:bit LED matrix.  
- Uses input buttons or sensors to control simulated direction and thrust.  
- Logs navigation data for testing and presentation purposes.  

---

## Technical Details  

- **Hardware:** Micro:bit V2 (x2 or more for subsystem separation)  
- **Language:** MicroPython  
- **Tools:** Mu Editor / Visual Studio Code with the Micro:bit extension  
- **Communication:** Radio module used to send sensor data between subsystem Micro:bits  
- **Inputs/Outputs:** Built-in accelerometer, compass, light sensor, and LEDs  

**Example setup:**  
- Micro:bit 1 → Life Support + display  
- Micro:bit 2 → Power Systems  
- Micro:bit 3 → Navigation  

---

## How It Works  

1. Each subsystem collects or simulates data.  
2. Data is transmitted using **radio communication** between Micro:bits.  
3. A main controller module displays all system statuses on the LED array or serial monitor.  

```python
# Example: broadcasting O2 level data
from microbit import *
import radio

radio.on()

while True:
    o2_level = 97  # example simulated value
    radio.send(f"O2:{o2_level}")
    sleep(1000)
