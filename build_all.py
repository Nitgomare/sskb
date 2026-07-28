#!/usr/bin/env python
"""Build the main MkDocs site and every independent book into one site/ tree."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "site"
BOOKS_DIR = ROOT / "books"


def run_mkdocs(*arguments: str) -> None:
    command = [sys.executable, "-m", "mkdocs", "build", *arguments]
    print(f"\n> {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    print("Building main knowledge base...", flush=True)
    run_mkdocs(
        "--config-file",
        str(ROOT / "mkdocs.yml"),
        "--site-dir",
        str(SITE_DIR),
        "--clean",
    )

    configs = sorted(BOOKS_DIR.glob("*/mkdocs.yml"), key=lambda path: path.as_posix())
    if not configs:
        print("\nNo independent book projects found.", flush=True)
        return

    for config in configs:
        slug = config.parent.name
        output = SITE_DIR / "book-sites" / slug
        print(f"\nBuilding book: {slug}", flush=True)
        run_mkdocs(
            "--config-file",
            str(config),
            "--site-dir",
            str(output),
            "--clean",
        )

    print(f"\nComplete: {SITE_DIR}", flush=True)


if __name__ == "__main__":
    main()
