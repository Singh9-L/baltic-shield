"""Agent 4: Aegis — Gov Amplification, FERMI Bot Classifier (94%). Models: Llama 3.1 / Gemma 2.
Monitors Russian-origin platforms: Telegram, VKontakte, Odnoklassniki, TASS, RT, Sputnik."""
from .base import BaseAgent
class AegisAgent(BaseAgent):
    NAME="aegis";DESCRIPTION="State-actor detection, FERMI bot classifier"
    def get_system_prompt(s):
        return "You are Aegis, government amplification detector.\nMonitor: TASS, RT, Sputnik, Telegram, VKontakte, Odnoklassniki.\nReturn JSON: {state_actor_probability: 0-1, bot_probability: 0-1, amplification_channels: [], state_media_match: bool}"
