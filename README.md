# Source Code - CO-OP Module-2 Project Report

**Project:** From Mindful Living to Algorithmic Dependence  
**Authors:** Hiya Kashyap (2210990415), Shivi (2210992333)  
**Mentor:** Dr. Rajat Takkar  
**Course:** 22CS421 — Chitkara University

## Files

| File | Purpose |
|------|---------|
| `figure_4_1_wearable_market.py` | Generates Figure 4.1 — Wearable Device Market Growth (2020-2028) |
| `figure_4_2_digital_amnesia.py` | Generates Figure 4.2 — Digital Amnesia Research Publication Growth |
| `figure_5_1_clinical_harm.py` | Generates Figure 5.1 — Clinical Harm and Negative Effects Prevalence |
| `figure_5_2_handwriting_typing.py` | Generates Figure 5.2 — Learning Retention: Handwriting vs Typing |
| `literature_synthesis.py` | Loads the 15-study evidence matrix and reproduces the report's headline statistics |
| `dependency_assessment.py` | Interactive CLI tool: scores a user's algorithmic-dependence risk based on report's diagnostic thresholds |

## Requirements

```
python >= 3.8
matplotlib
numpy
```

Install:
```
pip install matplotlib numpy
```

## Running

Generate all four figures:
```
python figure_4_1_wearable_market.py
python figure_4_2_digital_amnesia.py
python figure_5_1_clinical_harm.py
python figure_5_2_handwriting_typing.py
```


```
# Algorithmic Dependence — Interactive Self-Assessment

A web-based companion to the research paper *"From Mindful Living to Algorithmic Dependence: Psychological Consequences of AI-Driven Health and Wellness Applications"* by Hiya Kashyap and Shivi, supervised by Dr. Rajat Takkar, Chitkara University.

## What This Is

A single self-contained HTML page that presents a 20-question reflective self-assessment translating the diagnostic thresholds from the research paper into an interactive tool.

The assessment covers three domains:

- **Self-Tracking Behaviour** (7 questions) — fitness apps, sleep trackers, calorie counters
- **AI-Companion Reliance** (6 questions) — emotional support chatbots, parasocial AI relationships
- **Cognitive Offloading** (7 questions) — memory, navigation, attention, mental arithmetic

Users receive an overall dependence score (out of 60), a per-domain breakdown, an interpretive paragraph drawn from the research, and a set of practical recommendations calibrated to their result.

## Files in This Package

| File | Purpose |
|------|---------|
| `index.html` | The complete website — single self-contained file. Just open it in any browser. |
| `HOSTING_GUIDE.md` | Step-by-step instructions for putting the site online (Netlify, GitHub Pages, Cloudflare). |
| `README.md` | This file. |

## Technical Details

- Pure HTML, CSS, and vanilla JavaScript — no frameworks, no build tools, no dependencies.
- Single file: 39 KB uncompressed.
- External resources: only Google Fonts (Fraunces serif and Manrope sans-serif).
- No data is uploaded, stored, or shared. All scoring happens locally in the user's browser.
- Mobile-first responsive design, prints cleanly, keyboard accessible (number keys 1-4 or A/B/C/D to answer).
- Compatible with all modern browsers (Chrome, Firefox, Safari, Edge — desktop and mobile).

## Quick Test

Open `index.html` in your browser by double-clicking it. The full assessment runs locally — no internet connection or hosting needed.

## Going Live

See `HOSTING_GUIDE.md` for the three easiest ways to put the site online and get a URL you can include in your research paper.

## Citation

Kashyap, H., & Shivi. (2025). *From Mindful Living to Algorithmic Dependence: Psychological Consequences of AI-Driven Health and Wellness Applications.* Department of Computer Science and Engineering, Chitkara University, Punjab, India. CO-OP Module-2 (22CS421). Supervised by Dr. Rajat Takkar.
