# Precipitation & ET data for hydrological studies

Campaign materials and a static session website for **EGU27 session HS3.8**.

**Full session title:** Precipitation and Evapotranspiration Datasets for Hydrological Studies: Development, Evaluation, and Applications.

- [Official session and abstract submission](https://meetingorganizer.copernicus.org/EGU27/session/61787)
- **Travel support: 1 December 2026, 13:00 CET**, for eligible Roland Schlich applicants. Submit the abstract and support request by this earlier deadline. [Check eligibility and apply](https://www.egu27.eu/attendance/financial_support_and_waivers.html).
- **Abstracts: 12 January 2027, 13:00 CET**. [Official deadlines](https://www.egu27.eu/about/deadlines_and_milestones.html).
- Conference: 4–9 April 2027, Vienna and online. These are conference dates, not the session's scheduled presentation time.

The visual direction uses blue and yellow, a large subject headline, an original editable water-cycle illustration, four concise contribution topics and distinct deadline panels. TeX Gyre Heros is the only font family, with three size levels in each layout. The colleague's reference image is not redistributed.

## Project layout

| Path | Purpose |
| --- | --- |
| `source/latex/` | Editable text, shared TikZ artwork and Instagram/LinkedIn layouts |
| `output/` | Current linked PDFs, exact-size social PNGs and alt text |
| `site/` | Buildless HTML/CSS/JS website and prepared downloadable materials |
| `outreach/promotion-pack.md` | Social posts, newsletter copy, contacts and proposed campaign timing |
| `scripts/` | Setup, artwork/website packaging and local validation |
| `docs/history.md` | Meaningful project decisions and milestones |

## Setup and build

Requires **Python 3.9+**, **pdfLaTeX** with TikZ and TeX Gyre Heros (TeX Live or MacTeX), and Poppler's **pdftoppm**. No Python packages or JavaScript package installation are needed. A normal full TeX Live installation supplies the LaTeX packages; Poppler is separate. On macOS, Poppler can be installed with `brew install poppler` if missing.

From the repository root:

```sh
python3 scripts/setup.py
python3 scripts/build.py
python3 scripts/validate.py
```

Setup creates the working folders and an ignored `config.local.json` from `config.example.json`, preserving an existing local configuration. If tools are outside the shell's PATH, put their containing directories in the local `extra_path` list. Credentials are not required for local work and do not belong in the repository.

The build compiles both LaTeX layouts and exports **1080 × 1350** and **1200 × 627** PNGs. It then prepares the website downloads, including a standalone LaTeX ZIP, and updates content-versioned preview URLs so browsers load the current artwork. If the existing artwork is unchanged, use `python3 scripts/build.py --skip-artwork` to refresh only downloads. Temporary TeX files stay in ignored `tmp/latex/`.

## Edit the materials

1. Edit `source/latex/content.tex` for the subject headline, session badge, dates and embedded links. Edit `campaign.sty` for colours, type and vector geometry.
2. Compile `source/latex/main.tex` (Instagram) or `linkedin.tex` directly in TeXShop, Overleaf or another LaTeX editor, or run the complete build above.
3. Edit `site/index.html` and `site/styles.css` for the website. `site/session.js` centralizes the session code, URLs and travel-support details; keep the marked HTML fallback and page metadata in sync for visitors without JavaScript and social previews.
4. Edit `outreach/promotion-pack.md` for the channel copy. Rebuild the download package after any source/copy change.

If EGU changes the session identifier after a merger, update the artwork content fields, web settings/fallback and share copy. The repository name chosen for this campaign can remain a stable address.

Instagram includes labelled QR codes for session/abstract submission and travel-support information, generated as vectors by the LaTeX qrcode package. The PDFs contain clickable session and travel-support links. A PNG cannot contain a clickable hyperlink; use the corresponding caption link, Instagram profile link or Story sticker. Alt text is included in `output/alt-text.txt` and the website downloads.

The website includes locally served TeX Gyre Heros webfonts in `site/assets/fonts/`, with their GUST Font License and provenance. Those assets require no external font service.

## Local website preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Open `http://127.0.0.1:8000/` and stop the server with Ctrl-C when finished. Check the headline and both deadline blocks on desktop and mobile, and follow the session/support/download links. `scripts/validate.py` checks local links and export packaging; it does not establish that remote URLs are reachable or that visual layout is correct.

## GitHub Pages

The selected destination is **Jorub/egu27-hs3-8-precip-et-dataset-for-hydrology**. The supplied workflow publishes the prepared `site/` folder from `main` after its local-file checks pass.

For a new GitHub repository, select **Settings → Pages → Source → GitHub Actions**. Once the project is pushed, the workflow provides the deployment URL. Expected project address after successful deployment:

[Session campaign website](https://jorub.github.io/egu27-hs3-8-precip-et-dataset-for-hydrology/)

Do not call that address live until the GitHub Pages deployment has succeeded. Follow the [official GitHub Pages workflow guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) for changes to hosting configuration. Rebuild and commit the prepared downloads whenever the artwork changes; CI validates and deploys them without installing a TeX distribution.

## Search discovery

The canonical landing page is listed in [`site/sitemap.xml`](site/sitemap.xml), served at [the public sitemap](https://jorub.github.io/egu27-hs3-8-precip-et-dataset-for-hydrology/sitemap.xml). The HTML head also links to this file. Keep the canonical URL and sitemap in sync if the site moves.

`site/robots.txt` contains permissive directives and the absolute sitemap URL. Because this is a GitHub Pages **project** site, that copy is served inside the project subfolder. Search engines consult `https://jorub.github.io/robots.txt` at the host root instead; a root-level file would need to be published by the user-site repository. A missing root robots.txt does not itself block crawling. This project does not modify other repositories.

For Google Search Console, add a **URL-prefix property** for `https://jorub.github.io/egu27-hs3-8-precip-et-dataset-for-hydrology/`. Use Google's real HTML verification tag in the page head or its supplied verification file in `site/`; retain it after verification. Submit `sitemap.xml`, inspect the canonical landing-page URL and request indexing. Verification requires access to the owner's Google account or its issued verification token; publishing a sitemap alone does not verify ownership or guarantee indexing.

## Contribution and attribution

Read [CONTRIBUTING.md](CONTRIBUTING.md) for editing, validation and commit conventions. Scientific session wording and approval originate with the conveners. The website, revised campaign artwork, drafts and project tooling were prepared with **GPT-6 (Codex)** assistance; the supplied colleague reference remains human-provided material and is not claimed as AI-authored.
