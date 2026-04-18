import matplotlib.pyplot as plt
import numpy as np

# Data from our previous calculations
time = [0, 2, 4, 6, 8, 10]
energy = [0, 1.5, 3.5, 6, 9, 13]
# Including the endpoint estimates for a complete graph
power = [0.75, 0.875, 1.125, 1.375, 1.75, 2.0]

plt.figure(figsize=(12, 5))

# Plot 1: Energy vs Time
plt.subplot(1, 2, 1)
plt.plot(time, energy, 'b-o', linewidth=2, label='Energy (kWh)')
plt.title('Cumulative Energy Consumption')
plt.xlabel('Time (hours)')
plt.ylabel('Energy (kWh)')
plt.grid(True, linestyle='--')
plt.legend()

# Plot 2: Power vs Time
plt.subplot(1, 2, 2)
plt.plot(time, power, 'r-s', linewidth=2, label='Power (kW)')
plt.title('Instantaneous Power Usage')
plt.xlabel('Time (hours)')
plt.ylabel('Power (kW)')
plt.grid(True, linestyle='--')
plt.legend()

plt.tight_layout()
plt.show()