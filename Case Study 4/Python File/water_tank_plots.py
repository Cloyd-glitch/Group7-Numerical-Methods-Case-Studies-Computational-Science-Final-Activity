# ============================================================
#   CASE STUDY 4: Water Tank Filling Rate Analysis
#   Visualizations — 4 separate plots
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# ── Data ────────────────────────────────────────────────────
t = [0, 2, 4, 6, 8, 10]
v = [0, 40, 110, 210, 340, 500]
h = 2

# Compute flow rates (central difference)
flow_times = []
flow_rates = []
for i in range(1, len(t) - 1):
    rate = (v[i + 1] - v[i - 1]) / (2 * h)
    flow_times.append(t[i])
    flow_rates.append(rate)

# Compute trapezoid areas
trap_areas = []
total_volume = 0
for i in range(len(t) - 1):
    area = (h / 2) * (v[i] + v[i + 1])
    trap_areas.append(area)
    total_volume += area

# Smooth curve for reference
t_fine = np.linspace(0, 10, 300)
# fit a quadratic through data for smooth line
coeffs = np.polyfit(t, v, 2)
v_fine = np.polyval(coeffs, t_fine)

BLUE   = "#1565C0"
LBLUE  = "#90CAF9"
GREEN  = "#2E7D32"
LGREEN = "#A5D6A7"
RED    = "#C62828"
LRED   = "#FFCDD2"
AMBER  = "#E65100"
LAMBER = "#FFE0B2"
GRAY   = "#455A64"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "--",
})


# ============================================================
# PLOT 1: Volume vs Time
# ============================================================
fig1, ax = plt.subplots(figsize=(9, 5.5))
fig1.patch.set_facecolor("white")

ax.plot(t_fine, v_fine, color=LBLUE, linewidth=1.5, linestyle="--", alpha=0.6, label="Quadratic fit")
ax.plot(t, v, "o-", color=BLUE, linewidth=2.5, markersize=9,
        markerfacecolor="white", markeredgewidth=2.2, label="Measured volume", zorder=5)
ax.fill_between(t, v, alpha=0.08, color=BLUE)

for i in range(len(t)):
    ax.annotate(f"{v[i]} L", (t[i], v[i]),
                textcoords="offset points", xytext=(5, 10),
                ha="left", fontsize=9, color=BLUE, fontweight="bold")

ax.set_xlabel("Time (min)", fontsize=12)
ax.set_ylabel("Volume (L)", fontsize=12)
ax.set_title("Plot 1 — Volume vs Time", fontsize=13, fontweight="bold", pad=12)
ax.set_xticks(t)
ax.set_ylim(-20, 560)
ax.legend(fontsize=10, loc="upper left")
ax.annotate("Volume grows quadratically\n(accelerating fill rate)",
            xy=(7, 340), xytext=(4.5, 430),
            arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.2),
            fontsize=9, color=GRAY,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=LBLUE, lw=0.8))

fig1.tight_layout()
fig1.savefig("/mnt/user-data/outputs/plot1_volume_vs_time.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig1)
print("Saved: plot1_volume_vs_time.png")


# ============================================================
# PLOT 2: Flow Rate vs Time
# ============================================================
fig2, ax = plt.subplots(figsize=(9, 5.5))
fig2.patch.set_facecolor("white")

bar_colors = [GREEN if r < max(flow_rates) else AMBER for r in flow_rates]
bars = ax.bar(flow_times, flow_rates, width=1.3,
              color=bar_colors, edgecolor="white", linewidth=1.2, zorder=3)

ax.plot(flow_times, flow_rates, "D--", color=RED, linewidth=1.8,
        markersize=7, markerfacecolor="white", markeredgewidth=2,
        label="Flow rate trend", zorder=5)

for bar, rate in zip(bars, flow_rates):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
            f"{rate:.1f} L/min", ha="center", va="bottom",
            fontsize=9.5, fontweight="bold", color=GRAY)

