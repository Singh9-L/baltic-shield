"""Evaluation metrics with bootstrap CI."""
import numpy as np
def bootstrap_ci(y_true,y_pred,metric_fn,n=1000,ci=0.95):
    scores,rng=[],np.random.default_rng(42)
    for _ in range(n):
        idx=rng.integers(0,len(y_true),size=len(y_true))
        try: scores.append(metric_fn(y_true[idx],y_pred[idx]))
        except: pass
    return float(np.mean(scores)),float(np.percentile(scores,(1-ci)/2*100)),float(np.percentile(scores,(1+ci)/2*100))
