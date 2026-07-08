#!/usr/bin/env python3
"""Run repository checks before publishing the skill."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
TEMP_PARTS = {
    "tmp",
    "temp",
    "test-output",
    ".agents",
    ".codex",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}
TEXT_SUFFIXES = {
    ".env",
    ".env.local",
    ".md",
    ".py",
    ".yaml",
    ".yml",
    ".toml",
    ".json",
    ".txt",
    ".gitignore",
}

SOURCE_TERMS = "|".join(
    [
        "video" + "-derived",
        "transcript" + "-derived",
        "source " + "transcript",
        "video " + "key points",
        "\u89c6\u9891\u6587\u5b57",
        "\u89c6\u9891\u6765\u6e90",
        "\u8f6c\u5199",
    ]
)

PATTERNS = [
    ("windows absolute path", re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:\\[^\s`\"')]+")),
    ("private thread id", re.compile(r"\b019[a-f0-9]{29}\b", re.IGNORECASE)),
    ("uuid-like id", re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.IGNORECASE)),
    ("openai api key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("github token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("generic secret assignment", re.compile(r"(?i)\b(api[_-]?key|token|secret|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]")),
    ("source-description term", re.compile(SOURCE_TERMS, re.IGNORECASE)),
]


def git_files(args: list[str]) -> list[Path]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line]


def publishable_files() -> list[Path]:
    files = git_files(["ls-files"])
    files += git_files(["ls-files", "--others", "--exclude-standard"])
    return sorted(path for path in set(files) if path.exists())


def is_text_file(path: Path) -> bool:
    if any(part in IGNORED_PARTS for part in path.parts):
        return False
    if path.name in TEXT_SUFFIXES:
        return True
    return path.suffix.lower() in TEXT_SUFFIXES


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_temp_paths(files: list[Path]) -> list[str]:
    errors = []
    for path in files:
        rel_parts = path.relative_to(ROOT).parts
        if any(part in TEMP_PARTS for part in rel_parts):
            errors.append(f"temporary path tracked or publishable: {relative(path)}")
    return errors


def check_content(files: list[Path]) -> list[str]:
    errors = []
    for path in files:
        if not is_text_file(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"not utf-8: {relative(path)} ({exc})")
            continue

        for line_no, line in enumerate(text.splitlines(), 1):
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    errors.append(f"{label}: {relative(path)}:{line_no}")
    return errors


def main() -> int:
    files = publishable_files()
    errors = check_temp_paths(files) + check_content(files)
    if errors:
        print("Pre-publish check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Pre-publish check passed ({len(files)} files scanned).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
