# CV pipeline — build the website + single-page PDF from cv.md
# Usage:
#   make          build web page + PDF
#   make web      regenerate site/cv/index.html
#   make pdf      render pdf/CV.pdf (one-page enforced) and copy into the site
#   make serve    preview site/ at http://localhost:8000 (optional)
#   make clean    remove generated artifacts

.PHONY: all web pdf serve clean
all: web pdf

web: site/cv/index.html

pdf: pdf/CV.pdf site/cv/CV.pdf

site/cv/index.html: cv.md templates/cv.html styles/web.css
	@mkdir -p $(dir $@)
	pandoc cv.md --template templates/cv.html --css styles/web.css --embed-resources -o $@

build/cv-print.html: cv.md templates/cv.html styles/print.css
	@mkdir -p $(dir $@)
	pandoc cv.md --template templates/cv.html --css styles/print.css --embed-resources -o $@

pdf/CV.pdf: build/cv-print.html
	@mkdir -p pdf
	uv run python build_pdf.py

site/cv/CV.pdf: pdf/CV.pdf
	cp pdf/CV.pdf $@

serve: all
	python3 -m http.server 8000 --directory site

clean:
	rm -rf build pdf site/cv/index.html site/cv/CV.pdf
