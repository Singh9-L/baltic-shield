"""Simulation runner."""
from .agent_population import generate_population
from .dhpa_network import generate_dhpa_network
from .sebri_model import SEBRIModel
def run_simulation(n_agents=1218,n_steps=72,bot_amplification=False,seed=42,config=None):
    agents=generate_population(n=n_agents,seed=seed);adj=generate_dhpa_network(agents,config=config)
    model=SEBRIModel(agents,adj,config=config)
    for _ in range(n_steps): model.step(bot_amplification=bot_amplification)
    return model.get_metrics(),model.history
