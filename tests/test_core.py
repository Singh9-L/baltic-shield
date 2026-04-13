"""7 tests — no Ollama needed."""
import sys,os;sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def test_population():
    from src.abm.agent_population import generate_population
    a=generate_population(n=100,seed=42);assert len(a)>0;print(f"  ✓ Population: {len(a)} agents")
def test_network():
    from src.abm.agent_population import generate_population
    from src.abm.dhpa_network import generate_dhpa_network
    a=generate_population(n=50,seed=42);adj=generate_dhpa_network(a);assert adj.shape==(len(a),len(a));print(f"  ✓ DHPA: {adj.shape[0]} nodes, {int((adj>0).sum())} edges")
def test_simulation():
    from src.abm import run_simulation
    m,h=run_simulation(50,10,seed=42);assert m["steps"]==10;print(f"  ✓ SEBRI: believing={m['final_believing_pct']}%")
def test_bots():
    from src.abm import run_simulation
    m1,_=run_simulation(50,20,False,42);m2,_=run_simulation(50,20,True,42);assert m2["mean_belief"]>=m1["mean_belief"];print(f"  ✓ Bots: {m1['mean_belief']:.3f}→{m2['mean_belief']:.3f}")
def test_shap():
    from src.xai import compute_shap_features
    f=compute_shap_features({"veritas":{"output":{"emotional_density":0.7,"techniques":["X"]}},"aegis":{"output":{"bot_probability":0.8}}});assert len(f)==8;print(f"  ✓ SHAP: {len(f)} features")
def test_cf():
    from src.xai import compute_shap_features,generate_counterfactual
    cf=generate_counterfactual("PROPAGANDA",compute_shap_features({"veritas":{"output":{"emotional_density":0.7,"techniques":["X"]}},"aegis":{"output":{"bot_probability":0.8}}}));assert len(cf)>20;print("  ✓ Counterfactual")
def test_lang():
    from src.utils.nlp_tools import detect_language
    assert detect_language("Vilnius yra sostine")=="lt";assert detect_language("Hello world")=="en";print("  ✓ Language detection")
if __name__=="__main__":
    tests=[test_population,test_network,test_simulation,test_bots,test_shap,test_cf,test_lang];p=0
    for t in tests:
        try: t();p+=1
        except Exception as e: print(f"  ✗ {t.__name__}: {e}")
    print(f"\n  {p}/{len(tests)} passed {'✓' if p==len(tests) else '✗'}");exit(0 if p==len(tests) else 1)
