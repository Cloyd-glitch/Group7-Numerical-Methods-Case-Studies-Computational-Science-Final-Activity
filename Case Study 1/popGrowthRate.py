import matplotlib.pyplot as plt

# ── DATA ──────────────────────────────────────────────────
years = [2020, 2021, 2022, 2023, 2024]
population = [10000, 10800, 11900, 13200, 14800]

# ── STEP 1: NUMERICAL DIFFERENTIATION (Central Difference) ─
growth_years = [2021, 2022, 2023]
growth_rates = []

for i in range(1, len(years) - 1):
    rate = (population[i + 1] - population[i - 1]) / 2
    growth_rates.append(rate)

# Print derivatives table
print("=" * 35)
print("   GROWTH RATE TABLE (Central Difference)")
print("=" * 35)
print(f"{'Year':<10} {'Growth Rate (people/year)'}")
print("-" * 35)
for y, r in zip(growth_years, growth_rates):
    print(f"{y:<10} {r}")

# ── STEP 2: NUMERICAL INTEGRATION (Trapezoidal Rule) ───────
h = 1  # 1 year spacing
total = (h / 2) * (population[0] + 2*population[1] + 2*population[2] + 2*population[3] + population[4])

print("\n" + "=" * 35)
print("   TRAPEZOIDAL RULE INTEGRATION")
print("=" * 35)
print(f"Total accumulated population (2020–2024): {total} person-years")

# ── STEP 3: PREDICTION FOR 2025 ────────────────────────────
predicted_rate_2024 = 1700  # growth rate trend: +250 each year
predicted_2025 = population[-1] + predicted_rate_2024

print("\n" + "=" * 35)
print("   2025 POPULATION PREDICTION")
print("=" * 35)
print(f"Predicted growth rate (2024): {predicted_rate_2024} people/year")
print(f"Predicted population in 2025: {predicted_2025}")

# ── STEP 4: VISUALIZATION ──────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Population vs Time
ax1.plot(years, population, marker='o', color='blue', linewidth=2)
ax1.set_title('Population vs Time')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')
ax1.set_xticks(years)
ax1.grid(True)

# Plot 2: Growth Rate vs Time
ax2.bar(growth_years, growth_rates, color='orange', alpha=0.6, label='Growth Rate (bar)')
ax2.plot(growth_years, growth_rates, marker='o', color='red', linewidth=2, label='Growth Rate (line)')
ax2.set_title('Growth Rate vs Time')
ax2.set_xlabel('Year')
ax2.set_ylabel('Growth Rate (people/year)')
ax2.set_xticks(growth_years)
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('population_analysis.png')
plt.show()