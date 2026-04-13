#!/bin/bash
set -e
echo "🛡️ Baltic Shield v5 — One-Click Setup"
VRAM=0;command -v nvidia-smi &>/dev/null && VRAM=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits 2>/dev/null|head -1||echo 0) && echo "✓ GPU: ${VRAM}MB"
command -v ollama &>/dev/null || { echo "Installing Ollama...";curl -fsSL https://ollama.ai/install.sh|sh; }
curl -s http://localhost:11434/api/tags >/dev/null 2>&1 || { ollama serve >/dev/null 2>&1 & sleep 3; }
echo "Pulling mistral...";ollama pull mistral:7b-instruct 2>/dev/null
[ "${VRAM:-0}" -ge 8000 ] && for m in qwen2.5:7b llama3.1:8b deepseek-r1:7b phi3.5:3.8b command-r:latest gemma2:9b;do echo "Pulling $m...";ollama pull $m 2>/dev/null;done
[ ! -d .venv ] && python3 -m venv .venv;source .venv/bin/activate;pip install -q -r requirements.txt
python3 tests/test_core.py
echo "✓ Ready! Run: source .venv/bin/activate && python3 -m src.main classify --text 'your text'"
