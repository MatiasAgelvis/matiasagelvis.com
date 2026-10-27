# Career workspace

Two things live here: the static site (CV variants, homepages, letter builder) and the
working files behind the job search.

## The map

One question, one file. When two of them disagree, the one higher in this table wins.

| Question | File | Committed |
|---|---|---|
| What are my dates, roles, employers? | `timeline.md` | yes |
| What is my contact block? | `cv.yaml` | yes |
| What did I actually do, and how do I say it? | `impact.md` | no |
| What do I paste into Malt / Free-Work / LinkedIn? | `profiles.md` | no |
| What goes in the CV? | `cv-fr.md`, `cv.md` | yes |
| What do I do if nothing lands? | `plan.md` | no |
| What have I sent, and when do I follow up? | `applications.csv` | no |

The four marked **no** are gitignored: this repo is public, and rates, recruiter contacts
and contingency plans don't belong in it.

## The CV is not the reference

The CV is a *rendering* of the facts, compressed to one page, and it drops things on
purpose. The research assistantship sits under Formation, the two freelance periods are
merged into one entry, and the fintech variant swaps a bullet. `timeline.md` is the
reference; the CV is one output of it.

## Update order

1. `timeline.md` — if a date or a role changes
2. `impact.md` — if the story or the evidence changes
3. `cv-fr.md` / `cv.md` — the CV content
4. `profiles.md` — the platforms
5. `make` — rebuild the pages and the PDFs

## Commands

```sh
make               # build every variant (page + one-page PDF), then check links
make list          # list configured variants
make followups     # applications due for follow-up (DAYS=7 to look ahead)
make serve         # build, then preview site/ at http://localhost:8000
make clean         # remove generated artifacts
```

## How the site is built

`cv.yaml` (identity) + `variants/*.yaml` (one per page) + `cv-fr.md` / `cv.md` (content)
→ `tools/build_cv.py` → `site/`.

Content is selected with inline markers:

```markdown
<!-- v:or -->  ...  <!-- /v -->          a block only the `or` variant renders
- a bullet <!-- v:backend,fintech -->   a line only those variants render
```

Untagged content always renders. The one-page rule is enforced by `build_pdf.py`, so a
variant that overflows fails the build with the overflowing text instead of shipping
quietly. A live inventory of every generated route is at `/routes/` on the deployed site.

## Never edit

`site/` is generated — edit the sources and run `make`. `build/` and `pdf/` are artifacts.
`DESIGN.md` covers the visual design.
