#!/usr/bin/env python3
"""Guard: every paper-count on docs/index.html must agree with papers.json.

Single source of truth = papers.json (one row per paper, single `layer` field).
Every literal the page shows -- Survey Scope table, Surveyed Papers TOC / pills /
hero / search-stats, and the actual <li> entries -- is derived from it and must
match. Run standalone or as a git pre-commit hook; exits non-zero on any drift.

Usage:  python3 docs/check_counts.py
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML = (HERE / "index.html").read_text()
PAPERS = json.loads((HERE / "papers.json").read_text())

# layer-id (html)  ->  layer string (papers.json).  First 5 = taxonomy; orw is adjacent.
TAXONOMY = [
    ("perception", "Perception"),
    ("cognition", "Cognition"),
    ("planning", "Planning"),
    ("action", "Action and Interaction"),
    ("agentic", "Agentic"),
]
ORW = ("orw", "Other Related Works")
ALL_LAYERS = TAXONOMY + [ORW]

# ---- source of truth -------------------------------------------------------
truth = Counter(p["layer"] for p in PAPERS)
truth_total = len(PAPERS)
truth_taxonomy = sum(truth[name] for _, name in TAXONOMY)


def section(sid):
    m = re.search(rf'<section id="{sid}">.*?</section>', HTML, re.S)
    if not m:
        sys.exit(f"FATAL: <section id={sid}> not found")
    return m.group(0)


def li_per_layer(papers_sec):
    """Count actual <li> between consecutive id="layer-X" markers."""
    marks = [(m.start(), m.group(1)) for m in
             re.finditer(r'id="layer-([a-z]+)"', papers_sec)]
    out = {}
    for i, (pos, lid) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(papers_sec)
        out[lid] = len(re.findall(r"<li\b", papers_sec[pos:end]))
    return out


scope_sec = section("scope")
papers_sec = section("papers")

scope_cnts = [int(x) for x in re.findall(r'class="cnt">(\d+)</span>', scope_sec)]
scope_total = int(re.search(r'class="total-count">(\d+)</span>', scope_sec).group(1))
toc = {lid: int(n) for lid, n in
       re.findall(r'href="#layer-([a-z]+)"[^>]*>[^<]*<em>\((\d+)\)', papers_sec)}
li = li_per_layer(papers_sec)
hero = int(re.search(r'stat-num">(\d+)</span><span class="stat-label">Papers Surveyed', HTML).group(1))
stats = int(re.search(r'id="searchStats">(\d+)\s*papers', HTML).group(1))
pill_all = int(re.search(r'data-layer="all"[^>]*>All \((\d+)\)', HTML).group(1))

fails = []


def check(label, got, want):
    if got != want:
        fails.append(f"  {label:42} page={got:<5} expected={want}")


# 1. rendered <li> faithful to papers.json (per layer)
for lid, name in ALL_LAYERS:
    check(f"<li> count [{lid}]", li.get(lid, 0), truth[name])
# 2. Surveyed-Papers TOC matches papers.json (per layer)
for lid, name in ALL_LAYERS:
    check(f"TOC em [{lid}]", toc.get(lid, 0), truth[name])
# 3. headline totals all equal papers.json total
check("hero stat-num", hero, truth_total)
check("searchStats literal", stats, truth_total)
check("pill All(N)", pill_all, truth_total)
# 4. Survey Scope per-layer matches papers.json (all 6 rows incl ORW)
for i, (lid, name) in enumerate(ALL_LAYERS):
    got = scope_cnts[i] if i < len(scope_cnts) else None
    check(f"Scope cnt [{lid}]", got, truth[name])
# 5. Scope total == sum of its rows == papers.json grand total
check("Scope total == sum(rows)", scope_total, sum(scope_cnts))
check("Scope total == json total", scope_total, truth_total)

# 6. llms.txt taxonomy table + headline match papers.json
llms_path = HERE.parent / "llms.txt"
if llms_path.exists():
    llms = llms_path.read_text()
    LLMS_NAME = {'Action and Interaction': 'Action and Interaction', 'Agentic': 'Agentic System'}
    for lid, name in ALL_LAYERS:
        row = re.search(r'\|\s*' + re.escape(LLMS_NAME.get(name, name)) + r'\s*\|[^|]*\|\s*(\d+)\s*\|', llms)
        check(f"llms.txt [{lid}]", int(row.group(1)) if row else None, truth[name])
    head = re.search(r'covering (\d+) papers', llms)
    check("llms.txt headline", int(head.group(1)) if head else None, truth_total)

print(f"papers.json: {truth_total} total "
      f"({truth_taxonomy} taxonomy + {truth[ORW[1]]} ORW)")
print("per-layer:   " + "  ".join(f"{lid}={truth[name]}" for lid, name in ALL_LAYERS))
if fails:
    print(f"\nFAIL: {len(fails)} count mismatch(es):")
    print("\n".join(fails))
    sys.exit(1)
print("\nPASS: all page counts agree with papers.json")
