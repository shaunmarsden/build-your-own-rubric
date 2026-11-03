"""Unblind the wording test and add up the totals. From the repository root:
python3 evidence/wording-test/analyse.py evidence/wording-test
scores.json holds [N, G, U, F, shape, copied] per rubric reply, or ["T"] for a quiz reply that stopped.
"""
import json
import sys
from pathlib import Path

folder = Path(sys.argv[1])
mapping = json.loads((folder / "mapping.json").read_text())
scores = json.loads((folder / "scores.json").read_text())

for arm in ("current", "edited"):
    rub = [s for cid, s in scores.items() if mapping[cid]["arm"] == arm and s[0] != "T"]
    stop = [cid for cid, s in scores.items() if mapping[cid]["arm"] == arm and s[0] == "T"]
    n = len(rub)
    print(
        f"{arm:8} rubric replies={n} failures={sum(s[0] for s in rub)} "
        f"ungrounded={sum(s[2] for s in rub)} F={sum(s[3] for s in rub)}/{n} "
        f"shape 5/5={sum(s[4] == 5 for s in rub)}/{n} "
        f"copied total={sum(s[5] for s in rub)} mean={sum(s[5] for s in rub) / n:.2f} "
        f"quiz stops={len(stop)}"
    )

print()
for sc in ("invoices", "applicants", "tenancy"):
    for arm in ("current", "edited"):
        rows = [scores[c] for c, m in mapping.items() if m["scenario"] == sc and m["arm"] == arm]
        print(f"{sc:10} {arm:8} copied={[r[5] for r in rows]} N={[r[0] for r in rows]}")
