"""Agent 2: Veritas — Propaganda Classification (ATSPARA 9 techniques). Models: Mistral / Command-R."""
from .base import BaseAgent
TECHNIQUES=["Emotional Expression","Simplification","Doubt and Smear","Whataboutism","Repetition","Appeal to Authority","Flag-waving","Reductio ad Hitlerum","Bandwagoning"]
NARRATIVES=["Distrust national institutions","Distrust Western institutions","Western moral decay","NATO aggression","Pro-authoritarian","National defamation","New world order","Migrant crisis","Climate denial","Economic collapse"]
class VeritasAgent(BaseAgent):
    NAME="veritas";DESCRIPTION="Propaganda classification (ATSPARA taxonomy)"
    def get_system_prompt(s):
        return f"You are Veritas, propaganda classifier.\nTechniques: {', '.join(TECHNIQUES)}\nNarratives: {', '.join(NARRATIVES)}\nReturn JSON: {{classification: PROPAGANDA/LEGITIMATE/MONITORING, confidence: 0-1, techniques: [{{name,score}}], primary_narrative, reasoning, emotional_density: 0-1}}"
