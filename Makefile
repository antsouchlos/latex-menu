all: build/menu-leaflet.pdf

build/menu.pdf: menu.tex
	latexmk menu.tex

build/menu-leaflet.pdf: build/menu.pdf
	python scripts/create-leaflet.py --input build/menu.pdf --output build/menu-leaflet.pdf

clean:
	rm -rf build

