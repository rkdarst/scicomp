# -*- coding: utf-8 -*-
"""
    The Pygments reStructuredText directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This fragment is a Docutils_ 0.5 directive that renders source code
    (to HTML only, currently) via Pygments.

    To use it, adjust the options below and copy the code into a module
    that you import on initialization.  The code then automatically
    registers a ``sourcecode`` directive that you can use instead of
    normal code blocks like this::

        .. sourcecode:: python

            My code goes here.

    If you want to have different code styles, e.g. one with line numbers
    and one without, add formatters with their names in the VARIANTS dict
    below.  You can invoke them instead of the DEFAULT one by using a
    directive option::

        .. sourcecode:: python
            :linenos:

            My code goes here.

    Look at the `directive documentation`_ to get all the gory details.

    .. _Docutils: http://docutils.sf.net/
    .. _directive documentation:
       http://docutils.sourceforge.net/docs/howto/rst-directives.html

    :copyright: Copyright 2006-2012 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os

# Options
# ~~~~~~~

# Set to True if you want inline CSS styles instead of classes
INLINESTYLES = True

from pygments.formatters import HtmlFormatter

# The default formatter
#DEFAULT = HtmlFormatter(noclasses=INLINESTYLES)
DEFAULT = HtmlFormatter(noclasses=INLINESTYLES, linenos=True)

# Add name -> formatter pairs for every variant you want to use
VARIANTS = {
    # 'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
    'lineno': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
}


from docutils import nodes
from docutils.parsers.rst import directives, Directive

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer

class Pygments(Directive):
    """ Source code syntax hightlighting.
    """
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = dict([(key, directives.flag) for key in VARIANTS])
    has_content = True
    default_lexer = 'python'

    def get_lexer(self, lexername=None):
        if lexername:
            lexer_name = lexername
        elif len(self.arguments) > 0:
            lexer_name = self.arguments[0]
        else:
            lexer_name = self.default_lexer
        try:
            lexer = get_lexer_by_name(lexer_name)
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = get_lexer_by_name(self.default_lexer)
        # take an arbitrary option if more than one is given
        return lexer
    def get_formatter(self):
        formatter =self.options and VARIANTS[self.options.keys()[0]] or DEFAULT
        return formatter

    def run(self):
        lexer = self.get_lexer()
        formatter = self.get_formatter()

        self.assert_has_content()
        parsed = highlight(u'\n'.join(self.content), lexer, formatter)
        return [nodes.raw('', parsed, format='html')]

class PygmentsInclude(Pygments):
    has_content = False
    required_arguments = 1
    optional_arguments = 1
    default_lexer = 'python'
    def run(self):
        if len(self.arguments) == 1:
            lexer = None
            fname = self.arguments[0]
        else:
            lexer = self.arguments[0]
            fname = self.arguments[1]

        lexer = self.get_lexer(lexer)
        formatter = self.get_formatter()

        data = os.path.join(os.path.dirname(self.src), fname)
        if not os.path.exists(data):
            return [nodes.raw('', "File does not exist: %s"%data, format='html')]
        data = open(data).read()

        parsed = highlight(data, lexer, formatter)
        parsed = '''<b><small><a href=%s style="color:gray">%s</a>:</small></b>\n'''%(
            fname,fname) + parsed
        return [nodes.raw('', parsed, format='html')]


directives.register_directive('sourcecode', Pygments)
directives.register_directive('code', Pygments)

class Python(Pygments):
    default_lexer = 'python'
class Console(Pygments):
    default_lexer = 'console'
directives.register_directive('python', Python)
directives.register_directive('console', Console)

directives.register_directive('pyinc', PygmentsInclude)
