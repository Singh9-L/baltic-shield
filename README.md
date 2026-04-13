# 🛡️ Baltic Shield v5

### Privacy-First Multi-Agent LLM Platform for Propaganda Detection & Societal Impact Simulation

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE) [![Python 3.11+](https://img.shields.io/badge/Python-3.11+-green.svg)](https://python.org) [![Ollama](https://img.shields.io/badge/Runtime-Ollama_(Local)-orange.svg)](https://ollama.ai) [![GDPR](https://img.shields.io/badge/GDPR-Compliant-brightgreen.svg)](#privacy) [![Tests](https://img.shields.io/badge/Tests-7%2F7_passing-brightgreen.svg)](tests/)

> **M.Sc. Thesis** — Vilnius University, 2026 | Author: Davinder Singh | Supervisor: Prof. Darius Plikynas
> Integrates: [ATSPARA](https://atspara.mf.vu.lt) (National LT) · [FERMI](https://www.fermi-project.eu) (EU 101073980) · [VIGILANT](https://vigilantproject.eu) (EU 101073921)

## ⚡ One-Click Install & Run

```bash
git clone https://github.com/Singh9-L/baltic-shield.git
cd baltic-shield && chmod +x setup.sh && ./setup.sh
```

## What It Does

Detects propaganda targeting European democracies, then simulates societal impact using 1,218 ATSPARA-calibrated agents. **100% local GPU — zero cloud, zero data export, GDPR compliant.**

| Version | Architecture | F1 | Agents | LLMs | XAI |
|---------|-------------|------|--------|------|-----|
| v3 | Single-LLM | 0.68 | 1 | 1 | — |
| v4 | Multi-Agent | 0.89 (+31%) | 6 | 1 | SHAP |
| **v5** | **Multi-LLM** | **0.94 (+38%)** | **6** | **7** | **SHAP+CF** |

## Usage

```bash
source .venv/bin/activate
python3 -m src.main classify --text "NATO exercises threaten Baltic peace"
python3 -m src.main simulate --steps 72 --agents 1218
python3 -m src.main simulate --steps 72 --bots     # H4: bot amplification
python3 -m src.main info                            # GPU + models
```

## Architecture

```
DATA INGESTION (18 feeds, 14 languages)
         ↓
SYSTEM A: 6-AGENT PIPELINE (Ollama — local GPU, zero cloud)
  Sentinel → Veritas → Nexus → Aegis → Oracle → Forge
  ATSPARA(LT) + FERMI(EU) + VIGILANT(EU) integration
         ↓  Typed interface (no LLM inside agents below)
SYSTEM B: ABM ENGINE (SEBRI 5-state, DHPA network, N=1,218)
         ↓
XAI: SHAP (κ=0.83) + Counterfactual + Audit Trail
         ↓
OUTPUT: 100% Local · Zero Cloud · GDPR · AGPL-3.0
```

## 📁 Repository

| Folder | Contents |
|--------|----------|
| `src/agents/` | 6 agent files + pipeline |
| `src/abm/` | SEBRI model, DHPA network, population |
| `src/xai/` | SHAP, counterfactual, audit |
| `thesis/` | Master thesis (71 pages) |
| `papers/` | EUMAS 2026, FedCSIS papers |
| `docs/` | Equations, reproduction guide |
| `tests/` | 7 automated tests |

## Key Results
- **F1 = 0.94** (+38%, McNemar p<0.001) · **89% XAI** (κ=0.83)
- **+34% belief** from segregation · **+23%** from bot amplification
- **71% topology-driven** vulnerability · Structural > content interventions

## Privacy
✅ Zero cloud · ✅ Zero data export · ✅ No telemetry · ✅ No API keys · ✅ GDPR Art.25 · ✅ Air-gap capable · ✅ AGPL-3.0

## Citation
```bibtex
@inproceedings{singh2026balticshield,
  title={Baltic Shield: Multi-Agent LLM for Propaganda Detection and ABM Simulation},
  author={Singh, Davinder and Plikynas, Darius},
  booktitle={EUMAS 2026}, publisher={Springer LNCS}, year={2026}}
```

## License
[AGPL-3.0](LICENSE) — Free to use, modify, distribute. Derivatives must be open-sourced.
