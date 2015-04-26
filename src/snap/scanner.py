'''
Created on Apr 26, 2015

@author: nick
'''

from rply import LexerGenerator

grammar = ( ('INTEGER', r'\d+'),
            ('STRING', r'"[^"]*"'),
            ('PLUS', r'\+'),
            ('EQUALS', r'='),
            ('LPAR', '\('),
            ('RPAR', '\)'),
            ('PRINT', r'print'),
            ('VARIABLE', r'[A-Za-z][A-Za-z0-9_]*') )


class Scanner(object):
    def __init__(self):
        _lg = LexerGenerator()
        for r in grammar:
            _lg.add(r[0], r[1])
        _lg.ignore(r'\s+')
        self._scanner = _lg.build()

    def scan(self, text):
        return self._scanner.lex(text)


def scan(text):
    s = Scanner()
    return s.scan(text)