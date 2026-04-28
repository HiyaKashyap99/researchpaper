"""
figure_5_1_clinical_harm.py
------------------------------------------------------------
Generates Figure 5.1 of the project report:
"Clinical Harm and Negative Effects Prevalence"

Multi-coloured bar chart summarising the prevalence of five
clinically documented negative effects of AI-driven health
and wellness applications.

Authors : Hiya Kashyap (2210990415), Shivi (2210992333)
Project : CO-OP Module-2, Chitkara University
"""

import matplotlib.pyplot as plt

# ---- Data ----------------------------------------------------------------
# Each entry corresponds to a row in Table 5.3 / VIII of the source paper.
categories = [
    "Orthosomnia\n(trackers)",
    "ED Patients\nUsing Apps",
    "Apps Worsen\nED",
    "AI Users\nHarmed",
    "Can't Remember\nKids' Numbers",
]

values = [2, 75, 73, 9, 71]                       # percentages
colors = ["#C0392B",   # crimson
          "#E67E22",   # orange
          "#F4B942",   # mustard
          "#F0E5C5",   # pale sand
          "#A02E2E"]   # deep red

# ---- Figure setup --------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.5))

bars = ax.bar(categories, values,
              color=colors,
              edgecolor="black", linewidth=1.0,
              width=0.65)

# Value labels on top of each bar
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2,
            val + 1.8, f"{val}%",
            ha="center", fontsize=12, fontweight="bold")

# ---- Cosmetics -----------------------------------------------------------
ax.set_title("Clinical Harm and Negative Effects Prevalence",
             fontsize=17, fontweight="bold", pad=14)
ax.set_ylabel("Percentage (%)", fontsize=13, fontweight="bold")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
ax.set_ylim(0, 85)
plt.xticks(fontsize=11)

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig("figure_5_1_clinical_harm.png", dpi=300, bbox_inches="tight")
print("Saved figure_5_1_clinical_harm.png")
