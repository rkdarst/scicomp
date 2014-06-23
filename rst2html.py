try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description

import pygments_rst

description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)

import sys
import re
writer_name = re.search(r'rst2([^.]+)(.py)?', sys.argv[0]).group(1)

publish_cmdline(writer_name=writer_name, description=description)
