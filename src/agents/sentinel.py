"""Agent 1: Sentinel — Multilingual Ingestion. Models: Qwen 2.5 / Phi-3.5."""
from .base import BaseAgent
class SentinelAgent(BaseAgent):
    NAME="sentinel";DESCRIPTION="Multilingual ingestion, NER, language detection"
    def get_system_prompt(s):
        return "You are Sentinel, multilingual triage agent.\nReturn JSON: {language, entities: [{text,type}], source_type, platform_origin, priority}"
