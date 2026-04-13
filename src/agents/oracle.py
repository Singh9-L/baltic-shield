"""Agent 5: Oracle — SHAP XAI + Counterfactual. Models: Mistral / DeepSeek-R1 / Gemma 2."""
from .base import BaseAgent
class OracleAgent(BaseAgent):
    NAME="oracle";DESCRIPTION="SHAP XAI, counterfactual reasoning"
    def get_system_prompt(s):
        return "You are Oracle, XAI agent.\nReturn JSON: {shap_features: [{feature, contribution, direction}], counterfactual: str, impact_scores: {polarisation, echo_chamber, radicalisation, trust_erosion}, confidence_explanation: str}"
