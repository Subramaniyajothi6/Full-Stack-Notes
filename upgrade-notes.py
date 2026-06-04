"""
upgrade-notes.py

Walks every .md note in the vault and appends any missing template sections
so every note has the same structure:

    Prerequisites
    What To Learn Next
    Real World Usage
    Common Mistakes
    Best Learning Resources
        Official Documentation
        Best YouTube Resource
        Best Free Course
        Best Advanced Resource
        Best Practice Project
        Recommended Order to Learn
    Interview Questions

A note is upgraded only if it is missing one of those sections (case-insensitive
heading match). Notes that already have all sections are skipped.

Skips: MOCs, Interview Banks, Roadmap files. Compatible with both pre-refactor
and post-refactor folder layouts.

USAGE
-----
    python upgrade-notes.py            # dry-run, prints what would change
    python upgrade-notes.py --apply    # actually edit files
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent

REQUIRED_SECTIONS = [
    "Prerequisites",
    "What To Learn Next",
    "Real World Usage",
    "Common Mistakes",
    "Best Learning Resources",
    "Interview Questions",
]

# Topic-aware default doc + youtube hints, keyed by stack folder name
# (works both pre- and post-refactor: the script picks the second-to-last
# path segment, e.g. "JavaScript" from "9 Full Stack Infra/JavaScript/Topics/x.md")
SECTION_HINTS: dict[str, dict[str, str]] = {
    "JavaScript":   {"docs": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
                     "youtube": "Web Dev Simplified, Fireship, The Net Ninja"},
    "TypeScript":   {"docs": "https://www.typescriptlang.org/docs/handbook/intro.html",
                     "youtube": "Matt Pocock, Theo, Jack Herrington"},
    "React":        {"docs": "https://react.dev/",
                     "youtube": "Jack Herrington, Theo, Web Dev Simplified"},
    "NextJS":       {"docs": "https://nextjs.org/docs",
                     "youtube": "Lee Robinson, Theo, Jack Herrington"},
    "NodeJS":       {"docs": "https://nodejs.org/en/docs",
                     "youtube": "Hussein Nasser, TechWorld with Nana, Traversy Media"},
    "Express":      {"docs": "https://expressjs.com/",
                     "youtube": "Web Dev Simplified, Traversy Media"},
    "MongoDB":      {"docs": "https://www.mongodb.com/docs/",
                     "youtube": "Hussein Nasser, MongoDB official"},
    "PostgreSQL":   {"docs": "https://www.postgresql.org/docs/",
                     "youtube": "Hussein Nasser"},
    "Redis":        {"docs": "https://redis.io/docs/",
                     "youtube": "Hussein Nasser, ByteByteGo"},
    "Vector Databases": {"docs": "https://www.pinecone.io/learn/",
                         "youtube": "James Briggs, Greg Kamradt"},
    "Networking":   {"docs": "https://developer.mozilla.org/en-US/docs/Web/HTTP",
                     "youtube": "Hussein Nasser, ByteByteGo"},
    "System Design":{"docs": "https://aws.amazon.com/architecture/",
                     "youtube": "ByteByteGo, Hussein Nasser"},
    "Security":     {"docs": "https://owasp.org/",
                     "youtube": "Hussein Nasser, John Hammond"},
    "DevOps":       {"docs": "https://kubernetes.io/docs/, https://www.terraform.io/docs",
                     "youtube": "TechWorld with Nana, Anton Putra"},
    "Cloud":        {"docs": "https://docs.aws.amazon.com/",
                     "youtube": "Stephane Maarek, TechWorld with Nana"},
    "Docker":       {"docs": "https://docs.docker.com/",
                     "youtube": "TechWorld with Nana, Bret Fisher"},
    "CI-CD":        {"docs": "https://docs.github.com/en/actions",
                     "youtube": "TechWorld with Nana, Anton Putra"},
    "Testing":      {"docs": "https://playwright.dev/, https://vitest.dev/",
                     "youtube": "Web Dev Simplified, Kent C. Dodds"},
    "AI Engineering": {"docs": "https://docs.anthropic.com/, https://platform.openai.com/docs",
                       "youtube": "Theo, Greg Kamradt, James Briggs"},
    "AI SDKs":      {"docs": "https://sdk.vercel.ai/docs",
                     "youtube": "Theo, Lee Robinson"},
    "RAG":          {"docs": "https://www.pinecone.io/learn/retrieval-augmented-generation/",
                     "youtube": "Greg Kamradt, James Briggs"},
    "AI Agents":    {"docs": "https://www.anthropic.com/research/building-effective-agents",
                     "youtube": "Greg Kamradt, Theo"},
    "Go":           {"docs": "https://go.dev/doc/",
                     "youtube": "Anthony GG, TechWorld with Nana"},
    "Rust":         {"docs": "https://doc.rust-lang.org/book/",
                     "youtube": "Jon Gjengset, Let's Get Rusty"},
    "CLI & Terminal": {"docs": "https://www.gnu.org/software/bash/manual/",
                       "youtube": "The Primeagen, TechWorld with Nana"},
    "Browser DevTools": {"docs": "https://developer.chrome.com/docs/devtools",
                        "youtube": "Umar Hansa, Web Dev Simplified"},
    "Git & GitHub": {"docs": "https://git-scm.com/doc",
                     "youtube": "The Net Ninja, Fireship"},
    "MERN Stack":   {"docs": "Stack-specific docs",
                     "youtube": "Traversy Media, Web Dev Simplified"},

    # Pre-refactor folder names — same hints
    "1 JavaScript":         {"docs": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
                             "youtube": "Web Dev Simplified, Fireship"},
    "2 React":              {"docs": "https://react.dev/",
                             "youtube": "Jack Herrington, Theo"},
    "3 NodeJS":             {"docs": "https://nodejs.org/en/docs",
                             "youtube": "Hussein Nasser, TechWorld with Nana"},
    "4 Express":            {"docs": "https://expressjs.com/",
                             "youtube": "Web Dev Simplified"},
    "5 MongoDB":            {"docs": "https://www.mongodb.com/docs/",
                             "youtube": "Hussein Nasser"},
    "6 System Design":      {"docs": "https://aws.amazon.com/architecture/",
                             "youtube": "ByteByteGo"},
    "7 Projects":           {"docs": "Project-specific docs",
                             "youtube": "Project-specific tutorials"},
    "8 Interview Questions":{"docs": "Topic-specific docs",
                             "youtube": "ByteByteGo, Tech Dummies"},
}

SKIP_SUBSTRINGS = ["MOC.md", "Interview Bank.md", "Roadmap"]

HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")


def find_notes() -> list[Path]:
    notes: list[Path] = []
    for p in VAULT_ROOT.rglob("*.md"):
        if any(seg.startswith(".") for seg in p.relative_to(VAULT_ROOT).parts):
            continue
        if any(s in p.name for s in SKIP_SUBSTRINGS):
            continue
        notes.append(p)
    return notes


def existing_headings(text: str) -> set[str]:
    found: set[str] = set()
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            found.add(m.group(1).strip().lower())
    return found


def stack_for(note: Path) -> str:
    """
    Best-effort detection of the owning stack from path.
    Tries (innermost-meaningful → outermost) so it works both before & after refactor.
    """
    parts = note.relative_to(VAULT_ROOT).parts
    # Post-refactor: 9 Full Stack Infra / <Stack> / Topics|... / file.md
    if len(parts) >= 3 and parts[0] == "9 Full Stack Infra":
        return parts[1]
    # Pre-refactor: <numbered folder> / file.md
    if len(parts) >= 2:
        return parts[0]
    return ""


def template_block(note: Path, missing: list[str]) -> str:
    sect = stack_for(note)
    hints = SECTION_HINTS.get(sect, {"docs": "", "youtube": ""})
    out = ["", "<!-- upgrade-notes.py auto-appended -->"]

    for s in missing:
        out.append(f"\n## {s}")
        if s == "Prerequisites":
            out.append("- TODO: link prerequisite notes")
        elif s == "What To Learn Next":
            out.append("- TODO: link follow-up notes")
        elif s == "Real World Usage":
            out.append("- TODO: where this concept appears in production")
        elif s == "Common Mistakes":
            out.append("- TODO: pitfalls and edge cases")
        elif s == "Interview Questions":
            out.append("**Q. TODO** — A. ...")
            out.append("\n**Q. TODO** — A. ...")
        elif s == "Best Learning Resources":
            out.append(f"\n### Official Documentation\n- {hints['docs']} — TODO: pick the most relevant page and say why")
            out.append(f"\n### Best YouTube Resource\n- TODO: e.g. {hints['youtube']}")
            out.append("\n### Best Free Course\n- TODO")
            out.append("\n### Best Advanced Resource\n- TODO")
            out.append("\n### Best Practice Project\n- TODO: 1-paragraph project idea")
            out.append("\n### Recommended Order to Learn\n1. TODO\n2. TODO\n3. TODO")
    return "\n".join(out) + "\n"


def upgrade_note(note: Path, apply: bool) -> bool:
    text = note.read_text(encoding="utf-8", errors="ignore")
    have = existing_headings(text)
    missing = [s for s in REQUIRED_SECTIONS if s.lower() not in have]
    if not missing:
        return False
    block = template_block(note, missing)
    if apply:
        note.write_text(text.rstrip() + "\n" + block, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="actually write changes")
    args = ap.parse_args()

    notes = find_notes()
    print(f"Scanning {len(notes)} notes…")
    changed = 0
    for n in notes:
        if upgrade_note(n, apply=args.apply):
            print(f"  {'updated' if args.apply else 'would update'}: {n.relative_to(VAULT_ROOT)}")
            changed += 1
    print(f"\n{'Updated' if args.apply else 'Would update'} {changed}/{len(notes)} notes.")
    if not args.apply:
        print("Run again with --apply to write changes.")


if __name__ == "__main__":
    main()
