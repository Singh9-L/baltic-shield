"""Sequential Multi-Agent Pipeline: v3 (1 agent) / v4 (6 agents, 1 LLM) / v5 (6 agents, 7 LLMs)."""
import time
from .sentinel import SentinelAgent
from .veritas import VeritasAgent
from .nexus import NexusAgent
from .aegis import AegisAgent
from .oracle import OracleAgent
from .forge import ForgeAgent
from .base import AgentResult
class Pipeline:
    def __init__(s,ollama_client,version="v5",model_config=None):
        s.version=version;mc=model_config or {}
        if version=="v3": s.agents=[VeritasAgent(ollama_client)]
        elif version=="v4": s.agents=[SentinelAgent(ollama_client),VeritasAgent(ollama_client),NexusAgent(ollama_client),AegisAgent(ollama_client),OracleAgent(ollama_client),ForgeAgent(ollama_client)]
        else: s.agents=[SentinelAgent(ollama_client,model=mc.get("sentinel","qwen2.5:7b")),VeritasAgent(ollama_client,model=mc.get("veritas","mistral:7b-instruct")),NexusAgent(ollama_client,model=mc.get("nexus","llama3.1:8b")),AegisAgent(ollama_client,model=mc.get("aegis","llama3.1:8b")),OracleAgent(ollama_client,model=mc.get("oracle","mistral:7b-instruct")),ForgeAgent(ollama_client,model=mc.get("forge","deepseek-r1:7b"))]
    def run(s,text):
        print(f"\n  Baltic Shield {s.version} — Processing...\n")
        results,context,t0=[],{},time.time()
        for a in s.agents:
            try:
                r=a.process(text,context=context);results.append(r);context[a.NAME]=r.output
                print(f"  ✓ {a.NAME:10s} ({a.model:25s}) {r.latency_ms:6.0f}ms")
            except Exception as e:
                print(f"  ✗ {a.NAME:10s} ERROR: {e}");results.append(AgentResult(a.NAME,text[:200],{"error":str(e)},a.model,0))
        total=round((time.time()-t0)*1000,1)
        summary={"version":s.version,"total_ms":total,"agents_run":len(results),"agent_results":{r.agent_name:r.to_dict() for r in results}}
        v=summary["agent_results"].get("veritas",{}).get("output",{})
        if not v.get("parse_error"): summary.update({"classification":v.get("classification","UNKNOWN"),"confidence":v.get("confidence",0)})
        cls=summary.get("classification","N/A");conf=summary.get("confidence",0)
        print(f"\n  Result: {cls} ({conf:.0%}) | {total:.0f}ms | {len(results)} agents\n")
        return summary