# Annotate slope
ax.annotate("", xy=(8, 72.5), xytext=(2, 27.5),
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5))
ax.text(5.2, 45, "+15 L/min\nevery 2 min", fontsize=9,
        color=RED, ha="center",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=LRED, lw=0.8))

ax.set_xlabel("Time (min)", fontsize=12)
ax.set_ylabel("Flow Rate (L/min)", fontsize=12)
ax.set_title("Plot 2 — Flow Rate vs Time", fontsize=13, fontweight="bold", pad=12)
ax.set_xticks(flow_times)
ax.set_ylim(0, 95)
ax.legend(fontsize=10)

green_patch = mpatches.Patch(color=GREEN, label="Flow rate")
amber_patch = mpatches.Patch(color=AMBER, label="Max flow rate (t=8)")
ax.legend(handles=[green_patch, amber_patch], fontsize=9, loc="upper left")

fig2.tight_layout()
fig2.savefig("/mnt/user-data/outputs/plot2_flowrate_vs_time.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig2)
print("Saved: plot2_flowrate_vs_time.png")


# ============================================================
# PLOT 3: Numerical Differentiation — Central Difference
# ============================================================
fig3, axes = plt.subplots(2, 2, figsize=(11, 8))
fig3.patch.set_facecolor("white")
fig3.suptitle("Plot 3 — Numerical Differentiation (Central Difference Formula)",
              fontsize=13, fontweight="bold", y=1.01)

central_info = [
    (2,  0,  4,  0,   110, 27.5),
    (4,  2,  6,  40,  210, 42.5),
    (6,  4,  8,  110, 340, 57.5),
    (8,  6,  10, 210, 500, 72.5),
]

for ax, (tc, tl, tr, vl, vr, rate) in zip(axes.flat, central_info):
    ax.plot(t, v, "o-", color=LBLUE, linewidth=1.8, markersize=6,
            markerfacecolor="white", markeredgewidth=1.5, alpha=0.5, zorder=2)

    # Highlight the two points used
    ax.plot([tl, tr], [vl, vr], "o", color=RED, markersize=10, zorder=5,
            label=f"V({tl})={vl}, V({tr})={vr}")

    # Draw the slope line (central difference span)
    ax.plot([tl, tr], [vl, vr], "-", color=RED, linewidth=2.2, zorder=4, label="Slope span")

    # Vertical dashed lines to x-axis
    ax.plot([tl, tl], [0, vl], "--", color=RED, linewidth=1, alpha=0.5)
    ax.plot([tr, tr], [0, vr], "--", color=RED, linewidth=1, alpha=0.5)

    # Highlight center point
    idx = t.index(tc)
    ax.plot(tc, v[idx], "s", color=BLUE, markersize=11, zorder=6, label=f"t={tc} (target)")

    # Annotation box with formula
    ax.text(0.03, 0.97,
            f"t = {tc}\nV'({tc}) = [{vr} − {vl}] / (2×{h})\n       = {vr-vl} / 4\n       = {rate} L/min",
            transform=ax.transAxes, fontsize=8.5, va="top", fontfamily="monospace",
            bbox=dict(boxstyle="round,pad=0.4", fc="#E8F5E9", ec=LGREEN, lw=0.8))

    ax.set_title(f"At t = {tc} min  →  V'({tc}) = {rate} L/min",
                 fontsize=10, fontweight="bold", color=BLUE)
    ax.set_xlabel("Time (min)", fontsize=9)
    ax.set_ylabel("Volume (L)", fontsize=9)
    ax.set_xticks(t)
    ax.set_ylim(-15, 560)
    ax.legend(fontsize=7.5, loc="lower right")

fig3.tight_layout()
fig3.savefig("/mnt/user-data/outputs/plot3_differentiation.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig3)
print("Saved: plot3_differentiation.png")


# ============================================================
# PLOT 4: Numerical Integration — Trapezoidal Rule
# ============================================================
fig4, axes = plt.subplots(2, 3, figsize=(13, 8))
fig4.patch.set_facecolor("white")
fig4.suptitle("Plot 4 — Numerical Integration (Trapezoidal Rule)",
              fontsize=13, fontweight="bold", y=1.01)

trap_colors = ["#90CAF9", "#64B5F6", "#42A5F5", "#1E88E5", "#1565C0"]
cumulative = 0

for col, (ax, i) in enumerate(zip(axes.flat[:5], range(5))):
    t0, t1 = t[i], t[i + 1]
    v0, v1 = v[i], v[i + 1]
    area = trap_areas[i]
    cumulative += area

    # Full curve faint
    ax.plot(t, v, "o-", color=LBLUE, linewidth=1.5, markersize=5,
            markerfacecolor="white", markeredgewidth=1.2, alpha=0.35, zorder=2)

    # Fill trapezoid
    ax.fill_between([t0, t1], [v0, v1], alpha=0.55, color=trap_colors[i], zorder=3,
                    label=f"Area = {area:.0f} L")
    ax.plot([t0, t1], [v0, v1], color=trap_colors[i], linewidth=2.5, zorder=4)

    # Vertical sides of trapezoid
    ax.plot([t0, t0], [0, v0], color=trap_colors[i], linewidth=1.5, zorder=4)
    ax.plot([t1, t1], [0, v1], color=trap_colors[i], linewidth=1.5, zorder=4)

    # Endpoints
    ax.plot([t0, t1], [v0, v1], "o", color=BLUE, markersize=8, zorder=5)

    # Area label inside trapezoid
    ax.text((t0 + t1) / 2, (v0 + v1) / 4 + 10,
            f"{area:.0f} L", ha="center", fontsize=10,
            fontweight="bold", color="white",
            bbox=dict(boxstyle="round,pad=0.2", fc=trap_colors[i], ec="none"))

    ax.text(0.03, 0.97,
            f"½×h×(V({t0})+V({t1}))\n= ½×{h}×({v0}+{v1})\n= {area:.0f} L",
            transform=ax.transAxes, fontsize=8, va="top", fontfamily="monospace",
            bbox=dict(boxstyle="round,pad=0.35", fc="#FFF9C4", ec="#F9A825", lw=0.8))

    ax.set_title(f"Trapezoid {i+1}: t={t0}→{t1}  |  Area = {area:.0f} L\n(Cumulative: {cumulative:.0f} L)",
                 fontsize=9.5, fontweight="bold")
    ax.set_xlabel("Time (min)", fontsize=9)
    ax.set_ylabel("Volume (L)", fontsize=9)
    ax.set_xticks(t)
    ax.set_ylim(-15, 560)

# Last panel: all trapezoids combined
ax_all = axes.flat[5]
for i in range(5):
    t0, t1 = t[i], t[i + 1]
    v0, v1 = v[i], v[i + 1]
    ax_all.fill_between([t0, t1], [v0, v1], alpha=0.5, color=trap_colors[i])
    ax_all.plot([t0, t0], [0, v0], color=trap_colors[i], linewidth=1.2)
    ax_all.plot([t1, t1], [0, v1], color=trap_colors[i], linewidth=1.2)
    ax_all.plot([t0, t1], [v0, v1], color=trap_colors[i], linewidth=2)

ax_all.plot(t, v, "o", color=BLUE, markersize=7, zorder=5)
ax_all.text(0.5, 0.55, f"Total\n∫V(t)dt\n= {total_volume:.0f} L",
            transform=ax_all.transAxes, ha="center", fontsize=13,
            fontweight="bold", color=BLUE,
            bbox=dict(boxstyle="round,pad=0.5", fc="white", ec=LBLUE, lw=1.5))
ax_all.set_title("All Trapezoids Combined\nTotal = 1,900 L", fontsize=10, fontweight="bold")
ax_all.set_xlabel("Time (min)", fontsize=9)
ax_all.set_ylabel("Volume (L)", fontsize=9)
ax_all.set_xticks(t)
ax_all.set_ylim(-15, 560)

fig4.tight_layout()
fig4.savefig("/mnt/user-data/outputs/plot4_integration.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig4)
print("Saved: plot4_integration.png")

print("\nAll 4 plots saved successfully!")
