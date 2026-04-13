"""Agent 6: Forge — Autonomous Rule Generation. Models: DeepSeek-R1 / Phi-3.5."""
from .base import BaseAgent
class ForgeAgent(BaseAgent):
    NAME="forge";DESCRIPTION="Autonomous detection rule generation"
    def get_system_prompt(s):
        return "You are Forge, rule generator.\nReturn JSON: {rule_name, rule_type, detection_logic, target_accuracy: 0-1, applicable_languages: [], improvement_rationale}"
