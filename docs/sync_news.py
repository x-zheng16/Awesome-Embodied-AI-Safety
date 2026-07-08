#!/usr/bin/env python3
"""Deterministic News sync.

`docs/news.json` is the SINGLE SOURCE OF TRUTH for the project's News timeline.
This script renders it into BOTH surfaces, between `<!-- NEWS:START -->` and
`<!-- NEWS:END -->` markers:

  - README.md            `## News` section  (Markdown, verbatim)
  - docs/index.html      `#news` <ul>       (Markdown subset -> HTML)

news.json is a newest-first array of {"date": "YYYY/MM/DD", "md": "<markdown>"}.
The `md` body may use the constrained Markdown subset: [text](url), **bold**,
*italic*, `code`.

Usage:
  python3 docs/sync_news.py           # regenerate both files from news.json
  python3 docs/sync_news.py --check    # exit 1 if either file is stale (pre-commit gate)
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # docs/
ROOT = HERE.parent                              # repo root
README = ROOT / "README.md"
INDEX = HERE / "index.html"
START, END = "<!-- NEWS:START -->", "<!-- NEWS:END -->"


def md_inline_to_html(s: str) -> str:
    """Convert the constrained news Markdown subset to HTML.

    Order matters: stash links first (their URLs must not be emphasis-mangled),
    escape &<> in the remaining text, apply code/bold/italic, then restore links
    with their text and URL escaped too.
    """
    links = []

    def stash(m):
        links.append((m.group(1), m.group(2)))
        return f"\x00{len(links) - 1}\x00"

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", stash, s)

    def esc(t):
        return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)

    def restore(m):
        text, url = links[int(m.group(1))]
        return f'<a href="{esc(url)}">{esc(text)}</a>'

    return re.sub(r"\x00(\d+)\x00", restore, s)


def readme_block(news) -> str:
    return "\n".join(f"- **[{n['date']}]** {n['md']}" for n in news)


def index_block(news) -> str:
    out = []
    for n in news:
        html = md_inline_to_html(n["md"])
        out.append(
            '      <li class="ni">\n'
            f'        <span class="ndate">{n["date"]}</span>\n'
            f'        <span class="ntext">{html}</span>\n'
            "      </li>"
        )
    return "\n".join(out)


def splice(text: str, block: str, end_indent: str) -> str:
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    return pat.sub(lambda _: f"{START}\n{block}\n{end_indent}{END}", text)


def main() -> int:
    check = "--check" in sys.argv
    news = json.loads((HERE / "news.json").read_text())
    targets = [(README, readme_block(news), ""), (INDEX, index_block(news), "      ")]
    stale = []
    for path, block, end_indent in targets:
        cur = path.read_text()
        if START not in cur or END not in cur:
            print(f"ERROR: {path.name} is missing the {START}/{END} markers", file=sys.stderr)
            return 2
        new = splice(cur, block, end_indent)
        if new != cur:
            stale.append(path.name)
            if not check:
                path.write_text(new)
    if check:
        if stale:
            print(f"news out of sync: {', '.join(stale)} -- run: python3 docs/sync_news.py",
                  file=sys.stderr)
            return 1
        print("news in sync")
        return 0
    print(f"synced news -> README.md + index.html ({len(news)} entries)"
          + (f"; updated {', '.join(stale)}" if stale else "; no change"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
