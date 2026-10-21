"""Deterministic paper-list sync.

`docs/papers.json` is the SINGLE SOURCE OF TRUTH for every paper entry and every
paper-count on the site. This script renders it into the two hand-maintained
surfaces, killing the 3-copy drift (papers.json / index.html / README):

  - docs/index.html   the <ul class="paper-list"> under each cat-summary, plus the
                      (N) count in every cat-summary.
  - README.md         the `- [...]` lines under each subcategory <details>, plus:
                      the "We review **N** papers" prose, the Survey-Scope table
                      per-layer counts, the layer-accordion "(N papers)" counts,
                      and the subcategory-accordion "(n)" counts.
  - llms.txt          the "covering N papers" headline + the taxonomy table counts
                      (counts only; llms.txt carries no per-paper list).

Rendering is keyed by subcategory name (papers.json `subcat`). Within a subcat,
papers render in papers.json `id` order (matching the live site). Non-standard
entries (tools/orgs with no venue+year, e.g. "Isaac Sim. NVIDIA.") keep a verbatim
tail from docs/paper_render.json; venue display strings (the "In " prefix etc.)
also come from that config's venue_map.

The headline totals + per-layer <li> counts that index.html shows are additionally
guarded by docs/check_counts.py; this script is the generator, check_counts is the
independent audit.

Usage:
  python3 docs/sync_papers.py            # regenerate index.html + README from papers.json
  python3 docs/sync_papers.py --check    # exit 1 if either file is stale (pre-commit gate)
"""
import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
README = ROOT / "README.md"
INDEX = HERE / "index.html"
LLMS = ROOT / "llms.txt"

TAXONOMY = ["Perception", "Cognition", "Planning", "Action and Interaction", "Agentic"]
ORW = "Other Related Works"
LAYERS = [
    ("perception", "Perception", "Perception"),
    ("cognition", "Cognition", "Cognition"),
    ("planning", "Planning", "Planning"),
    ("action", "Action and Interaction", "Action and Interaction"),
    ("agentic", "Agentic", "Agentic System"),
    ("orw", "Other Related Works", "Other Related Works"),
]


