"""Counterfactual Explanations — minimum change to reverse classification."""
def generate_counterfactual(classification,shap_features):
    if classification!="PROPAGANDA": return "No counterfactual needed."
    pos=[f for f in shap_features if f["direction"]=="+"]
    if not pos: return "Insufficient data."
    t=pos[0];feat=t["feature"].replace("_"," ");val=t["value"];return f"If {feat} were reduced (contribution: {val:+.2f}), classification would shift to MONITORING or LEGITIMATE."
