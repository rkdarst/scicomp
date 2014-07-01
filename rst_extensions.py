
from docutils import nodes
from docutils.parsers.rst import directives, Directive

class TutorialIndex(Directive):
    """ Source code syntax hightlighting.
    """
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = { }
    has_content = True

    def run(self):
        ns = [ ]

        table = nodes.table()

        rows = [ ]
        for i in range(10):
            row = nodes.row()
            row.append(nodes.Element('aa%s'%i))
            row.append(nodes.paragraph('bb%s'%i))
            table.append(row)

        return [table ]

    def run(self):
        l = nodes.bullet_list('ul-name')
        for line in self.content:
            #print line

            path, rest = line.split(' ', 1)
            line_text = rest

            text_nodes, messages = self.state.inline_text(line_text,
                                                          self.lineno)
            line = nodes.line(line_text, '', *text_nodes)
            item = nodes.list_item(line_text, line)
            l.append(item)

            # Make the sub-list
            l2 = nodes.bullet_list('ul-name')
            for ext, title in [('.html', 'Main text'),
                               ('-big.html', 'Big text (for presentation)'),
                               ('-s5.html', 'Slide Show'),
                               ]:
                line_text = '`%s <%s%s>`__'%(title.strip(), path, ext)
                #print line_text

                text_nodes, messages = self.state.inline_text(line_text,
                                                              self.lineno)
                line = nodes.line(line_text, '', *text_nodes)
                #print type(line)
                item2 = nodes.list_item(line_text, line)

                l2.append(item2)

            item.append(l2)


        return [l, nodes.paragraph('hi')]


directives.register_directive('tut-index', TutorialIndex)
