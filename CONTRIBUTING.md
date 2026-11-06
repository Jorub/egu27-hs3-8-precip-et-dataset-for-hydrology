# Contributing

Keep editable LaTeX in `source/latex/`, final PDF/PNG exports in `output/`, the static website in `site/`, channel copy in `outreach/`, and execution helpers in `scripts/`. TeX auxiliary files and private machine settings stay ignored.

Prefer small, readable changes. Keep the artwork's text live and vector geometry editable. Use TeX Gyre Heros only, at no more than three size levels per layout. Preserve blue/yellow emphasis, an immediately visible subject headline, and concise contribution topics instead of the earlier verb-only theme line. Use the official programme and support pages for factual updates; conference dates do not establish a session presentation time.

Run `python3 scripts/build.py` when LaTeX changes, or `python3 scripts/build.py --skip-artwork` when only copy/download packaging changes. Run `python3 scripts/validate.py` before publishing. Visually inspect both final PNGs and the responsive website after layout changes, and verify embedded PDF hyperlinks after link changes. Keep generated website downloads in the same commit as their sources.

Use the optional ignored `config.local.json` for local executable paths; `config.example.json` is the tracked template. Preserve existing local configuration. Use the normal GitHub sign-in/credential tools for publication; never commit credentials, browser exports or the colleague's reference attachment.

For subsequent work, `codex/` branches are the suggested convention; no branch protection or mandatory review gate has been established. Do not rewrite shared history. Make commits detailed enough to explain the change and its purpose, including useful validation or material limitations. Update `docs/history.md` for meaningful milestones or design decisions, without duplicating the full diff or conversation.

Credit the actual contributing AI model in AI-assisted commits. For this work, a suitable commit-body statement is `AI assistance: GPT-6 (Codex).` Use the actual model for later work; do not invent identities or attribute human-provided material to AI. Keep the README's attribution accurate.

Discuss consequential changes to the visual concept, published audience, scientific scope or permanent address with the project owner. Handle routine corrections and rebuilds within the authorized task.
