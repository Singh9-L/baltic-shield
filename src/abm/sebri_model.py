"""SEBRI 5-State: S→E→B→R→I. 11 equations. ELM cognition. ODD protocol."""
import numpy as np
from enum import IntEnum
class State(IntEnum): S=0;E=1;B=2;R=3;I=4
class SEBRIAgent:
    def __init__(s,aid,country,mt,edu,ct,ec,belief=0.0):
        s.id=aid;s.country=country;s.mother_tongue=mt;s.education=edu;s.ct_score=ct;s.ec_score=ec;s.belief=belief;s.state=State.S;s.trust=0.5
        s.susceptibility=np.clip(0.50+(0.20 if mt=="russian" else 0)-(0.14 if edu=="higher" else 0)+0.08*(ec/15),0.05,0.95)
class SEBRIModel:
    def __init__(s,agents,adj,config=None):
        s.agents=agents;s.adj=adj;s.n=len(agents);s.history=[];s.step_count=0;c=config or {}
        s.alpha=c.get("alpha",0.15);s.delta=c.get("novelty_decay",0.1);s.gamma=c.get("acrophily",0.3)
    def step(s,bot_amplification=False):
        s.step_count+=1;rng=np.random.default_rng(s.step_count)
        for i,a in enumerate(s.agents):
            nb=np.where(s.adj[i]>0)[0]
            if len(nb)==0: continue
            n_b=sum(1 for j in nb if s.agents[j].state==State.B);er=n_b/len(nb) if len(nb)>0 else 0
            conval=np.exp(-s.delta*s.step_count)*(0.5+0.5*er)*(1+s.gamma*max((s.agents[j].belief for j in nb if s.agents[j].state==State.B),default=0))*(1.23 if bot_amplification else 1.0)
            if a.state==State.S and rng.random()<conval*a.susceptibility: a.state=State.E
            elif a.state==State.E:
                elm=1.0-(a.ct_score/5.0)
                if rng.random()<conval*a.susceptibility*elm*(1+a.ec_score/15): a.state=State.B;a.belief=min(1,a.belief+s.alpha*conval)
                elif rng.random()<(1-a.susceptibility)*(a.ct_score/5): a.state=State.S
            elif a.state==State.B:
                a.belief=np.clip(a.belief+s.alpha*conval*(1-a.ct_score/5)+rng.normal(0,0.02),0,1);a.trust=max(0,a.trust-0.005*conval)
                if rng.random()<0.18*(a.ct_score/5): a.state=State.R
            elif a.state==State.R:
                if rng.random()<0.02: a.state=State.B
                elif rng.random()<0.05*(a.ct_score/5): a.state=State.I
        s._record()
    def _record(s):
        counts={st:sum(1 for a in s.agents if a.state==st) for st in State};bs=[a.belief for a in s.agents];ts=[a.trust for a in s.agents]
        s.history.append({"step":s.step_count,"counts":{st.name:counts[st] for st in State},"mean_belief":float(np.mean(bs)),"polarisation":float(np.std(bs)/(np.mean(bs)+1e-9)),"mean_trust":float(np.mean(ts)),"believing_pct":counts[State.B]/s.n})
    def get_metrics(s):
        if not s.history: return {}
        f=s.history[-1];return {"steps":s.step_count,"agents":s.n,"final_believing_pct":round(f["believing_pct"]*100,1),"polarisation":round(f["polarisation"],3),"mean_belief":round(f["mean_belief"],3),"trust_erosion":round(1-f["mean_trust"],3)}
