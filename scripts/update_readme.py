#!/usr/bin/env python3
"""Regenerate the Progress and Problem Index blocks of README.md from stats.json.

Run from anywhere inside the repo:  python3 scripts/update_readme.py
Only the blocks between the START/END markers are rewritten, so any other
hand-written README content is preserved.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
STATS = ROOT / "stats.json"

PROGRESS_START = "<!--PROGRESS:START-->"
PROGRESS_END = "<!--PROGRESS:END-->"
INDEX_START = "<!--INDEX:START-->"
INDEX_END = "<!--INDEX:END-->"

DIFF_LABEL = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
MAX_APPROACH = 90


def build_progress(stats):
    s = stats.get("leetcode", {})
    return "**{} solved** · {} Easy · {} Medium · {} Hard".format(
        s.get("solved", 0), s.get("easy", 0), s.get("medium", 0), s.get("hard", 0)
    )


def solution_language(folder):
    for ext, name in ((".java", "Java"), (".py", "Python")):
        if any(f.suffix == ext for f in folder.iterdir()):
            return name
    return "?"


def problem_title(folder):
    readme = folder / "README.md"
    if readme.exists():
        m = re.search(r"<h2><a href=\"https://leetcode\.com/problems/[^\"]+\">([^<]+)</a></h2>", readme.read_text(errors="ignore"))
        if m:
            return m.group(1).strip()
    return folder.name[5:].replace("-", " ").title()


def approach_text(folder):
    readme = folder / "README.md"
    if readme.exists():
        m = re.search(r"## Approach\s*\n\s*(.+)", readme.read_text(errors="ignore"))
        if m:
            text = m.group(1).strip()
            return text if len(text) <= MAX_APPROACH else text[:MAX_APPROACH - 1] + "…"
    return ""


def build_index(stats):
    shas = stats.get("leetcode", {}).get("shas", {})
    rows = [
        "| # | Problem | Difficulty | Language | Approach |",
        "|---|---------|------------|----------|----------|",
    ]
    folders = sorted(p for p in ROOT.iterdir() if p.is_dir() and re.fullmatch(r"\d{4}-[\w-]+", p.name))
    for folder in folders:
        number = str(int(folder.name[:4]))
        slug = folder.name
        diff = DIFF_LABEL.get(shas.get(slug, {}).get("difficulty", ""), "?")
        title = problem_title(folder)
        approach = approach_text(folder).replace("|", "\\|")
        rows.append("| {} | [{}]({}/) | {} | {} | {} |".format(number, title, slug, diff, solution_language(folder), approach))
    return "\n".join(rows)


def replace_block(text, start, end, replacement):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(start + "\n" + replacement + "\n" + end, text)


def main():
    if not STATS.exists() or not README.exists():
        return
    stats = json.loads(STATS.read_text(errors="ignore"))
    readme = README.read_text(errors="ignore")
    readme = replace_block(readme, PROGRESS_START, PROGRESS_END, build_progress(stats))
    readme = replace_block(readme, INDEX_START, INDEX_END, build_index(stats))
    README.write_text(readme)


if __name__ == "__main__":
    main()
