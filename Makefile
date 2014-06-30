
FILES = $(wildcard tut/*/*.rst)

default: tut/index.html $(foreach x, $(FILES), $(basename $x).html)

tut/index.html: tut/index.rst
	python rst2html.py tut/index.rst tut/index.html --traceback

%.html: %.rst
	python rst2html.py $*.rst $*.html
	python rst2html.py $*.rst $*-big.html    --stylesheet-path=style-docutils.css,style.css
	python rst2s5.py   $*.rst $*-s5.html

pub:
	rsync -avP --inplace --delete tut/ kafka:/srv/rkd/www/scicomp/