"""
PR Issue Checker — powered by free Gemini API
Repo: Rahul-pamula/DBMS

What this does:
  1. Gets all open PRs (or the specific PR that triggered this run)
  2. Finds which issue each PR is linked to (via "Fixes #N" in PR body)
  3. Reads that issue's description
  4. Reads the PR's code diff
  5. Asks Gemini: "Does this code actually solve the issue?"
  6. Posts the verdict as a comment on the PR
"""

import os
import re
import sys
import requests

# ── Config from environment ───────────────────────────────────────────────────
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GITHUB_TOKEN   = os.environ.get("GITHUB_TOKEN")
REPO           = os.environ.get("REPO", "Rahul-pamula/DBMS")
PR_NUMBER      = os.environ.get("PR_NUMBER")  # only set when triggered by a PR event

# Validate required env vars
if not GEMINI_API_KEY:
    print("❌ ERROR: GEMINI_API_KEY secret is not set in GitHub repo settings.")
    sys.exit(1)

if not GITHUB_TOKEN:
    print("❌ ERROR: GITHUB_TOKEN not available.")
    sys.exit(1)

GH_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
)


# ── Helper: Post a comment on a PR ───────────────────────────────────────────
def post_comment(pr_num, body):
    url = f"https://api.github.com/repos/{REPO}/issues/{pr_num}/comments"
    response = requests.post(url, headers=GH_HEADERS, json={"body": body})
    if response.status_code == 201:
        print(f"  ✅ Comment posted on PR #{pr_num}")
    else:
        print(f"  ❌ Failed to post comment: {response.status_code} — {response.text}")


# ── Helper: Ask Gemini a question ────────────────────────────────────────────
def ask_gemini(prompt):
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 600,
            "temperature": 0.2   # lower = more consistent/factual
        }
    }
    response = requests.post(GEMINI_URL, json=payload)

    if response.status_code != 200:
        print(f"  ❌ Gemini API error: {response.status_code} — {response.text}")
        return None

    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        print(f"  ❌ Unexpected Gemini response format: {data}")
        return None


# ── Step 1: Get PRs to check ─────────────────────────────────────────────────
print(f"\n🔍 PR Issue Checker starting for repo: {REPO}")

if PR_NUMBER and PR_NUMBER != "":
    # Triggered by a specific PR event
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
    pr_data = requests.get(url, headers=GH_HEADERS).json()
    prs = [pr_data]
    print(f"📋 Checking triggered PR #{PR_NUMBER}")
else:
    # Scheduled run — check all open PRs
    url = f"https://api.github.com/repos/{REPO}/pulls?state=open&per_page=20"
    prs = requests.get(url, headers=GH_HEADERS).json()
    print(f"📋 Found {len(prs)} open PR(s) to check")

if not prs:
    print("✅ No open PRs to check. All done!")
    sys.exit(0)


