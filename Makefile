# CV pipeline — build the website + single-page PDF from cv.md
# Usage:
#   make          build everything (EN + FR)
#   make web      regenerate English CV page
#   make pdf      render English PDF (one-page enforced) + copy into site
#   make web-fr   regenerate French CV page
#   make pdf-fr   render French PDF (one-page enforced) + copy into site
#   make serve    preview site/ at http://localhost:8000 (optional)
#   make clean    remove generated artifacts

.PHONY: all web pdf web-fr pdf-fr serve clean

all: web pdf web-fr pdf-fr

# ---- English ----

web: site/cv/index.html site/web.css

pdf: pdf/CV.pdf site/cv/CV.pdf

site/web.css: styles/web.css
	cp styles/web.css $@

site/cv/index.html: cv.md templates/cv.html styles/web.css
	@mkdir -p $(dir $@)
	pandoc cv.md --template templates/cv.html --css styles/web.css --embed-resources -V en-active=true -V 'download-text=⬇ Download PDF' -o $@

build/cv-print.html: cv.md templates/cv.html styles/print.css
	@mkdir -p $(dir $@)
	pandoc cv.md --template templates/cv.html --css styles/print.css --embed-resources -V en-active=true -o $@

pdf/CV.pdf: build/cv-print.html
	@mkdir -p pdf
	uv run python build_pdf.py build/cv-print.html pdf/CV.pdf

site/cv/CV.pdf: pdf/CV.pdf
	cp pdf/CV.pdf $@

# ---- French ----

web-fr: site/fr/cv/index.html site/web.css

pdf-fr: pdf/CV-fr.pdf site/fr/cv/CV.pdf

site/fr/cv/index.html: cv-fr.md templates/cv.html styles/web.css
	@mkdir -p $(dir $@)
	pandoc cv-fr.md --template templates/cv.html --css styles/web.css --embed-resources -V fr-active=true -V 'download-text=⬇ Télécharger le PDF' -o $@

build/fr-cv-print.html: cv-fr.md templates/cv.html styles/print.css
	@mkdir -p $(dir $@)
	pandoc cv-fr.md --template templates/cv.html --css styles/print.css --embed-resources -V fr-active=true -o $@

pdf/CV-fr.pdf: build/fr-cv-print.html
	uv run python build_pdf.py build/fr-cv-print.html pdf/CV-fr.pdf

site/fr/cv/CV.pdf: pdf/CV-fr.pdf
	cp pdf/CV-fr.pdf $@

# ---- Utilities ----

serve: all
	python3 -m http.server 8000 --directory site

clean:
	rm -rf build site/cv/index.html site/cv/CV.pdf site/fr/cv/index.html site/fr/cv/CV.pdf pdf/CV.pdf pdf/CV-fr.pdf
