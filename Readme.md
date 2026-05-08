# 📊 YetAnotherDashboardsRepo

> *Because the world clearly needed one more dashboard repository — but this time, all 15 Python frameworks under one roof.*

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)
![Frameworks](https://img.shields.io/badge/Frameworks-15-6366f1?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)

---

## 🧭 What Is This?

A hands-on **comparative playground** for Python dashboard and data app frameworks. Each folder contains self-contained examples built with the same conceptual goals — so you can see exactly how each framework approaches interactivity, layout, and deployment without switching mental models.

Whether you're evaluating frameworks for a new analytics product, a data science portfolio, or an internal audit tool, this repo gives you working code side-by-side.

---

## 📁 Repository Structure

```
YetAnotherDashboardsRepo/
│
├── altair/        # Declarative statistical visualization (Vega-Altair)
├── bokeh/         # Interactive browser-based plotting
├── dash/          # Production-grade web apps (Plotly Dash)
├── fastHTML/      # Lightweight HTML-first Python web apps
├── gradio/        # ML model UIs and rapid prototyping
├── mercury/       # Turn Jupyter notebooks into shareable web apps
├── mesop/         # Google's component-based Python UI framework
├── panel/         # HoloViz panel for notebook-to-dashboard pipelines
├── rio/           # Reactive Python UI framework (no HTML/CSS needed)
├── shiny/         # Shiny for Python — reactive web apps
├── streamlit/     # The quick-deploy data app standard
├── taipy/         # Full-stack Python for data pipelines + dashboards
├── toga/          # Native desktop GUIs with Python
├── voila/         # Convert Jupyter notebooks to standalone web apps
└── webview/       # Wrap Python UIs in a native desktop webview
```

---

## 🔍 Framework Comparison at a Glance

| Framework | Best For | Interactivity | Deployment | Learning Curve |
|-----------|----------|:-------------:|:----------:|:--------------:|
| **Streamlit** | Rapid data apps | ✅ High | Cloud / Docker | 🟢 Low |
| **Dash** | Production dashboards | ✅ High | Any server | 🟡 Medium |
| **Gradio** | ML model demos | ✅ High | HuggingFace / Docker | 🟢 Low |
| **Panel** | Notebook-to-app pipelines | ✅ High | Bokeh server | 🟡 Medium |
| **Bokeh** | Custom interactive plots | ✅ High | Bokeh server | 🟡 Medium |
| **Altair** | Statistical visualization | 🔶 Medium | Static HTML | 🟢 Low |
| **Voilà** | Jupyter → web app | 🔶 Medium | Jupyter server | 🟢 Low |
| **Mercury** | Notebook sharing | 🔶 Medium | Cloud | 🟢 Low |
| **Shiny** | Reactive web apps | ✅ High | Posit Connect | 🟡 Medium |
| **FastHTML** | Lightweight web UIs | ✅ High | Any ASGI server | 🟡 Medium |
| **Taipy** | Pipelines + dashboards | ✅ High | Taipy Cloud | 🔴 High |
| **Mesop** | Google-style component UIs | ✅ High | Cloud Run | 🟡 Medium |
| **Rio** | Reactive Python-only UIs | ✅ High | Rio Cloud | 🟡 Medium |
| **Toga** | Native desktop GUIs | 🔶 Medium | Desktop binary | 🔴 High |
| **Webview** | Desktop webview wrapper | ✅ High | Desktop binary | 🟡 Medium |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Recommended: use a virtual environment per framework folder

```bash
git clone https://github.com/alketcecaj12/YetAnotherDashboardsRepo.git
cd YetAnotherDashboardsRepo
```

### Running a specific framework example

Navigate into any framework folder and install its requirements, then run:

```bash
# Streamlit example
cd streamlit
pip install streamlit
streamlit run app.py

# Dash example
cd dash
pip install dash pandas plotly
python app.py

# Gradio example
cd gradio
pip install gradio
python app.py
```

> 💡 Each folder is self-contained. Check individual folder READMEs (where available) for framework-specific setup notes.

---

## 🧪 Use Cases Covered

The examples in this repo demonstrate common patterns relevant to data scientists, analysts, and ML engineers:

- **KPI dashboards** — summary metrics, filters, date pickers
- **Exploratory data analysis** — scatter plots, histograms, correlation matrices
- **Model monitoring** — prediction distributions, drift indicators
- **Tabular data apps** — filterable/sortable tables, downloadable reports
- **ML demos** — model inference interfaces (via Gradio and Streamlit)

---

## 🧩 When to Pick Which Framework

| Situation | Recommended Framework |
|-----------|----------------------|
| Internal analyst tool, fast iteration | Streamlit |
| Client-facing production dashboard | Dash |
| Sharing an ML model with non-technical users | Gradio |
| Already living in Jupyter notebooks | Panel or Voilà |
| Need a native desktop app | Toga or Webview |
| Full pipeline orchestration + UI | Taipy |
| Pure Python UI without HTML/CSS | Rio or Mesop |

---

## 🗂️ Tech Stack

- **Language:** Python 3.9+
- **Notebook format:** Jupyter (`.ipynb`)
- **Visualization cores:** Plotly, Bokeh, Vega-Altair, Matplotlib
- **Data layer:** pandas, NumPy (synthetic datasets throughout)

---

## 🤝 Contributing

Contributions are welcome! If you have an example for a framework not yet covered, or want to improve an existing one:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-framework-example`
3. Add your example inside the appropriate framework folder
4. Submit a pull request with a short description of what was added

Please keep examples self-contained and dependency lists minimal.

---

## 📬 Author

**Alket Cecaj** — Data Scientist & Quantitative Analyst  
[GitHub](https://github.com/alketcecaj12) · Copenhagen, Denmark

---

*Yes, yet another dashboards repo. But now you have 15 frameworks in one place — and a comparison table.*