# ── Process each PR ──────────────────────────────────────────────────────────
for pr in prs:
    pr_num   = pr.get("number")
    pr_title = pr.get("title", "No title")
    pr_body  = pr.get("body") or ""
    pr_author = pr.get("user", {}).get("login", "unknown")

    print(f"\n{'─'*60}")
    print(f"🔎 PR #{pr_num}: {pr_title} (by @{pr_author})")

    # ── Step 2: Find linked issue ─────────────────────────────────────────────
    issue_match = re.search(
        r"(?:fix(?:es|ed)?|close[sd]?|resolve[sd]?)\s*#(\d+)",
        pr_body,
        re.IGNORECASE
    )

    if not issue_match:
        print(f"  ⚠️  No linked issue found in PR body")
        comment = f"""## 🤖 PR Review Bot

Hi @{pr_author}! 👋

I noticed this PR doesn't have a linked issue.

**Please add one of these to your PR description:**
```
Fixes #<issue-number>
Closes #<issue-number>
Resolves #<issue-number>
```

This helps me automatically verify your solution matches the problem. Without it, I can't do an automated review.

---
_Automated check by PR Issue Checker bot_"""
        post_comment(pr_num, comment)
        continue

    issue_number = issue_match.group(1)
    print(f"  🔗 Linked to Issue #{issue_number}")

    # ── Step 3: Get issue details ─────────────────────────────────────────────
    issue_url  = f"https://api.github.com/repos/{REPO}/issues/{issue_number}"
    issue_resp = requests.get(issue_url, headers=GH_HEADERS)

    if issue_resp.status_code != 200:
        print(f"  ❌ Could not fetch issue #{issue_number}: {issue_resp.status_code}")
        continue

    issue_data  = issue_resp.json()
    issue_title = issue_data.get("title", "No title")
    issue_body  = issue_data.get("body") or "No description provided"
    print(f"  📝 Issue: {issue_title}")

    # ── Step 4: Get PR diff ───────────────────────────────────────────────────
    diff_headers = {**GH_HEADERS, "Accept": "application/vnd.github.diff"}
    diff_url     = f"https://api.github.com/repos/{REPO}/pulls/{pr_num}"
    diff_resp    = requests.get(diff_url, headers=diff_headers)
    diff_text    = diff_resp.text[:6000]  # limit to avoid token overflow

    if not diff_text.strip():
        diff_text = "No diff available (possibly an empty PR or large binary files)"

    print(f"  📄 Got diff ({len(diff_text)} chars)")

    # ── Step 5: Ask Gemini ────────────────────────────────────────────────────
    print(f"  🤖 Asking Gemini to analyze...")

    prompt = f"""You are a helpful code reviewer for a DBMS (Database Management Systems) course repository.

A student has submitted a Pull Request claiming to solve a GitHub Issue. Your job is to check if the PR actually solves the issue.

---
## GitHub Issue #{issue_number}
**Title:** {issue_title}
**Description:**
{issue_body[:2000]}

---
## Pull Request #{pr_num}
**Title:** {pr_title}
**Author:** @{pr_author}
**PR Description:**
{pr_body[:1000]}

---
## Code Changes (Diff)
```diff
{diff_text}
```

---
## Your Task
Analyze whether this PR solves the issue. Be student-friendly and encouraging.

Respond in exactly this format:

**Verdict:** [SOLVED / PARTIAL / UNRELATED / NEEDS_REVIEW]

**Summary:** (1-2 sentences: what the PR does and how it relates to the issue)

**Feedback:** (2-3 sentences of constructive feedback for the student)

**Next Steps:** (1-2 sentences on what the maintainer should do, or what the student should improve)

Use these verdict definitions:
- SOLVED: PR clearly and completely addresses what the issue asked
- PARTIAL: PR is on the right track but missing something important
- UNRELATED: PR changes don't match what the issue requested
- NEEDS_REVIEW: Cannot determine automatically — needs human review
"""

    gemini_result = ask_gemini(prompt)

    if not gemini_result:
        print(f"  ❌ Gemini returned no result, skipping PR #{pr_num}")
        continue

    print(f"  ✨ Gemini analysis complete")

    # Determine emoji based on verdict
    verdict_emoji = "❓"
    if "SOLVED" in gemini_result:
        verdict_emoji = "✅"
    elif "PARTIAL" in gemini_result:
        verdict_emoji = "⚠️"
    elif "UNRELATED" in gemini_result:
        verdict_emoji = "❌"
    elif "NEEDS_REVIEW" in gemini_result:
        verdict_emoji = "👀"

    # ── Step 6: Post comment on PR ────────────────────────────────────────────
    full_comment = f"""## {verdict_emoji} Automated PR Review

> Checking if this PR solves Issue #{issue_number}: _{issue_title}_

{gemini_result}

---
<details>
<summary>ℹ️ About this bot</summary>

This automated review is generated by the PR Issue Checker using Google Gemini AI.
It checks whether your code changes match the issue requirements.

**This is NOT the final decision** — a human maintainer (@Rahul-pamula) will make the final call on merging.

If you think this review is wrong, just explain in a comment below.
</details>"""

    post_comment(pr_num, full_comment)


print(f"\n{'─'*60}")
print("✅ PR Issue Checker complete!")
