#!/usr/bin/env python3
"""
Auto-review paper submissions via Claude API.
Triggered by GitHub Actions when a paper-submission issue is opened.
"""

import os
import json
import subprocess
import anthropic

TAXONOMY = """
Embodied AI Safety Taxonomy (5 layers):

1. PERCEPTION
   - Visual Perception: adversarial patches, object detection attacks, camera spoofing
   - Auditory Perception: voice command attacks, audio adversarial examples
   - Spatial Perception: depth estimation attacks, LiDAR spoofing
   - Motion Perception: optical flow attacks, action recognition robustness
   - Cross-Modal Perception: multi-modal fusion vulnerabilities

2. COGNITION
   - Instruction Understanding: prompt injection, jailbreak on VLMs/LLMs
   - World Model: world model robustness, causal reasoning under attack
   - Reasoning: logical reasoning attacks, chain-of-thought manipulation

3. PLANNING
   - Task Planning: LLM planner jailbreak, goal hijacking
   - Trajectory Planning: motion planning adversarial attacks, path manipulation
   - Multi-Agent Planning: coordination attacks, goal conflicts in multi-agent systems

4. ACTION AND INTERACTION
   - Robot Control: physical adversarial attacks, control policy backdoors
   - Human-Agent Interaction: social engineering, trust manipulation, HRI safety
   - Multi-Agent Collaboration: Byzantine agents, collusion, infection

5. AGENTIC
   - Tool Use and Skill: tool poisoning, malicious API calls, MCP attacks, skill extraction
   - Memory: memory poisoning, retrieval manipulation
   - Self-Evolving: fine-tuning attacks, knowledge editing attacks
   - Cascading Risks: supply chain attacks, emergent multi-agent risks
"""

SYSTEM_PROMPT = f"""You are a senior researcher in embodied AI safety reviewing paper submissions for the survey "Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses."

The survey covers attacks and defenses across the full embodied AI pipeline. Here is the taxonomy:

{TAXONOMY}

Your role is to:
1. Assess relevance to embodied AI safety (not just general ML safety or pure robotics without safety focus)
2. Suggest the correct taxonomy layer and subcategory
3. Give a brief, constructive review

Be direct and helpful. If a paper is clearly off-topic, say so kindly.
"""


def review_paper(title: str, body: str) -> str:
    client = anthropic.Anthropic()

    user_message = f"""Please review this paper submission:

**Issue Title:** {title}

**Submission:**
{body}

Provide:
1. **Relevance**: Is this paper relevant to embodied AI safety? (Yes / Marginal / No) — one sentence explanation
2. **Suggested Layer**: Which taxonomy layer(s) fit best?
3. **Suggested Subcategory**: Which specific subcategory?
4. **Brief Assessment**: 2-3 sentences on why this paper belongs (or doesn't) in the survey
5. **Decision**: Accept / Review Needed / Reject (with reason if rejecting)

Keep the response concise and actionable for the maintainers."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    return message.content[0].text


def post_comment(repo: str, issue_number: str, comment: str, token: str) -> None:
    full_comment = f"""## Automated Paper Review

{comment}

---
*This review was generated automatically by Claude. Maintainers should verify before adding the paper to the list.*
*To add this paper, maintainers can update the relevant CSV or markdown file and close this issue.*"""

    result = subprocess.run(
        [
            "gh", "issue", "comment", issue_number,
            "--repo", repo,
            "--body", full_comment,
        ],
        env={**os.environ, "GH_TOKEN": token},
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gh comment failed: {result.stderr}")


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set")

    title = os.environ.get("ISSUE_TITLE", "")
    body = os.environ.get("ISSUE_BODY", "")
    issue_number = os.environ.get("ISSUE_NUMBER", "")
    repo = os.environ.get("REPO", "")
    token = os.environ.get("GH_TOKEN", "")

    if not all([title, body, issue_number, repo, token]):
        raise ValueError("Missing required environment variables")

    print(f"Reviewing submission: {title}")
    review = review_paper(title, body)
    print(f"Review generated:\n{review}")

    post_comment(repo, issue_number, review, token)
    print(f"Comment posted to issue #{issue_number}")


if __name__ == "__main__":
    main()