def esc_html(s: str) -> str:
    """Escape a title for placement inside <a>...</a> (matches the hand-authored site)."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load():
    papers = json.loads((HERE / "papers.json").read_text())
    cfg = json.loads((HERE / "paper_render.json").read_text())
    return papers, cfg


def group_by_subcat(papers):
    g = defaultdict(list)
    for p in papers:
        g[p["subcat"]].append(p)
    for sub in g:
        g[sub].sort(key=lambda p: p["id"])
    return g


def venue_disp(venue, venue_map, warnings):
    if venue not in venue_map:
        warnings.add(venue)
    return venue_map.get(venue, venue)


def gen_li(p, cfg, warnings):
    """One index.html <li> (title escaped; venue raw)."""
    a = f'<a href="{p["url"]}" target="_blank" rel="noopener">{esc_html(p["title"])}</a>'
    tail = cfg["html_edge"].get(str(p["id"]))
    if tail is None:
        auth = p["authors"].rstrip(".")
        tail = f'. {auth}. <em>{venue_disp(p["venue"], cfg["venue_map"], warnings)}</em>, {p["year"]}.'
    return f"<li>{a}{tail}</li>"


def gen_md(p, cfg, warnings):
    """One README `- [...]` line (raw, no HTML escaping)."""
    tail = cfg["md_edge"].get(str(p["id"]))
    if tail is None:
        auth = p["authors"].rstrip(".")
        end = "." if p["id"] <= 559 else ""
        tail = f'. {auth}. *{venue_disp(p["venue"], cfg["venue_map"], warnings)}*, {p["year"]}{end}'
    return f'- [{p["title"]}]({p["url"]}){tail}'


def render_index(text, all_papers, groups, cfg, warnings, check=False):
    """Replace each cat-summary count + its <ul class="paper-list"> inner li list."""
    layer_ct = defaultdict(int)
    for p in all_papers:
        layer_ct[p["layer"]] += 1
    total = len(all_papers)

    text = re.sub(
        r'(stat-num">)\d+(</span><span class="stat-label">Papers Surveyed)',
        rf"\g<1>{total}\g<2>",
        text,
    )
    text = re.sub(
        r'(id="searchStats">)\d+(\s*papers)',
        rf"\g<1>{total}\g<2>",
        text,
    )
    text = re.sub(
        r'(data-layer="all"[^>]*>All \()\d+(\))',
        rf"\g<1>{total}\g<2>",
        text,
    )
    text = re.sub(
        r'(<span class="total-count">)\d+(</span>)',
        rf"\g<1>{total}\g<2>",
        text,
    )
    for lid, name, scope_name in LAYERS:
        cnt = layer_ct[name]
        text = re.sub(
            r'(<div class="lname">' + re.escape(scope_name) + r'</div>.*?<span class="cnt">)\d+(</span>)',
            rf"\g<1>{cnt}\g<2>",
            text,
            flags=re.DOTALL,
        )
        text = re.sub(
            r'(href="#layer-' + re.escape(lid) + r'"[^>]*>[^<]*<em>\()\d+(\))',
            rf"\g<1>{cnt}\g<2>",
            text,
        )
        text = re.sub(
            r'(id="layer-' + re.escape(lid) + r'"[^>]*>\s*<summary class="layer-summary">.*?<span class="layer-cnt">)\d+( papers</span>)',
            rf"\g<1>{cnt}\g<2>",
            text,
            flags=re.DOTALL,
        )

    pat = re.compile(
        r'(<summary class="cat-summary">)(.*?)( <span class="cat-cnt">\()(\d+)(\)</span></summary>\s*'
        r'<ul class="paper-list">)(.*?)(</ul>)',
        re.DOTALL,
    )

    def repl(m):
        name = html.unescape(m.group(2))
        if name not in groups:
            sys.exit(f"FATAL: index.html cat-summary {name!r} has no papers in papers.json")
        papers = groups[name]
        cur = {html.unescape(t) for t in re.findall(r"<a [^>]*>(.*?)</a>", m.group(6), re.DOTALL)}
        want = {p["title"] for p in papers}
        if (check and cur != want) or (cur - want):
            sys.exit(f"FATAL [index.html/{name}]: membership drift\n  +{want - cur}\n  -{cur - want}")
        inner = "\n" + "\n".join("            " + gen_li(p, cfg, warnings) for p in papers) + "\n          "
        return f"{m.group(1)}{m.group(2)}{m.group(3)}{len(papers)}{m.group(5)}{inner}{m.group(7)}"

    new, n = pat.subn(repl, text)
    if n != 22:
        sys.exit(f"FATAL: index.html matched {n} paper-list blocks (expected 22)")
    return new


def render_readme(text, papers, groups, cfg, warnings, check=False):
    layer_ct = defaultdict(int)
    for p in papers:
        layer_ct[p["layer"]] += 1
    tax_total = sum(layer_ct[l] for l in TAXONOMY)

    text = re.sub(r"We review \*\*\d+\*\* papers", f"We review **{tax_total}** papers", text)

    for layer in TAXONOMY:
        cnt_cell = f"| {layer_ct[layer]:>6} |"
        text = re.sub(
            r"(\| \*\*" + re.escape(layer) + r"\*\* +\|.*?)\|\s*\d+\s*\|",
            lambda m, cell=cnt_cell: f"{m.group(1)}{cell}",
            text,
        )

    for layer in TAXONOMY:
        text = re.sub(
            r"(<summary>[^<]*<b>" + re.escape(layer) + r"</b> \()\d+( papers\)</summary>)",
            r"\g<1>" + str(layer_ct[layer]) + r"\g<2>",
            text,
        )

    subcat_pat = re.compile(
        r"(<summary>(?:<b>)?)([^<(]+?)((?:</b>)? \()(\d+)(\)</summary>\n\n)(.*?)(\n</details>)",
        re.DOTALL,
    )

    def repl(m):
        name = m.group(2).strip()
        if name not in groups:
            sys.exit(f"FATAL: README subcategory {name!r} has no papers in papers.json")
        papers_sub = groups[name]
        cur = set(re.findall(r"^- \[(.*?)\]\(", m.group(6), re.MULTILINE))
        want = {p["title"] for p in papers_sub}
        if (check and cur != want) or (cur - want):
            sys.exit(f"FATAL [README/{name}]: membership drift\n  +{want - cur}\n  -{cur - want}")
        lines = "\n".join(gen_md(p, cfg, warnings) for p in papers_sub)
        return f"{m.group(1)}{m.group(2)}{m.group(3)}{len(papers_sub)}{m.group(5)}{lines}{m.group(7)}"

    text, n = subcat_pat.subn(repl, text)
    if n != 22:
        sys.exit(f"FATAL: README matched {n} subcategory blocks (expected 22)")
    return text


def render_llms(text, papers):
    """Regenerate llms.txt: the "covering N papers" headline + the 6-row taxonomy
    table counts. Same padded-cell trap as the README table -- allow 1+ spaces
    before the closing pipe."""
    layer_ct = defaultdict(int)
    for p in papers:
        layer_ct[p["layer"]] += 1
    text = re.sub(r"covering \d+ papers", f"covering {len(papers)} papers", text)
    for _lid, layer, disp in LAYERS:
        cnt_cell = f"| {layer_ct[layer]:>6} |"
        text = re.sub(
            r"(\| " + re.escape(disp) + r" +\|.*?)\|\s*\d+\s*\|",
            lambda m, cell=cnt_cell: f"{m.group(1)}{cell}",
            text,
        )
    return text


def main() -> int:
    check = "--check" in sys.argv
    papers, cfg = load()
    groups = group_by_subcat(papers)
    warnings = set()

    targets = [
        (INDEX, render_index(INDEX.read_text(), papers, groups, cfg, warnings, check=check)),
        (README, render_readme(README.read_text(), papers, groups, cfg, warnings, check=check)),
        (LLMS, render_llms(LLMS.read_text(), papers)),
    ]

    if warnings:
        print("WARNING: venue(s) missing from paper_render.json venue_map (rendered verbatim):",
              file=sys.stderr)
        for v in sorted(warnings):
            print(f"  {v!r}", file=sys.stderr)

    stale = []
    for path, new in targets:
        if new != path.read_text():
            stale.append(path.name)
            if not check:
                path.write_text(new)

    if check:
        if stale:
            print(f"papers out of sync: {', '.join(stale)} -- run: python3 docs/sync_papers.py",
                  file=sys.stderr)
            return 1
        print("papers in sync")
        return 0
    print(f"synced papers -> index.html + README.md + llms.txt ({len(papers)} papers)"
          + (f"; updated {', '.join(stale)}" if stale else "; no change"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
