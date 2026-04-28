"""
figure_4_1_wearable_market.py
------------------------------------------------------------
Generates Figure 4.1 of the project report:
"Wearable Device Market Growth (2020 - 2028)"

Plots projected global wearable health-tracker market value
in billion USD across the period 2020 to 2028.

Authors : Hiya Kashyap (2210990415), Shivi (2210992333)
Project : CO-OP Module-2, Chitkara University
Mentor  : Dr. Rajat Takkar
Course  : 22CS421
"""

import matplotlib.pyplot as plt
import numpy as np

# ---- Data ----------------------------------------------------------------
# Source: industry reports synthesised in Section 4.2 of the report.
years  = np.array([2020, 2022, 2024, 2026, 2028])
values = np.array([36.34, 58.0, 80.0, 97.0, 114.36])   # billion USD

# ---- Figure setup --------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.5))

LINE_COLOR = "#1F3B6B"     # deep navy
FILL_COLOR = "#A8C0E0"     # ice-blue area

# Filled area below the line
ax.fill_between(years, values, alpha=0.35, color=FILL_COLOR)

# Trend line + markers
ax.plot(years, values,
        color=LINE_COLOR, linewidth=3,
        marker="o", markersize=11,
        markerfacecolor=LINE_COLOR,
        markeredgecolor="black")

# Data labels
for x, y in zip(years, values):
    ax.annotate(f"${y}B",
                xy=(x, y), xytext=(0, 14),
                textcoords="offset points",
                ha="center", fontsize=12, fontweight="bold")

# ---- Cosmetics -----------------------------------------------------------
ax.set_title("Wearable Device Market Growth (2020-2028)",
             fontsize=17, fontweight="bold", pad=14)
ax.set_xlabel("Year",                  fontsize=13, fontweight="bold")
ax.set_ylabel("Market Value (Billion USD)", fontsize=13, fontweight="bold")
ax.grid(True, axis="both", linestyle="--", alpha=0.5)
ax.set_ylim(0, 130)
ax.set_xticks(years)

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig("figure_4_1_wearable_market.png", dpi=300, bbox_inches="tight")
print("Saved figure_4_1_wearable_market.png")
