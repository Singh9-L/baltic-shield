"""DHPA Network — Directed Homophilic Preferential Attachment."""
import numpy as np,networkx as nx
def generate_dhpa_network(agents,config=None):
    cfg=config or {};alpha=cfg.get("alpha_homophily",0.45);beta=cfg.get("beta_platform",0.30);n=len(agents);G=nx.DiGraph();G.add_nodes_from(range(n));deg=np.ones(n)
    for i in range(n):
        ne=max(2,int(np.random.poisson(cfg.get("avg_degree",12))));pr=np.zeros(n)
        for j in range(n):
            if i==j: continue
            pr[j]=alpha*(1.0 if agents[i].mother_tongue==agents[j].mother_tongue else 0)+beta*(1.0 if agents[i].country==agents[j].country else 0.3)+(1-alpha-beta)*deg[j]/deg.sum()
        pr[i]=0;pr/=(pr.sum()+1e-12)
        for t in np.random.choice(n,size=min(ne,n-1),replace=False,p=pr): G.add_edge(i,t);deg[t]+=1
    return nx.to_numpy_array(G)
