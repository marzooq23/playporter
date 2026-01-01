#!/usr/bin/env python3
"""PlayPorter CLI entrypoint.

Usage:
  playporter --migrate <selenium-path> <playwright-path>

This file provides a minimal CLI that will be exposed as the `playporter`
console script when the package is installed.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import logging
from typing import Sequence

logger = logging.getLogger(__name__)


def migrate_framework(src: str, dest: str, language: str | None = None) -> int:
    """Attempt to run a migration tool if available, otherwise print a helpful message.

    This will try to import `playporter.tools.selenium_to_playwright_tool` and call
    a `migrate(src, dest, language=None)` function if present. It is backward
    compatible with older tools that accept only (src, dest).
    """
    try:
        # Try to delegate to a tool if the project implements it
        from .tools import selenium_to_playwright_tool  # type: ignore

        if hasattr(selenium_to_playwright_tool, "migrate"):
            try:
                # Prefer calling with language when supported
                result = selenium_to_playwright_tool.migrate(src, dest, language)
            except TypeError:
                # Fallback for older implementations that accept only (src, dest)
                result = selenium_to_playwright_tool.migrate(src, dest)
            return int(result or 0)
    except Exception as exc:  # pragma: no cover - fallback behavior
        logger.debug("Could not run migration tool", exc_info=exc)

    if language:
        print(f"Migrate requested from '{src}' to '{dest}' using language '{language}', but no migration tool is implemented.")
    else:
        print(f"Migrate requested from '{src}' to '{dest}', but no migration tool is implemented.")
    print("Implement `migrate(src, dest, language=None)` in `playporter.tools.selenium_to_playwright_tool` to enable this.")
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="playporter")
    parser.add_argument(
        "-m",
        "--migrate",
        nargs="+",
        metavar=("SRC", "DEST", "LANG"),
        help='Migrate a Selenium framework to Playwright. Usage: --migrate SRC DEST [LANG] (LANG is optional)',
    )
    parser.add_argument("--version", action="version", version="playporter 0.0.1")

    args = parser.parse_args(argv)

    if args.migrate:
        if len(args.migrate) not in (2, 3):
            print("Usage: --migrate SRC DEST [LANG]")
            return 2

        src_path, dest_path = args.migrate[0], args.migrate[1]
        language = args.migrate[2] if len(args.migrate) == 3 else None

        src = Path(src_path)
        dest = Path(dest_path)

        if not src.exists():
            print(f"Source path does not exist: {src}")
            return 2

        # Make sure destination parent exists
        if dest.parent and not dest.parent.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)

        return migrate_framework(str(src), str(dest), language)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
