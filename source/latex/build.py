#!/usr/bin/env python3
"""Build both editable LaTeX campaign layouts and their social PNG exports."""

from pathlib import Path
import shutil
import subprocess
import sys


def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    if result.returncode:
        sys.stderr.write(result.stdout + result.stderr)
        raise SystemExit(result.returncode)


def main():
    source = Path(__file__).resolve().parent
    root = source.parents[1]
    temporary = root / "tmp" / "latex"
    output = root / "output"
    for directory in (temporary, output):
        directory.mkdir(parents=True, exist_ok=True)

    for executable in ("pdflatex", "pdftoppm"):
        if not shutil.which(executable):
            raise SystemExit(f"Missing {executable}; see source/latex/README.md.")

    for name, width, height in (("instagram", 1080, 1350), ("linkedin", 1200, 627)):
        for _ in range(2):
            run([
                "pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                f"-output-directory={temporary}", f"{name}.tex",
            ], source)
        basename = output / f"egu27-hs38-{name}"
        shutil.copyfile(temporary / f"{name}.pdf", basename.with_suffix(".pdf"))
        run([
            "pdftoppm", "-png", "-singlefile", "-scale-to-x", str(width),
            "-scale-to-y", str(height), str(basename.with_suffix(".pdf")),
            str(basename),
        ], root)
        print(f"Built {basename.relative_to(root)}.pdf and .png ({width} x {height})")


if __name__ == "__main__":
    main()
