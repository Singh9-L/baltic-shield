"""Baltic Shield v5 CLI. Usage: python3 -m src.main [classify|simulate|ablation|info]"""
import click
@click.group()
def cli(): """Baltic Shield v5 — Privacy-First Propaganda Detection"""
@cli.command()
@click.option("--text",required=True)
@click.option("--version",default="v5",type=click.Choice(["v3","v4","v5"]))
def classify(text,version):
    """Classify text (requires Ollama)."""
    from src.utils.ollama_client import OllamaClient
    from src.agents.pipeline import Pipeline
    Pipeline(OllamaClient(),version=version).run(text)
@cli.command()
@click.option("--steps",default=72)
@click.option("--agents",default=1218)
@click.option("--bots/--no-bots",default=False)
def simulate(steps,agents,bots):
    """Run SEBRI simulation (no Ollama needed)."""
    from src.abm import run_simulation
    print(f"\n  SEBRI: {agents} agents, {steps}h, bots={bots}")
    m,_=run_simulation(n_agents=agents,n_steps=steps,bot_amplification=bots)
    for k,v in m.items(): print(f"  {k:25s}: {v}")
@cli.command()
def info():
    """System info."""
    from src.utils.ollama_client import check_ollama_running,get_available_models,get_gpu_vram_mb
    vram=get_gpu_vram_mb();ok=check_ollama_running();models=get_available_models() if ok else []
    print(f"\n  🛡️ Baltic Shield v5\n  GPU: {vram}MB | Ollama: {'✓' if ok else '✗'} | Models: {len(models)}")
    for m in models: print(f"    • {m}")
    print(f"  Privacy: 100% local, zero cloud, GDPR\n")
if __name__=="__main__": cli()
