"""Unblind the automatic-failures test and add up the totals. Run with:
python3 evidence/auto-failures-test/analyse.py <folder with scores.json and the mapping file>
scores.json holds [N, G, U, F, shape] per rubric reply, or ["T"] for a quiz reply that stopped.
"""
import json, sys
from pathlib import Path
folder = Path(sys.argv[1])
mapping = json.loads((folder / "MAPPING_DO_NOT_READ_UNTIL_SCORED.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
for arm in ("baseline", "rule"):
    rub = [(cid, scores[cid]) for cid, m in mapping.items() if m["arm"] == arm and scores[cid][0] != "T"]
    stop = [cid for cid, m in mapping.items() if m["arm"] == arm and scores[cid][0] == "T"]
    n = sum(s[0] for _, s in rub); g = sum(s[1] for _, s in rub); u = sum(s[2] for _, s in rub)
    f = sum(s[3] for _, s in rub); shape = sum(s[4] for _, s in rub)
    print(f"{arm:9} rubric replies={len(rub)} failures={n} (mean {n/len(rub):.2f}) grounded={g} ungrounded={u} (mean {u/len(rub):.2f}) "
          f"replies with an ungrounded failure={sum(1 for _, s in rub if s[2])} F={f}/{len(rub)} mean shape={shape/len(rub):.1f} quiz stops={len(stop)}")
print()
for sc in ("invoices", "applicants", "tenancy"):
    for arm in ("baseline", "rule"):
        rows = [(cid, scores[cid]) for cid, m in mapping.items() if m["scenario"] == sc and m["arm"] == arm]
        print(f"{sc:11} {arm:9} N={[s[0] for _, s in rows]} U={[s[2] for _, s in rows]}")
