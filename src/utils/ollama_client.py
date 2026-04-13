"""Ollama API client — 100% local, zero cloud. GDPR compliant."""
import json,time,subprocess,requests,os
OLLAMA_BASE=os.environ.get("OLLAMA_HOST","http://localhost:11434")
def check_ollama_running():
    try: return requests.get(f"{OLLAMA_BASE}/api/tags",timeout=5).status_code==200
    except: return False
def get_available_models():
    try: return [m["name"] for m in requests.get(f"{OLLAMA_BASE}/api/tags",timeout=10).json().get("models",[])]
    except: return []
def get_gpu_vram_mb():
    try:
        r=subprocess.run(["nvidia-smi","--query-gpu=memory.total","--format=csv,noheader,nounits"],capture_output=True,text=True,timeout=10)
        return int(r.stdout.strip().split("\n")[0]) if r.returncode==0 else 0
    except: return 0
class OllamaClient:
    def __init__(s,default_model="mistral:7b-instruct"):
        s.default_model=default_model;s.vram_mb=get_gpu_vram_mb();s._calls=0
        if not check_ollama_running(): raise RuntimeError("Ollama not running. Start: ollama serve\nInstall: curl -fsSL https://ollama.ai/install.sh | sh")
    def generate(s,prompt,model=None,system=None,temperature=0.3,max_tokens=2048):
        model=model or s.default_model;s._calls+=1
        payload={"model":model,"prompt":prompt,"stream":False,"options":{"temperature":temperature,"num_predict":max_tokens}}
        if system: payload["system"]=system
        try:
            r=requests.post(f"{OLLAMA_BASE}/api/generate",json=payload,timeout=120);r.raise_for_status();return r.json().get("response","").strip()
        except requests.Timeout: return "[ERROR] Timeout"
        except requests.ConnectionError: return "[ERROR] Ollama unreachable"
        except Exception as e: return f"[ERROR] {e}"
    def generate_json(s,prompt,model=None,system=None,temperature=0.1):
        if system: system+="\nRespond ONLY with valid JSON."
        resp=s.generate(prompt,model=model,system=system,temperature=temperature)
        try:
            c=resp.strip()
            if c.startswith("```"): c=c.split("\n",1)[1].rsplit("```",1)[0].strip()
            if c.startswith("json"): c=c[4:].strip()
            return json.loads(c)
        except: return {"raw_response":resp,"parse_error":True}
