
FILES = $(wildcard tut/*/*.rst)

default: tut/index.html $(foreach x, $(FILES), $(basename $x).html)

tut/index.html: tut/index.rst
	python rst2html.py tut/index.rst tut/index.html --traceback

%.html: %.rst
	python rst2html.py $*.rst $*.html  --stylesheet=static/style.css --traceback
	python rst2html.py $*.rst $*-big.html  --stylesheet-path=static/style-docutils.css,static/style.css,static/style-big.css --template=./static/template-presentation.html
#	python rst2s5.py   $*.rst $*-s5.html  --stylesheet-path=style-docutils.css,style.css,style-big.css

#	If a file is named the same as a directory, link index.html
#	and big.html to the outputs.
	@test $$(basename `dirname $*`) = `basename $*` \
	        -a ! -e `dirname $*`/index.html \
	    && ln -s `basename $*`.html `dirname $*`/index.html || true
	@test $$(basename `dirname $*`) = `basename $*` \
	        -a ! -e `dirname $*`/big.html \
	    && ln -s `basename $*`-big.html `dirname $*`/big.html || true

pub: default
	rsync -avP --inplace --delete tut/ kafka:/srv/rkd/www/scicomp/