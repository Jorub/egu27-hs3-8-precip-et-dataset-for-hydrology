#!/usr/bin/env python3
"""Build artwork and prepare all static website downloads."""
import argparse
import hashlib
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

from setup import environment

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-artwork", action="store_true", help="Package existing PDF/PNG exports without recompiling them.")
    options = parser.parse_args()
    if not options.skip_artwork:
        subprocess.run([sys.executable, "source/latex/build.py"], cwd=ROOT, env=environment(), check=True)
    downloads = ROOT / "site/downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    for name in ("instagram", "linkedin"):
        for extension in ("pdf", "png"):
            filename = f"egu27-hs38-{name}.{extension}"
            shutil.copyfile(ROOT / "output" / filename, downloads / filename)
    page = ROOT / "site/index.html"
    html = page.read_text()
    for name in ("instagram", "linkedin"):
        filename = f"egu27-hs38-{name}.png"
        version = hashlib.sha256((downloads / filename).read_bytes()).hexdigest()[:12]
        pattern = r'(src="downloads/' + re.escape(filename) + r')(?:\?[^"\s]*)?"'
        html = re.sub(pattern, lambda match: match[1] + '?v=' + version + '"', html)
    page.write_text(html)
    shutil.copyfile(ROOT / "output/alt-text.txt", downloads / "alt-text.txt")
    shutil.copyfile(ROOT / "outreach/promotion-pack.md", downloads / "promotion-pack.md")
    archive = downloads / "egu27-hs38-latex.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for source in sorted((ROOT / "source/latex").iterdir()):
            if source.suffix in (".tex", ".sty"):
                package.write(source, arcname=source.name)
        package.writestr("README.md", "# Editable EGU27 artwork\n\nCompile main.tex with pdfLaTeX for the Instagram layout, or compile linkedin.tex for the landscape layout. Keep all files together. No external images are required.\n\nEdit content.tex for wording, deadlines and embedded links. Edit campaign.sty for colours, typography and the original TikZ illustration.\n\nThe full repository includes a Python build helper for exact-size PNG exports.\n")
    print("Prepared site/downloads: social PNGs, linked PDFs, editable LaTeX ZIP, alt text and share copy.")


if __name__ == "__main__":
    main()
