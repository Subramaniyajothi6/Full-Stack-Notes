"""
refactor-vault.py
=================

Reorganizes this Obsidian vault into a clean modular architecture under
`9 Full Stack Infra/`. Idempotent — safe to run twice.

ARCHITECTURE (target)
---------------------
9 Full Stack Infra/
  ├── JavaScript/          ← existing notes moved (preserved as-is)
  ├── React/               ← existing notes moved
  ├── NodeJS/              ← existing notes moved
  ├── Express/             ← existing notes moved
  ├── MongoDB/             ← existing notes moved
  ├── System Design/       ← existing notes moved
  ├── Projects/            ← existing notes moved
  ├── Interview Questions/ ← existing notes moved
  │
  ├── TypeScript/          ← NEW (gets the existing TypeScript.md)
  ├── NextJS/              ← NEW (App Router, Pages Router, RSC, Convex)
  ├── PostgreSQL/          ← NEW (Postgres + pgvector)
  ├── Redis/               ← NEW
  ├── DevOps/              ← NEW
  ├── Cloud/               ← NEW
  ├── Testing/             ← NEW
  ├── AI Engineering/      ← NEW
  │
  └── MERN Stack/          ← orchestration: MERN Roadmap, integration patterns

WHAT IT DOES
------------
1. Creates each target stack folder under `9 Full Stack Infra/`.
2. Moves existing notes from the numbered folders (1–8) and from the existing
   loose `9 Full Stack Infra/*.md` notes into their owning stack — flat.
3. Moves root-level roadmap canvases into their owning stack.
4. Rewrites wiki-links in every .md to basename form (`[[Promises]]`) so they
   resolve regardless of folder location.
5. Rewrites canvas JSON `"file"` paths to the new locations.
6. Removes useless placeholders.
7. Cleans up empty old folders.

WHAT IT DOES NOT DO
-------------------
- No new MOCs or canvases generated.
- No content rewriting.
- No subfolder structure (Topics/, Notes/, etc) — flat per the user's spec
  ("PRESERVED completely … then enhanced gradually").
- Existing populated stacks are preserved untouched apart from the move.

USAGE
-----
    python refactor-vault.py            # dry run
    python refactor-vault.py --apply    # actually do it
    # Then restart Obsidian once.
"""

from __future__ import annotations
import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent
INFRA = VAULT / "9 Full Stack Infra"

# -- Target stacks ---------------------------------------------------------------------------------

STACKS = [
    # Existing populated → moved
    "JavaScript", "React", "NodeJS", "Express", "MongoDB",
    "System Design", "Projects", "Interview Questions",
    # New empty stacks (empty unless an existing Infra note clearly fits)
    "TypeScript", "NextJS", "PostgreSQL", "Redis",
    "DevOps", "Cloud", "Testing", "AI Engineering",
    # Computer-science fundamentals
    "DSA",
    # Versioning + collaboration
    "Git and GitHub",
    # Orchestration
    "MERN Stack",
]

# -- Mapping rules ---------------------------------------------------------------------------------

# Numbered top-level folder → stack name (flat move, preserves filenames)
NUMBERED_TO_STACK: dict[str, str] = {
    "1 JavaScript":         "JavaScript",
    "2 React":              "React",
    "3 NodeJS":             "NodeJS",
    "4 Express":            "Express",
    "5 MongoDB":            "MongoDB",
    "6 System Design":      "System Design",
    "7 Projects":           "Projects",
    "8 Interview Questions":"Interview Questions",
}

