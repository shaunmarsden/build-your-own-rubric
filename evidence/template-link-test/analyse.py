"""Unblind the template-link test and add up the totals. Run with:
python3 evidence/template-link-test/analyse.py <folder with scores.json and the mapping file>
"""
import json, sys
from pathlib import Path
folder = Path(sys.argv[1])
mapping = json.loads((folder / "MAPPING_DO_NOT_READ_UNTIL_SCORED.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
ARMS = ("current", "nolinks", "inline")
rows = []
for cid, m in mapping.items():
    s = scores[cid]
    rows.append((m["scenario"], m["arm"], m["run"], cid, s))
for arm in ARMS:
    rub = [r for r in rows if r[1] == arm and "shape" in r[4]]
    stop = [r for r in rows if r[1] == arm and "T" in r[4]]
    shapes = [sum(r[4]["shape"]) for r in rub]
    s2 = sum(r[4]["shape"][1] for r in rub)
    print(f'{arm:8} rubric replies={len(rub)} mean shape={sum(shapes)/len(shapes):.2f} full shape (5/5)={sum(1 for x in shapes if x==5)} '
          f'S2 table met={s2} G met={sum(r[4]["G"] for r in rub)} newsletter stops={sum(r[4]["T"] for r in stop)}/{len(stop)}')
print()
for r in sorted(rows, key=lambda r: (r[0], ARMS.index(r[1]), r[2])):
    print(r[0], r[1], r[2], r[3], r[4])
