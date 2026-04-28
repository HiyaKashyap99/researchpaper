"""
figure_5_2_handwriting_typing.py
------------------------------------------------------------
Generates Figure 5.2 of the project report:
"Learning Retention: Handwriting vs Typing"

Grouped bar chart comparing two metrics across two note-taking
modalities:
    - Retention (% of material recalled after delay)
    - Words per minute (scaled by 1/10 to share the y-axis)

Authors : Hiya Kashyap (2210990415), Shivi (2210992333)
Project : CO-OP Module-2, Chitkara University
"""

import numpy as np
import matplotlib.pyplot as plt

# ---- Data ----------------------------------------------------------------
modalities = ["Handwriting", "Typing"]
retention  = [100, 66]      # percentage
words_per  = [39,  55]      # WPM divided by 10 for y-axis sharing

# ---- Figure setup --------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.5))

x     = np.arange(len(modalities))
width = 0.35

bar1 = ax.bar(x - width / 2, retention, width,
              label="Retention (%)",
              color="#2A9D8F",
              edgecolor="black", linewidth=1.0)

bar2 = ax.bar(x + width / 2, words_per, width,
              label="Words (÷10)",
              color="#E76F51",
              edgecolor="black", linewidth=1.0)

# Value labels
for bar, val in zip(bar1, retention):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
            str(val), ha="center", fontsize=12, fontweight="bold")

for bar, val in zip(bar2, words_per):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
            str(val), ha="center", fontsize=12, fontweight="bold")

# ---- Cosmetics -----------------------------------------------------------
ax.set_title("Learning Retention: Handwriting vs Typing",
             fontsize=17, fontweight="bold", pad=14)
ax.set_ylabel("Value", fontsize=13, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(modalities, fontsize=13, fontweight="bold")
ax.set_ylim(0, 115)
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
ax.legend(loc="upper right", fontsize=12, frameon=True, edgecolor="black")

# Caption beneath the axis
fig.text(0.5, 0.005,
         "34% better retention with handwriting",
         ha="center", fontsize=11, style="italic")

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

plt.tight_layout(rect=(0, 0.04, 1, 1))
plt.savefig("figure_5_2_handwriting_typing.png", dpi=300, bbox_inches="tight")
print("Saved figure_5_2_handwriting_typing.png")
