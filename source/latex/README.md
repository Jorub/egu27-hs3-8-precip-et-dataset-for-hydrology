# Editable campaign artwork

Both layouts are native LaTeX and TikZ. Text, colours, rain, clouds, ET arrows,
mountains, trees and river are editable; no background image is required.

- `content.tex`: headline, four contribution topics, programme badge, embedded links, abstract and travel-support deadlines, and conference dates.
- `campaign.sty`: shared colour palette, typography, illustration and layout coordinates.
- `instagram.tex`: portrait page, aspect ratio 4:5, exported to 1080 × 1350 px.
- `linkedin.tex`: landscape page, aspect ratio 1200:627, exported to 1200 × 627 px.
- `main.tex`: default entry point for Overleaf, using the Instagram portrait layout.

The session code is deliberately a content field. If the session is renumbered after
merging, update `\SessionCode` and `\SessionURL` in `content.tex` and rebuild.
Update the web content separately through the repository's documented web workflow.

The single font family is **TeX Gyre Heros**, in regular and bold weights. Each
layout uses exactly three size tokens: **26 / 22 / 14 TeX pt** for Instagram and
**20 / 18 / 10 TeX pt** for LinkedIn. The headline, context/deadlines and body
helpers in `campaign.sty` control every text element, including the P and ET labels.
Change the `\UseCampaignSizes` arguments to adjust these levels; do not add separate
caption sizes. Contribution macros use deliberate line breaks to avoid hyphenated
words in the small boxes. `\ContributionOneCompact` holds the narrower LinkedIn
version of the same evaluation topic.

## Build

Requires Python 3, pdfLaTeX (TeX Live or MacTeX), TikZ, TeX Gyre Heros and Poppler's
`pdftoppm`. These packages are included in a normal full TeX Live installation.

From the repository root:

```sh
python3 source/latex/build.py
```

The helper compiles each layout twice for stable positioning, writes final PDFs and
PNGs to `output/`, and keeps TeX auxiliary files under `tmp/latex/`.

You can also open `main.tex`, `instagram.tex` or `linkedin.tex` in a LaTeX editor and compile
with pdfLaTeX. Keep `campaign.sty` and `content.tex` in the same directory.

PDF labels and dates contain embedded links to the session and travel-support
information. PNG exports remain static images; use the accompanying platform links
when posting them. The 1 December deadline is for Roland Schlich travel support.

The artwork is an original illustration for the session campaign. It does not reuse
the colleague's reference image or represent an official EGU visual template.