# Existing notes that currently live LOOSE in `9 Full Stack Infra/*.md`.
# Map each filename to its target stack folder. None = keep at infra root (the MOC).
INFRA_LOOSE_TO_STACK: dict[str, str | None] = {
    "Full Stack Infra MOC.md":       None,
    # TypeScript / NextJS / React ecosystem
    "TypeScript.md":                 "TypeScript",
    "Next.js App Router.md":         "NextJS",
    "Pages Router.md":               "NextJS",
    "React Server Components.md":    "NextJS",
    "Convex.md":                     "NextJS",
    "Zustand.md":                    "React",
    "Immer.md":                      "React",
    "TanStack Query.md":             "React",
    "Framer Motion.md":              "React",
    "shadcn UI.md":                  "React",
    "Radix UI.md":                   "React",
    # Databases
    "PostgreSQL.md":                 "PostgreSQL",
    "pgvector.md":                   "PostgreSQL",      # extension of Postgres
    "Redis.md":                      "Redis",
    "Vector Databases.md":           "AI Engineering",
    "Turbopuffer.md":                "AI Engineering",
    # Cloud
    "AWS.md":                        "Cloud",
    "GCP.md":                        "Cloud",
    "Azure.md":                      "Cloud",
    "AWS S3.md":                     "Cloud",
    "Object Storage.md":             "Cloud",
    "Edge Computing.md":             "Cloud",
    # DevOps
    "Docker.md":                     "DevOps",
    "CI CD.md":                      "DevOps",
    "Terraform.md":                  "DevOps",
    "Pulumi.md":                     "DevOps",
    "WASM.md":                       "DevOps",
    "FFmpeg.md":                     "DevOps",
    "Sandboxing.md":                 "DevOps",
    "Firecracker.md":                "DevOps",
    "Remote Code Execution.md":      "DevOps",
    "DoS Protection.md":             "DevOps",
    "CLI.md":                        "DevOps",
    "Linux Basics.md":               "DevOps",
    "Shell Commands.md":             "DevOps",
    "Rust.md":                       "DevOps",
    "Go.md":                         "DevOps",
    # Testing
    "Unit Testing.md":               "Testing",
    "Integration Testing.md":        "Testing",
    "E2E Testing.md":                "Testing",
    "Vitest.md":                     "Testing",
    "Playwright.md":                 "Testing",
    "Puppeteer.md":                  "Testing",
    "TestSprite.md":                 "Testing",
    # AI Engineering
    "AI SDK by Vercel.md":           "AI Engineering",
    "AI Agents.md":                  "AI Engineering",
    "RAG.md":                        "AI Engineering",
    "Embeddings.md":                 "AI Engineering",
    "Vector Search.md":              "AI Engineering",
    "AI Providers.md":               "AI Engineering",
    # Internet / browser
    "DNS.md":                        "System Design",
    "WebRTC.md":                     "System Design",
    "Browser Internals.md":          "System Design",
    "Browser DevTools.md":           "System Design",
}

# Root-level canvases → destination
ROOT_CANVAS_MOVES: dict[str, Path] = {
    "React Roadmap.canvas":   INFRA / "React"      / "React Roadmap.canvas",
    "NodeJS Roadmap.canvas":  INFRA / "NodeJS"     / "NodeJS Roadmap.canvas",
    "Express Roadmap.canvas": INFRA / "Express"    / "Express Roadmap.canvas",
    "MongoDB Roadmap.canvas": INFRA / "MongoDB"    / "MongoDB Roadmap.canvas",
    "MERN Roadmap.canvas":    INFRA / "MERN Stack" / "MERN Roadmap.canvas",
    "Projects Path.canvas":   INFRA / "Projects"   / "Projects Path.canvas",
    # Full Stack Infra Roadmap.canvas stays at vault root
}

# Files to hard-delete
DELETIONS = [
    "1 JavaScript/Untitled.canvas",
    "1 JavaScript/Untitled.base",
    "2 React/sample react.md",
]

# Old top-level folders that should end up empty
OLD_TOP_FOLDERS = [
    "1 JavaScript", "2 React", "3 NodeJS", "4 Express",
    "5 MongoDB", "6 System Design", "7 Projects", "8 Interview Questions",
]


# -- Move planning ---------------------------------------------------------------------------------

