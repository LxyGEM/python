class Handler:
    """
    deal with the objects of functions from Parser
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if hasattr(method, '__call__'):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return substitution


class HTMLRender(Handler):
    """
    it is mainly used to produce HTML
    """

    def start_document(self):
        print("<html><head><title>...</title></head><body>")

    def end_document(self):
        print("</body></html>")

    def start_paragraph(self):
        print("<p>")

    def end_paragraph(self):
        print("</p>")

    def start_heading(self):
        print("<h2>")

    def end_heading(self):
        print("</h2>")

    def start_list(self):
        print("<ul>")

    def end_list(self):
        print("</ul>")

    def start_listitem(self):
        print("<li>")

    def end_listitem(self):
        print("</li>")

    def start_title(self):
        print("<h1>")

    def end_list(self):
        print("</h1>")

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        print(data)
        
import sys
import re
from handlers import *
from util import *
from rules import *


class Parser:
    """
    parser reads text,application rules
    and controls processing program
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    add rules and specific parser of filters in constructor function
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = HTMLRender()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)

class Rule:
    """
    the base class of all rules
    """
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    the title takes one line,
    and it`s less than 70 character,
    and it can`t end with colon
    """
    type = 'heading'

    def condition(self, block):
        return not'\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(HeadingRule):
    """
    title is the first block of document
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """
    listitem is paragraph which begins with hyphen,
    as a part of formatting,
    we should remove the hyphens
    """
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    the list is between the block which isn`t listitem
    and the following listitems,it ends after the last
    continue listitem.
    """
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    the paragraph is just something that other rules doesn`t cover
    """
    type = 'paragraph'

    def condition(self, block):
        return True
    
# a simple mark test
import sys
import re
from util import *

print('<html><head><title>...</title></head><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\l</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')

# text block builder
def lines(file):
    for line in file:
        yield line
        yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []