# CV pipeline — one source of facts, many variants.
#
#   make          build every variant in variants/*.yaml (web page + one-page PDF)
#   make list     list configured variants
#   make serve    build, then preview site/ at http://localhost:8000
#   make followups  applications whose follow-up is due (DAYS=7 to look ahead)
#   make clean    remove generated artifacts
#
# Identity lives in cv.yaml, per-variant settings in variants/*.yaml, content in
# cv.md / cv-fr.md selected by inline <!-- v:name --> markers. The one-page rule
# is enforced by build_pdf.py for every variant.

.PHONY: all list serve followups clean

DAYS ?=

all:
	uv run python tools/build_cv.py
	uv run python tools/check_links.py

followups:
	uv run python tools/followups.py $(DAYS)

list:
	@ls variants/*.yaml | sed 's|variants/||; s|\.yaml$$||'

serve: all
	python3 -m http.server 8000 --directory site

clean:
	rm -rf build pdf
	rm -rf site/cv site/fr/cv site/routes
	rm -f site/web.css