def plan_destination(src: Path) -> Path | None:
    """Return new absolute destination, or None if the file should stay where it is."""
    rel = src.relative_to(VAULT)
    parts = rel.parts
    name = parts[-1]

    # Numbered top-level folders (flat move, preserve everything)
    if parts[0] in NUMBERED_TO_STACK:
        if str(rel).replace("\\", "/") in DELETIONS:
            return None
        stack = NUMBERED_TO_STACK[parts[0]]
        # Preserve sub-paths within the numbered folder if any (rare)
        sub_path = Path(*parts[1:]) if len(parts) > 1 else Path(name)
        return INFRA / stack / sub_path

    # Loose notes inside `9 Full Stack Infra/`
    if parts[0] == "9 Full Stack Infra":
        if len(parts) > 2:
            return None  # already in a subfolder, idempotent
        if name in INFRA_LOOSE_TO_STACK:
            stack = INFRA_LOOSE_TO_STACK[name]
            if stack is None:
                return None  # MOC stays
            return INFRA / stack / name
        return None  # unknown — leave alone

    # Root-level canvases
    if len(parts) == 1 and name in ROOT_CANVAS_MOVES:
        return ROOT_CANVAS_MOVES[name]

    return None


# -- Link rewriting --------------------------------------------------------------------------------

WIKI_RE = re.compile(r"\[\[([^\[\]\|]+?)(?:#([^\[\]\|]+))?(?:\|([^\[\]]+))?\]\]")

def rewrite_wikilink_target(target: str) -> str:
    target = target.strip()
    if "/" not in target and "\\" not in target:
        return target
    return os.path.basename(target.replace("\\", "/"))


def rewrite_wikilinks_in_text(text: str) -> str:
    def repl(m: re.Match) -> str:
        target = rewrite_wikilink_target(m.group(1))
        anchor = f"#{m.group(2)}" if m.group(2) else ""
        alias  = f"|{m.group(3)}" if m.group(3) else ""
        return f"[[{target}{anchor}{alias}]]"
    return WIKI_RE.sub(repl, text)


def rewrite_canvas_file_paths(canvas_text: str, basename_index: dict[str, Path]) -> str:
    try:
        data = json.loads(canvas_text)
    except json.JSONDecodeError:
        return canvas_text
    for node in data.get("nodes", []):
        if node.get("type") != "file":
            continue
        old = node.get("file", "")
        if not old:
            continue
        base = os.path.basename(old)
        new_abs = basename_index.get(base)
        if new_abs is None:
            continue
        new_rel = new_abs.relative_to(VAULT).as_posix()
        if new_rel != old:
            node["file"] = new_rel
    return json.dumps(data, indent=2, ensure_ascii=False)


# -- Operations ------------------------------------------------------------------------------------

def gather_moves() -> tuple[list[tuple[Path, Path]], list[Path]]:
    moves: list[tuple[Path, Path]] = []
    deletes: list[Path] = []
    for p in VAULT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(VAULT)
        if any(seg.startswith(".") for seg in rel.parts):
            continue
        if rel.as_posix() in DELETIONS:
            deletes.append(p)
            continue
        dest = plan_destination(p)
        if dest is None or dest == p:
            continue
        moves.append((p, dest))
    return moves, deletes


def ensure_folder_structure(apply: bool) -> None:
    INFRA.mkdir(exist_ok=True)
    for stack in STACKS:
        target = INFRA / stack
        if not target.exists():
            action = "creating" if apply else "would create"
            print(f"  {action} stack folder: {target.relative_to(VAULT)}")
            if apply:
                target.mkdir(parents=True, exist_ok=True)


def perform_moves(moves: list[tuple[Path, Path]], apply: bool) -> None:
    for src, dst in moves:
        action = "moving" if apply else "would move"
        print(f"  {action}: {src.relative_to(VAULT)}  ->  {dst.relative_to(VAULT)}")
        if apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.exists() and dst.resolve() != src.resolve():
                conflict = dst.with_suffix(dst.suffix + ".conflict")
                shutil.move(str(src), str(conflict))
                print(f"    !! destination existed; saved as {conflict.name}")
            else:
                shutil.move(str(src), str(dst))


