"""
PR Issue Checker — L3 (Auto-merge capable)
Repo: Rahul-pamula/DBMS

Tier: L3 — Can merge PRs automatically

What this does:
  1. Gets all open PRs (or the specific PR that triggered this run)
  2. Finds which issue each PR is linked to (via "Fixes #N" in PR body)
  3. Reads that issue + the PR diff
  4. Asks Gemini: "Does this code actually solve the issue?"
  5. Posts the verdict as a comment on the PR
  6. [L3] If verdict = SOLVED + no conflicts + CI passing → merges automatically

Merge safety gates (ALL must pass before merge):
  ✅ Gemini verdict must be SOLVED (not PARTIAL/UNRELATED)
  ✅ PR must not have merge conflicts (mergeable = true)
  ✅ PR must be open (not already closed/merged)
  ✅ CI checks must be passing (if any exist)
  ✅ PR must be at least 10 minutes old (not brand new)

NEVER merges if:
  ❌ Verdict is PARTIAL, UNRELATED, or NEEDS_REVIEW
  ❌ There are merge conflicts
  ❌ CI is failing
  ❌ PR was just opened (< 10 min old) — gives CodeRabbit time to review
"""

import os
import re
import sys
import time
import requests
from datetime import datetime, timezone

# ── Config ─────────────────────────────────────────────────────────────────────
GEMINI_API_KEY  = os.environ.get("GEMINI_API_KEY")
GITHUB_TOKEN    = os.environ.get("GITHUB_TOKEN")
REPO            = os.environ.get("REPO", "Rahul-pamula/DBMS")
PR_NUMBER       = os.environ.get("PR_NUMBER")   # set only on PR-triggered runs
AUTO_MERGE      = os.environ.get("AUTO_MERGE", "true").lower() == "true"
MIN_AGE_MINUTES = 10  # PR must be this old before auto-merge kicks in

# Validate
if not GEMINI_API_KEY:
    print("❌ ERROR: GEMINI_API_KEY secret is missing in GitHub repo settings.")
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
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
)


# ── Helper: Post a comment on a PR ─────────────────────────────────────────────
def post_comment(pr_num, body):
    url = f"https://api.github.com/repos/{REPO}/issues/{pr_num}/comments"
    r = requests.post(url, headers=GH_HEADERS, json={"body": body})
    if r.status_code == 201:
        print(f"  ✅ Comment posted on PR #{pr_num}")
    else:
        print(f"  ❌ Failed to post comment: {r.status_code} — {r.text[:200]}")


# ── Helper: Ask Gemini ──────────────────────────────────────────────────────────
def ask_gemini(prompt):
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 600,
            "temperature": 0.2
        }
    }
    r = requests.post(GEMINI_URL, json=payload)
    if r.status_code != 200:
        print(f"  ❌ Gemini API error: {r.status_code} — {r.text[:200]}")
        return None
    try:
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError) as e:
        print(f"  ❌ Unexpected Gemini response: {e}")
        return None


# ── Helper: Check CI status ─────────────────────────────────────────────────────
def get_ci_status(pr_head_sha):
    """
    Returns: "passing", "failing", "pending", or "no_checks"
    """
    url = f"https://api.github.com/repos/{REPO}/commits/{pr_head_sha}/check-runs"
    r = requests.get(url, headers=GH_HEADERS)
    if r.status_code != 200:
        return "no_checks"

    runs = r.json().get("check_runs", [])
    if not runs:
        return "no_checks"

    statuses = [run["conclusion"] for run in runs if run["status"] == "completed"]
    in_progress = [run for run in runs if run["status"] in ("in_progress", "queued")]

    if in_progress:
        return "pending"
    if any(s in ("failure", "cancelled", "timed_out") for s in statuses):
        return "failing"
    if all(s in ("success", "skipped", "neutral") for s in statuses):
        return "passing"

    return "pending"


# ── Helper: Get PR age in minutes ───────────────────────────────────────────────
def get_pr_age_minutes(created_at_str):
    created = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    return (now - created).total_seconds() / 60


# ── Helper: Merge a PR ──────────────────────────────────────────────────────────
def merge_pr(pr_num, pr_title, issue_number):
    url = f"https://api.github.com/repos/{REPO}/pulls/{pr_num}/merge"
    payload = {
        "commit_title": f"feat: {pr_title} (closes #{issue_number})",
        "commit_message": (
            f"Auto-merged by PR Issue Checker bot.\n\n"
            f"Verdict: SOLVED — Gemini confirmed this PR resolves issue #{issue_number}.\n"
            f"CI: passing. No merge conflicts."
        ),
        "merge_method": "squash"   # squash = clean single commit
    }
    r = requests.put(url, headers=GH_HEADERS, json=payload)

    if r.status_code == 200:
        print(f"  🎉 PR #{pr_num} MERGED successfully!")
        return True
    else:
        print(f"  ❌ Merge failed: {r.status_code} — {r.text[:300]}")
        return False


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

