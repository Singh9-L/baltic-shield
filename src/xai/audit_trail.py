"""GDPR-compliant local audit trail. Zero cloud."""
import json,time,os
class AuditTrail:
    def __init__(s,d="data/audit"): s.dir=d;os.makedirs(d,exist_ok=True);s.entries=[]
    def record(s,r): e={"timestamp":time.time(),"classification":r.get("classification"),"confidence":r.get("confidence")};s.entries.append(e);return e
    def export(s,fp=None):
        fp=fp or os.path.join(s.dir,f"audit_{int(time.time())}.json")
        with open(fp,"w") as f: json.dump(s.entries,f,indent=2);return fp