def perform_deletes(deletes: list[Path], apply: bool) -> None:
    for d in deletes:
        if not d.exists():
            continue
        action = "deleting" if apply else "would delete"
        print(f"  {action}: {d.relative_to(VAULT)}")
        if apply:
            d.unlink()


def remove_empty_old_folders(apply: bool) -> None:
    for top in OLD_TOP_FOLDERS:
        p = VAULT / top
        if not p.exists():
            continue
        try:
            for sub in sorted(p.rglob("*"), key=lambda x: -len(x.parts)):
                if sub.is_dir() and not any(sub.iterdir()):
                    if apply: sub.rmdir()
            if p.is_dir() and not any(p.iterdir()):
                action = "removing empty folder" if apply else "would remove empty folder"
                print(f"  {action}: {p.relative_to(VAULT)}")
                if apply: p.rmdir()
        except OSError as e:
            print(f"  cannot remove {p.relative_to(VAULT)}: {e}")


def rewrite_links_in_all_files(apply: bool) -> int:
    md_files     = list(VAULT.rglob("*.md"))
    canvas_files = list(VAULT.rglob("*.canvas"))

    basename_index: dict[str, Path] = {}
    for f in md_files + canvas_files:
        if any(seg.startswith(".") for seg in f.relative_to(VAULT).parts):
            continue
        basename_index.setdefault(f.name, f)

    changed = 0
    for f in md_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        new  = rewrite_wikilinks_in_text(text)
        if new != text:
            changed += 1
            action = "rewrote" if apply else "would rewrite"
            print(f"  {action} wiki-links: {f.relative_to(VAULT)}")
            if apply:
                f.write_text(new, encoding="utf-8")

    for f in canvas_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        new  = rewrite_canvas_file_paths(text, basename_index)
        if new != text:
            changed += 1
            action = "rewrote" if apply else "would rewrite"
            print(f"  {action} canvas paths: {f.relative_to(VAULT)}")
            if apply:
                f.write_text(new, encoding="utf-8")
    return changed


def report_distribution() -> None:
    """Print which existing notes will land in which stack."""
    print("\n=== Resulting note distribution (from current state, before --apply) ===")
    counts: dict[str, int] = {s: 0 for s in STACKS}
    for p in VAULT.rglob("*.md"):
        if any(seg.startswith(".") for seg in p.relative_to(VAULT).parts):
            continue
        dest = plan_destination(p) or p
        rel = dest.relative_to(VAULT).as_posix()
        for stack in STACKS:
            if rel.startswith(f"9 Full Stack Infra/{stack}/"):
                counts[stack] += 1
                break
    width = max(len(s) for s in STACKS)
    for stack in STACKS:
        marker = "  " if counts[stack] > 0 else "(empty stack — start gradually filling)"
        print(f"  {stack.ljust(width)}  {counts[stack]:>3} notes  {marker}")


# -- Main ------------------------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="actually move files")
    args = ap.parse_args()

    print("=== 1. Folder structure ===")
    ensure_folder_structure(apply=args.apply)

    print("\n=== 2. Plan moves ===")
    moves, deletes = gather_moves()
    print(f"  {len(moves)} files to move, {len(deletes)} to delete")
    perform_moves(moves, apply=args.apply)

    print("\n=== 3. Delete placeholders ===")
    perform_deletes(deletes, apply=args.apply)

    print("\n=== 4. Rewrite links ===")
    n = rewrite_links_in_all_files(apply=args.apply)
    print(f"  {n} files {'rewritten' if args.apply else 'would be rewritten'}")

    print("\n=== 5. Cleanup empty old folders ===")
    remove_empty_old_folders(apply=args.apply)

    if not args.apply:
        report_distribution()
        print("\nDry run complete. Run with --apply to execute.")
    else:
        print("\nRefactor applied. Restart Obsidian so it re-indexes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
