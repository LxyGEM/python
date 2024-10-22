#encoding:utf-8
import sys,re
from handlers import *
from util import *
from rules import *

class Parser:
    # Initialize some attributes
    def __init__(self,handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    # Add rules to the rule list
    def addRule(self,rule):
        self.rules.append(rule)
    # Add filters to the filter list
    def addFilter(self,pattern,name):
        # Create a filter, which is actually a substitution formula
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    # Process the file
    def parse(self,file):
        self.handler.start('document')
        # Apply filters and rules to each text block in the file in turn
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block,self.handler)
            for rule in self.rules:
                # Determine whether the text block meets the corresponding rule, and if so, execute the processing method corresponding to the rule
                if rule.condition(block):
                    last = rule.action(block,self.handler)
                    if last:break
        self.handler.end('document')

class BasicTextParser(Parser):
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*','emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)','url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
