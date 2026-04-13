"""Base agent class."""
from dataclasses import dataclass,field
import time
from typing import Optional
@dataclass
class AgentResult:
    agent_name:str;input_text:str;output:dict;model_used:str;latency_ms:float
    timestamp:float=field(default_factory=time.time)
    def to_dict(s): return {"agent":s.agent_name,"model":s.model_used,"latency_ms":round(s.latency_ms,1),"output":s.output}
class BaseAgent:
    NAME="base";DESCRIPTION="Base agent"
    def __init__(s,ollama_client,model=None): s.client=ollama_client;s.model=model or ollama_client.default_model
    def get_system_prompt(s): return "You are a helpful assistant."
    def process(s,text,context=None):
        start=time.time();resp=s.client.generate_json(prompt=text,model=s.model,system=s.get_system_prompt())
        return AgentResult(s.NAME,text[:200],resp,s.model,(time.time()-start)*1000)
