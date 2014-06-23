
FILES = $(wildcard tut/*/*.rst)

default: $(foreach x, $(FILES), $(basename $x).html)

%.html: %.rst
#	python rst2html.py $*.rst $*.html
	python rst2html.py $*.rst $*.html    --stylesheet-path=style-docutils.css,style.css
	python rst2s5.py   $*.rst $*-s5.html

pub:
	rsync -avP --inplace --delete tut/ kafka:/srv/rkd/www/scicomp/