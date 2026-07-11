#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Self-hosted Star History chart generator.

Why: the README's chart was fetched from api.star-history.com, whose shared
GitHub-token pool is chronically rate-limited (HTTP 503 "All GitHub API tokens
are rate-limited"), so the image renders blank. This tool fetches the repo's
own stargazer timeline through the `gh` CLI (the repo's own token is not subject
to that shared pool) and hand-emits a static SVG line chart in light and dark
themes — a drop-in replacement for the two remote srcset URLs.

Output (into --out-dir):
  star-history.svg        light theme
  star-history-dark.svg   dark theme
  preview.html            side-by-side preview for eyeballing

Usage:
  ./gen_star_history.py --repo x-zheng16/Awesome-Embodied-AI-Safety --out-dir .
  ./gen_star_history.py --repo owner/name --stars-file stars.txt   # offline/test
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── theme palettes ────────────────────────────────────────────────────────────
THEMES = {
    "light": {
        "bg": "#ffffff", "fg": "#24292f", "muted": "#57606a",
        "grid": "#e6e8eb", "axis": "#d0d7de",
        "c0": "#7c3aed", "c1": "#ec4899", "area": 0.10,
    },
    "dark": {
        "bg": "#0d1117", "fg": "#e6edf3", "muted": "#8b949e",
        "grid": "#21262d", "axis": "#30363d",
        "c0": "#a371f7", "c1": "#f778ba", "area": 0.16,
    },
}
W, H = 800, 400
ML, MR, MT, MB = 64, 28, 56, 46          # plot margins
PW, PH = W - ML - MR, H - MT - MB          # plot area


def fetch_stars(repo: str) -> list[datetime]:
    """All starred_at timestamps via the repo's own token (gh), ascending."""
    out = subprocess.run(
        ["gh", "api", "--paginate",
         "-H", "Accept: application/vnd.github.star+json",
         f"/repos/{repo}/stargazers?per_page=100", "--jq", ".[].starred_at"],
        capture_output=True, text=True, check=True,
    ).stdout
    return _parse(out.splitlines())


def _parse(lines) -> list[datetime]:
    ts = [datetime.fromisoformat(l.strip().replace("Z", "+00:00"))
          for l in lines if l.strip()]
    return sorted(ts)


def _nice_step(vmax: float, target_ticks: int = 5) -> int:
    """Round vmax/target to a 1/2/5·10ⁿ step."""
    raw = max(vmax / target_ticks, 1)
    mag = 10 ** (len(str(int(raw))) - 1)
    for m in (1, 2, 5, 10):
        if m * mag >= raw:
            return int(m * mag)
    return int(10 * mag)


def _month_starts(t0: datetime, t1: datetime) -> list[datetime]:
    """First-of-month ticks strictly inside (t0, t1], plus t1's month if room."""
    out, y, m = [], t0.year, t0.month
    while True:
        m += 1
        if m > 12:
            m, y = 1, y + 1
        d = datetime(y, m, 1, tzinfo=timezone.utc)
        if d > t1:
            break
        out.append(d)
    return out


def build_svg(stars: list[datetime], repo: str, theme: str) -> str:
    t = THEMES[theme]
    now = datetime.now(timezone.utc)
    t0, t1 = stars[0], now
    span = max((t1 - t0).total_seconds(), 1.0)
    total = len(stars)

    ystep = _nice_step(total)
    ytop = ((total // ystep) + 1) * ystep

    def px(dt: datetime) -> float:
        return ML + PW * (dt - t0).total_seconds() / span

    def py(v: float) -> float:
        return MT + PH * (1 - v / ytop)

    # cumulative polyline: (t_i, i+1) then flat to now
    pts = [(px(dt), py(i + 1)) for i, dt in enumerate(stars)]
    pts.append((px(now), py(total)))
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = (f"{ML:.1f},{py(0):.1f} " + line +
            f" {px(now):.1f},{py(0):.1f}")

    s: list[str] = []
    s.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">'
    )
    s.append(f'<defs><linearGradient id="ln" x1="0" y1="0" x2="1" y2="0">'
             f'<stop offset="0" stop-color="{t["c0"]}"/>'
             f'<stop offset="1" stop-color="{t["c1"]}"/></linearGradient>'
             f'<linearGradient id="ar" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{t["c1"]}" stop-opacity="{t["area"]}"/>'
             f'<stop offset="1" stop-color="{t["c1"]}" stop-opacity="0"/>'
             f'</linearGradient></defs>')
    s.append(f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>')

    # title + repo + provenance (kept top-right so the x-axis band stays clean)
    s.append(f'<text x="{ML}" y="30" font-size="20" font-weight="700" '
             f'fill="{t["fg"]}">Star History</text>')
    s.append(f'<text x="{W-MR}" y="26" font-size="14" text-anchor="end" '
             f'fill="{t["muted"]}">{_esc(repo)}</text>')
    s.append(f'<text x="{W-MR}" y="44" font-size="11" text-anchor="end" '
             f'fill="{t["muted"]}">self-hosted · updated {now.strftime("%Y-%m-%d")}</text>')

    # y grid + labels
    v = 0
    while v <= ytop:
        gy = py(v)
        s.append(f'<line x1="{ML}" y1="{gy:.1f}" x2="{W-MR}" y2="{gy:.1f}" '
                 f'stroke="{t["grid"]}" stroke-width="1"/>')
        s.append(f'<text x="{ML-10}" y="{gy+4:.1f}" font-size="12" '
                 f'text-anchor="end" fill="{t["muted"]}">{v}</text>')
        v += ystep

    # x ticks at month starts
    for d in _month_starts(t0, t1):
        gx = px(d)
        s.append(f'<line x1="{gx:.1f}" y1="{MT}" x2="{gx:.1f}" y2="{H-MB}" '
                 f'stroke="{t["grid"]}" stroke-width="1"/>')
        s.append(f'<text x="{gx:.1f}" y="{H-MB+22}" font-size="12" '
                 f'text-anchor="middle" fill="{t["muted"]}">{d.strftime("%b %Y")}</text>')

    # area + line + end dot
    s.append(f'<polygon points="{area}" fill="url(#ar)"/>')
    s.append(f'<polyline points="{line}" fill="none" stroke="url(#ln)" '
             f'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    ex, ey = px(now), py(total)
    s.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="5" fill="{t["c1"]}" '
             f'stroke="{t["bg"]}" stroke-width="2"/>')
    s.append(f'<text x="{ex-10:.1f}" y="{ey-12:.1f}" font-size="14" '
             f'font-weight="700" text-anchor="end" fill="{t["c1"]}">{total} ★</text>')
    s.append('</svg>')
    return "".join(s)


def _esc(x: str) -> str:
    return (x.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_preview(repo: str) -> str:
    return f"""<!doctype html><meta charset="utf-8">
<title>Star History preview — {_esc(repo)}</title>
<style>
 body{{margin:0;font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;
   background:#f6f8fa;color:#24292f;padding:40px}}
 h1{{font-size:22px}} p{{color:#57606a;max-width:820px;line-height:1.6}}
 .row{{display:flex;gap:24px;flex-wrap:wrap;margin-top:24px}}
 .card{{border-radius:12px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.12)}}
 .card img{{display:block;width:800px;max-width:100%}}
 code{{background:#eaeef2;padding:2px 6px;border-radius:5px}}
</style>
<h1>Star History — self-hosted preview</h1>
<p>Drop-in replacement for the two <code>api.star-history.com</code> srcset URLs
(which 503 on a rate-limited shared token pool). Generated from the repo's own
stargazer timeline via <code>gh</code>. Left = light theme, right = dark theme.</p>
<div class="row">
  <div class="card"><img src="star-history.svg" alt="light"></div>
  <div class="card"><img src="star-history-dark.svg" alt="dark"></div>
</div>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="owner/name")
    ap.add_argument("--out-dir", default=".", type=Path)
    ap.add_argument("--stars-file", type=Path,
                    help="newline ISO timestamps (offline/test; skips gh)")
    a = ap.parse_args()

    if a.stars_file:
        stars = _parse(a.stars_file.read_text().splitlines())
    else:
        stars = fetch_stars(a.repo)
    if not stars:
        print("no stargazers found", file=sys.stderr)
        return 1

    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "star-history.svg").write_text(build_svg(stars, a.repo, "light"))
    (a.out_dir / "star-history-dark.svg").write_text(build_svg(stars, a.repo, "dark"))
    (a.out_dir / "preview.html").write_text(build_preview(a.repo))
    print(f"{len(stars)} stars → {a.out_dir}/star-history{{,-dark}}.svg + preview.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
