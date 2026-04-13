"""Digital Clone Population — N=1,218 from ATSPARA. Source: Plikynas et al. (2025)."""
import numpy as np
from .sebri_model import SEBRIAgent
C={"Lithuania":{"n":405,"ru":0.015,"trust":0.579},"Latvia":{"n":404,"ru":0.279,"trust":0.524},"Estonia":{"n":409,"ru":0.268,"trust":0.528}}
def generate_population(n=1218,seed=42):
    rng=np.random.default_rng(seed);agents=[];aid=0
    for country,info in C.items():
        cn=info["n"] if n==1218 else int(n*info["n"]/1218)
        for _ in range(cn):
            mt="russian" if rng.random()<info["ru"] else "titular";edu="primary" if rng.random()<0.35 else("secondary" if rng.random()<0.55 else "higher")
            ct=np.clip(rng.normal(3.0 if mt=="titular" else 2.5,0.8),1,5);ec=np.clip(rng.normal(8.0 if mt=="russian" else 7.0,2.0),3,15)
            a=SEBRIAgent(aid,country,mt,edu,ct,ec,np.clip(rng.normal(0.15 if mt=="titular" else 0.30,0.1),0,1))
            a.trust=info["trust"]+rng.normal(0,0.05);agents.append(a);aid+=1
    return agents