print(f"\n{'═'*60}")
print(f"🤖 PR Issue Checker (L3) — Repo: {REPO}")
print(f"{'═'*60}")

# ── Step 1: Get PRs ────────────────────────────────────────────────────────────
if PR_NUMBER and PR_NUMBER != "":
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
    pr_data = requests.get(url, headers=GH_HEADERS).json()
    prs = [pr_data]
    print(f"📋 PR-triggered run — checking PR #{PR_NUMBER}")
else:
    url = f"https://api.github.com/repos/{REPO}/pulls?state=open&per_page=20"
    prs = requests.get(url, headers=GH_HEADERS).json()
    print(f"📋 Scheduled run — found {len(prs)} open PR(s)")

if not prs:
    print("✅ No open PRs. Nothing to do.")
    sys.exit(0)


# ── Process each PR ────────────────────────────────────────────────────────────
for pr in prs:
    pr_num       = pr.get("number")
    pr_title     = pr.get("title", "No title")
    pr_body      = pr.get("body") or ""
    pr_author    = pr.get("user", {}).get("login", "unknown")
    pr_state     = pr.get("state", "")
    pr_merged    = pr.get("merged", False)
    pr_mergeable = pr.get("mergeable")           # True/False/None
    pr_head_sha  = pr.get("head", {}).get("sha", "")
    pr_created   = pr.get("created_at", "")

    print(f"\n{'─'*60}")
    print(f"🔎 PR #{pr_num}: {pr_title}")
    print(f"   Author: @{pr_author} | State: {pr_state}")

    # Skip already merged PRs
    if pr_merged or pr_state == "closed":
        print(f"  ⏭️  Already merged/closed. Skipping.")
        continue

    # ── Step 2: Find linked issue ───────────────────────────────────────────────
    issue_match = re.search(
        r"(?:fix(?:es|ed)?|close[sd]?|resolve[sd]?)\s*#(\d+)",
        pr_body, re.IGNORECASE
    )

    if not issue_match:
        print(f"  ⚠️  No linked issue found")
        post_comment(pr_num, f"""## 🤖 PR Review Bot

Hi @{pr_author}! 👋

This PR has **no linked issue**. I can't verify it or merge it without one.

**Please add to your PR description:**
```
Fixes #<issue-number>
```

---
_Automated check — L3 PR Issue Checker_""")
        continue

    issue_number = issue_match.group(1)
    print(f"  🔗 Linked to Issue #{issue_number}")

    # ── Step 3: Read the issue ──────────────────────────────────────────────────
    issue_resp = requests.get(
        f"https://api.github.com/repos/{REPO}/issues/{issue_number}",
        headers=GH_HEADERS
    )
    if issue_resp.status_code != 200:
        print(f"  ❌ Cannot fetch issue #{issue_number}")
        continue

    issue_data  = issue_resp.json()
    issue_title = issue_data.get("title", "No title")
    issue_body  = issue_data.get("body") or "No description"
    print(f"  📝 Issue: {issue_title}")

    # ── Step 4: Read PR diff ────────────────────────────────────────────────────
    diff_resp = requests.get(
        f"https://api.github.com/repos/{REPO}/pulls/{pr_num}",
        headers={**GH_HEADERS, "Accept": "application/vnd.github.diff"}
    )
    diff_text = diff_resp.text[:6000]
    if not diff_text.strip():
        diff_text = "No diff available."
    print(f"  📄 Diff: {len(diff_text)} chars")

    # ── Step 5: Ask Gemini ──────────────────────────────────────────────────────
    print(f"  🤖 Asking Gemini...")

    prompt = f"""You are a code reviewer for a DBMS (Database Management Systems) course repository.
A student submitted a PR claiming to solve a GitHub Issue.
Check if the PR actually and completely solves the issue.

---
## GitHub Issue #{issue_number}
Title: {issue_title}
Description: {issue_body[:2000]}

---
## Pull Request #{pr_num}
Title: {pr_title}
Author: @{pr_author}
Description: {pr_body[:800]}

---
## Code Diff
```diff
{diff_text}
```

---
## Instructions
Be encouraging but accurate. Respond in EXACTLY this format (no extra text before/after):

**Verdict:** SOLVED

**Summary:** (1-2 sentences what the PR does and how it relates to the issue)

**Feedback:** (2-3 sentences of constructive, student-friendly feedback)

**Next Steps:** (what the maintainer should do OR what student should fix)

Verdict options:
- SOLVED: PR completely and correctly addresses the issue — safe to merge
- PARTIAL: Right idea but something important is missing — do NOT merge yet
- UNRELATED: Code changes don't match the issue — do NOT merge
- NEEDS_REVIEW: Cannot determine automatically — needs human review
"""

    gemini_result = ask_gemini(prompt)
    if not gemini_result:
        print(f"  ❌ No Gemini result. Skipping.")
        continue

    # Extract verdict
    verdict_match = re.search(r"\*\*Verdict:\*\*\s*(SOLVED|PARTIAL|UNRELATED|NEEDS_REVIEW)", gemini_result)
    verdict = verdict_match.group(1) if verdict_match else "NEEDS_REVIEW"

    verdict_emoji = {
        "SOLVED":       "✅",
        "PARTIAL":      "⚠️",
        "UNRELATED":    "❌",
        "NEEDS_REVIEW": "👀"
    }.get(verdict, "❓")

    print(f"  {verdict_emoji} Gemini verdict: {verdict}")

    # ── Step 6: Determine if we can merge (L3 gate) ─────────────────────────────
    can_merge   = False
    merge_block = []   # reasons we cannot merge

    if verdict != "SOLVED":
        merge_block.append(f"Verdict is {verdict} (must be SOLVED)")

    # Check PR age
    if pr_created:
        age_minutes = get_pr_age_minutes(pr_created)
        print(f"  ⏱️  PR age: {age_minutes:.1f} minutes")
        if age_minutes < MIN_AGE_MINUTES:
            merge_block.append(
                f"PR is too new ({age_minutes:.0f} min old — waiting {MIN_AGE_MINUTES} min min)"
            )

    # Check merge conflicts
    if pr_mergeable is False:
        merge_block.append("PR has merge conflicts")
    elif pr_mergeable is None:
        merge_block.append("Mergeability unknown (GitHub still computing)")

    # Check CI
    ci_status = get_ci_status(pr_head_sha)
    print(f"  🔄 CI status: {ci_status}")
    if ci_status == "failing":
        merge_block.append("CI checks are failing")
    elif ci_status == "pending":
        merge_block.append("CI checks are still running")
    # "no_checks" or "passing" → OK to proceed

    can_merge = (verdict == "SOLVED") and (len(merge_block) == 0)

    # ── Step 7: Build and post comment ─────────────────────────────────────────
    if can_merge and AUTO_MERGE:
        merge_section = f"""
### 🚀 Auto-Merge Decision
All safety gates passed:
- ✅ Verdict: SOLVED
- ✅ No merge conflicts
- ✅ CI: {ci_status}
- ✅ PR age OK

**Merging now via squash commit...**"""
    elif not can_merge:
        block_list = "\n".join(f"  - ❌ {r}" for r in merge_block)
        merge_section = f"""
### 🔒 Auto-Merge Blocked
Cannot merge yet because:
{block_list}

Fix these and the bot will merge automatically on the next check."""
    else:
        merge_section = "\n### ℹ️ Auto-merge is disabled in this run."

    full_comment = f"""## {verdict_emoji} Automated PR Review (L3 Bot)

> Checking if PR #{pr_num} solves Issue #{issue_number}: _{issue_title}_

{gemini_result}

---
{merge_section}

---
<details>
<summary>ℹ️ About this bot</summary>

**Tier:** L3 — Can read, review, and merge PRs  
**AI:** Google Gemini 2.0 Flash (free tier)  
**Code review:** CodeRabbit handles code quality  
**This bot handles:** Issue-solution matching + merge decision  

The final merge happens only if:
✅ Gemini says SOLVED &nbsp; ✅ No conflicts &nbsp; ✅ CI passing &nbsp; ✅ PR is 10+ min old

Maintainer: @Rahul-pamula always has override authority.
</details>"""

    post_comment(pr_num, full_comment)

    # ── Step 8: Execute merge ───────────────────────────────────────────────────
    if can_merge and AUTO_MERGE:
        print(f"  🚀 All gates passed. Merging PR #{pr_num}...")
        time.sleep(2)   # small pause before merge
        merged = merge_pr(pr_num, pr_title, issue_number)

        if merged:
            # Post a success message
            post_comment(pr_num, f"""## 🎉 Merged!

PR #{pr_num} has been automatically merged into `main`.

Great work @{pr_author}! Issue #{issue_number} is now resolved. ✨

---
_Merged by PR Issue Checker bot (L3)_""")
        else:
            post_comment(pr_num, f"""## ⚠️ Merge Failed

The bot tried to merge but something went wrong. @Rahul-pamula please merge manually.

---
_PR Issue Checker bot (L3)_""")
    else:
        print(f"  ⏸️  Merge skipped — gates not passed or AUTO_MERGE=false")


print(f"\n{'═'*60}")
print("✅ PR Issue Checker (L3) complete!")
print(f"{'═'*60}\n")
