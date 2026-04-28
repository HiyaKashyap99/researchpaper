"""
figure_4_2_digital_amnesia.py
------------------------------------------------------------
Generates Figure 4.2 of the project report:
"Digital Amnesia Research Publication Growth (4x Increase)"

Plots the number of indexed academic publications on digital
amnesia from 2019 to 2023, with an annotation showing the
fourfold increase across that period.

Authors : Hiya Kashyap (2210990415), Shivi (2210992333)
Project : CO-OP Module-2, Chitkara University
"""

import matplotlib.pyplot as plt

# ---- Data (Web of Science indexed counts) -------------------------------
years  = [2019, 2020, 2021, 2022, 2023]
papers = [195,  300,  450,  620,  837]

# ---- Figure setup --------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.5))

BAR_COLOR = "#2C3E50"     # dark navy

bars = ax.bar(years, papers,
              color=BAR_COLOR,
              edgecolor="black", linewidth=1.0,
              width=0.65)

# Value labels on top of every bar
for bar, val in zip(bars, papers):
    ax.text(bar.get_x() + bar.get_width() / 2,
            val + 18, str(val),
            ha="center", fontsize=12, fontweight="bold")

# Diagonal arrow showing the 4x growth trend
ax.annotate("",
            xy=(2023, 837), xytext=(2019, 195),
            arrowprops=dict(arrowstyle="->", color="#E63946",
                            lw=2.4, mutation_scale=20))

# Callout box for "4x growth in 4 years"
ax.text(2021, 540, "4× Growth\nin 4 Years",
        ha="center", va="center",
        fontsize=12, fontweight="bold", color="#E63946",
        bbox=dict(boxstyle="round,pad=0.5",
                  facecolor="white", edgecolor="black", linewidth=1.2))

# ---- Cosmetics -----------------------------------------------------------
ax.set_title("Digital Amnesia Research Publication Growth (4× Increase)",
             fontsize=17, fontweight="bold", pad=14)
ax.set_xlabel("Year",                       fontsize=13, fontweight="bold")
ax.set_ylabel("Number of Research Papers",  fontsize=13, fontweight="bold")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
ax.set_ylim(0, 950)
ax.set_xticks(years)

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig("figure_4_2_digital_amnesia.png", dpi=300, bbox_inches="tight")
print("Saved figure_4_2_digital_amnesia.png")
