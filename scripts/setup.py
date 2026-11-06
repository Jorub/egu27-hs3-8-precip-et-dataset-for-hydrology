#!/usr/bin/env python3
"""Prepare local folders and preserve optional machine-specific configuration."""
import json
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def environment():
    configuration = ROOT / "config.local.json"
    values = json.loads(configuration.read_text()) if configuration.exists() else {}
    additions = values.get("extra_path", [])
    if not isinstance(additions, list) or not all(isinstance(item, str) for item in additions):
        raise SystemExit("config.local.json: extra_path must be a list of directory paths.")
    return {**os.environ, "PATH": os.pathsep.join(additions + [os.environ.get("PATH", "")])}


def main():
    for name in ("output", "site/downloads", "tmp/latex"):
        (ROOT / name).mkdir(parents=True, exist_ok=True)
    configuration = ROOT / "config.local.json"
    if not configuration.exists():
        shutil.copyfile(ROOT / "config.example.json", configuration)
        print("Created ignored config.local.json; add tool directories only if needed.")
    else:
        print("Preserved existing config.local.json.")
    env = environment()
    missing = [name for name in ("pdflatex", "pdftoppm") if not shutil.which(name, path=env["PATH"])]
    if missing:
        raise SystemExit("Missing system prerequisites: " + ", ".join(missing) + ". See README.md.")
    print("Ready: Python standard library, pdfLaTeX and Poppler. No Python packages need installing.")


if __name__ == "__main__":
    main()
