#!/usr/bin/env python3
"""Check local site destinations, downloadable sources and export dimensions."""
from html.parser import HTMLParser
from pathlib import Path
import struct
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if "id" in attributes:
            if attributes["id"] in self.ids:
                raise ValueError("Duplicate HTML id: " + attributes["id"])
            self.ids.add(attributes["id"])
        self.urls.extend(attributes[key] for key in ("href", "src") if key in attributes)


def main():
    page = Links()
    page.feed((SITE / "index.html").read_text())
    for value in page.urls:
        target = urlsplit(value)
        if target.scheme or target.netloc:
            continue
        if target.path:
            path = (SITE / unquote(target.path)).resolve()
            if not path.is_relative_to(SITE.resolve()) or not path.is_file():
                raise SystemExit("Missing or invalid local link: " + value)
        elif target.fragment and target.fragment not in page.ids:
            raise SystemExit("Missing HTML anchor: " + value)
    for name, expected in (("instagram", (1080, 1350)), ("linkedin", (1200, 627))):
        image = SITE / f"downloads/egu27-hs38-{name}.png"
        data = image.read_bytes()
        if data[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", data[16:24]) != expected:
            raise SystemExit("Unexpected PNG format or dimensions: " + image.name)
        pdf = SITE / f"downloads/egu27-hs38-{name}.pdf"
        if not pdf.read_bytes().startswith(b"%PDF-"):
            raise SystemExit("Invalid PDF header: " + pdf.name)
    with zipfile.ZipFile(SITE / "downloads/egu27-hs38-latex.zip") as package:
        required = {"main.tex", "instagram.tex", "linkedin.tex", "campaign.sty", "content.tex", "README.md"}
        if not required.issubset(set(package.namelist())) or package.testzip():
            raise SystemExit("Incomplete or corrupt editable LaTeX archive.")
    print("Passed: local site links/anchors, exact PNG dimensions, PDF headers and editable LaTeX archive.")


if __name__ == "__main__":
    main()
