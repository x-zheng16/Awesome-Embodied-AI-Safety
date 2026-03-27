# CLAUDE.md

This file describes the repository structure and contribution workflow for AI agents
(Claude Code, Cursor, Copilot, etc.) working on this project.

## Repository Overview

**Safety in Embodied AI: Risks, Attacks, and Defenses**
A curated Awesome list + survey paper covering 480+ papers on safety across the
full embodied AI pipeline.
GitHub: https://github.com/x-zheng16/Awesome-Embodied-AI-Safety
Project page: https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/

## Repository Structure

```
README.md          # Paper list (source of truth for paper entries)
CLAUDE.md          # This file — agent instructions
paper.pdf          # Survey paper
CITATION.cff       # Machine-readable citation metadata
assets/            # Images used in README and project page
  banner.png
  fig_capability_risk.png
  overview.png
  structure.png
docs/
  index.html       # GitHub Pages project page (single-file, no build step)
.github/
  ISSUE_TEMPLATE/
    paper-submission.md   # Template for contributors submitting papers
  workflows/
    review-paper-submission.yml  # Auto-reviews new paper-submission issues via Claude API
  scripts/
    review_paper.py       # Claude Haiku review logic with taxonomy context
```

## Taxonomy (5 layers)

Every paper in this repository maps to exactly one layer and one subcategory:

| Layer          | Subcategories                                                                 | Papers |
| -------------- | ----------------------------------------------------------------------------- | -----: |
| **Perception** | Visual, Auditory, Spatial, Motion, Cross-Modal                                |    191 |
| **Cognition**  | Instruction Understanding, World Model, Reasoning                             |     32 |
| **Planning**   | Task Planning, Trajectory Planning, Multi-Agent Planning                      |     51 |
| **Action**     | Robot Control, Human-Agent Interaction, Multi-Agent Collaboration             |     92 |
| **Agentic**    | Tool Use, Memory, Self-Evolving, Cascading Risks                              |     71 |

**Taxonomy rationale**: each layer corresponds to a capability stage in the embodied
AI pipeline where introducing new abilities also introduces new attack surfaces.
Perception = sensors; Cognition = understanding; Planning = goal decomposition;
Action = physical execution; Agentic = autonomous tool-use and self-improvement.

## Paper Entry Format (README.md)

Papers live in `README.md` under nested `<details>` accordions.
The structure is:

```markdown
<details open>
<summary><b>Perception</b> (N papers)</summary>

<details>
<summary>Visual Perception (N)</summary>

- [Paper Title](https://scholar.google.com/scholar?q=...). Author1, Author2. *Venue*, Year.
```

**Format rules**:
- Title links to a Google Scholar search URL (not direct PDF) unless a stable DOI/arXiv URL is available.
- Author format: `LastName, FirstName` (abbreviated if >3 authors use "et al.").
- Venue in italics: conference acronym (e.g., `*CVPR*`, `*NeurIPS*`) or `*arXiv XXXX.XXXXX*`.
- Year at the end, no period after the year.
- One paper per line; entries within a subcategory are not ordered.

## How to Add a Paper

1. Identify the correct layer and subcategory using the taxonomy above.
2. Format the entry as shown above.
3. Insert it under the appropriate `<details>` section in `README.md`.
4. Update the paper count in the `<summary>` tag for that subcategory.
5. Update the layer-level count in the `<summary>` tag.
6. Update the count in the table at the top of `## Surveyed Papers`.
7. Open a PR — the GitHub Action will auto-review if you use the `paper-submission` issue first.

## Automated Paper Review

When a contributor opens an issue using the **paper-submission** template and the
`paper-submission` label is applied, a GitHub Action triggers automatically:
- Calls Claude Haiku with the full taxonomy as context.
- Assesses relevance (Yes / Marginal / No) and suggests the best layer + subcategory.
- Posts the review as an issue comment within ~30 seconds.
- Maintainers can approve and close the issue after adding the paper to README.md.

To enable: add `ANTHROPIC_API_KEY` to repo Settings → Secrets → Actions.

## Project Page (docs/index.html)

The project page is a single self-contained HTML file served via GitHub Pages from
the `docs/` folder on `main`.
- No build step — edit `docs/index.html` directly.
- All asset paths use absolute `raw.githubusercontent.com` URLs (not relative `../assets/`).
- Fonts: Crimson Pro (headings) + Atkinson Hyperlegible (body) via Google Fonts.
- Do not add JavaScript frameworks or build dependencies.
- To update paper counts or add sections, edit the HTML directly.

## Contribution Guidelines for Agents

When helping a user contribute to this repository:

1. **Adding a paper**: read the taxonomy table, pick the most specific subcategory,
   format the entry, insert in the right `<details>` block, update all counts.

2. **Updating paper counts**: counts appear in three places — the subcategory
   `<summary>`, the layer `<summary>`, and the summary table. Update all three.

3. **Updating the project page**: the stats strip in `docs/index.html` shows
   aggregate counts — update them when total paper count changes significantly.

4. **Do not modify**: `paper.pdf`, `CITATION.cff`, `assets/` images, or
   `.github/workflows/` without explicit maintainer approval.

5. **Branch naming**: `feat/add-<topic>-papers` for new papers,
   `fix/<description>` for corrections, `docs/<description>` for page updates.

## Citation

```bibtex
@article{li2026safety,
  title={Safety in Embodied AI: Risks, Attacks, and Defenses},
  author={Li, Xiao and Zheng, Xiang and Gao, Yifeng and others},
  year={2026},
  url={https://github.com/x-zheng16/Awesome-Embodied-AI-Safety}
}
```
