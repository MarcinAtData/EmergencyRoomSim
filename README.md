# Emergency Room Simulation

## Overview
This project is a discrete‑event simulation of an emergency room (ER) designed to study how patient arrival rates and the number of available doctors affect waiting times.
It uses **SimPy** for the simulation engine and **Matplotlib**/**NumPy** for visual analysis.

The simulation models:
- Stochastic patient arrivals (Poisson process)
- Triage levels with different priorities and maximum waiting times
- Limited doctor capacity using priority queues
- Average waiting time as the main performance metric

The results are visualized using heatmaps, line charts, contour plots, and surface plots to help understand ER performance under different load conditions.


## Requirements
- Python 3.9+
- simpy
- numpy
- matplotlib

You can install the dependencies with:
```bash
pip install simpy numpy matplotlib
```

## How to Run
From the project root directory, run:
```bash
python simulation.py
```

This will:
- Run a grid of simulations with varying doctor counts and patient arrival rates
- Display several plots, including:
  - Heatmap of average waiting time
  - Waiting time vs. number of doctors
  - Contour and surface plots

## Customization
You can experiment with different scenarios by editing parameters in **experiment.py**, such as:
- Triage probabilities
- Treatment time distributions
- Simulation duration
- Arrival rates or doctor ranges

## Use Cases
- Healthcare operations research
- Capacity planning for emergency departments
- Teaching discrete‑event simulation concepts

## License
This project is released as open source. You are free to use, modify, and distribute it under your preferred open‑source license (e.g., MIT).

---
Contributions and suggestions are welcome!


