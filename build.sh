#!/bin/bash
set -e
echo "=== Building web ==="
mkdir -p site/cv
pandoc cv.md --template templates/cv.html --css styles/web.css --embed-resources -V en-active=true -o site/cv/index.html 2>&1
echo "web done, rc=$?"

echo "=== Copying web.css ==="
cp styles/web.css site/web.css 2>&1
echo "css done"

echo "=== Building web-fr ==="
mkdir -p site/fr/cv
pandoc cv-fr.md --template templates/cv.html --css styles/web.css --embed-resources -V fr-active=true -o site/fr/cv/index.html 2>&1
echo "web-fr done, rc=$?"

echo "=== Building print HTML (EN) ==="
mkdir -p build
pandoc cv.md --template templates/cv.html --css styles/print.css --embed-resources -V en-active=true -o build/cv-print.html 2>&1
echo "print-html done"

echo "=== Building PDF (EN) ==="
mkdir -p pdf
uv run python build_pdf.py build/cv-print.html pdf/CV.pdf 2>&1
echo "pdf done, rc=$?"

echo "=== Copying EN PDF to site ==="
cp pdf/CV.pdf site/cv/CV.pdf 2>&1

echo "=== Building print HTML (FR) ==="
pandoc cv-fr.md --template templates/cv.html --css styles/print.css --embed-resources -V fr-active=true -o build/fr-cv-print.html 2>&1
echo "fr-print-html done"

echo "=== Building PDF (FR) ==="
mkdir -p pdf-fr
uv run python build_pdf.py build/fr-cv-print.html pdf-fr/CV.pdf 2>&1
echo "pdf-fr done, rc=$?"

echo "=== Copying FR PDF to site ==="
cp pdf-fr/CV.pdf site/fr/cv/CV.pdf 2>&1

echo "=== ALL DONE ==="
