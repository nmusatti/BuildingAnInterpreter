'''
Created on Apr 26, 2015

@author: nick
'''

from snap.scanner import grammar, Scanner
from snap.ast import Assign, BinaryOperation, Integer, Output, String
from rply import ParserGenerator 

tokens = [ r[0] for r in grammar ]

pg = ParserGenerator(tokens)

@pg.production(r'program : program statement')
@pg.production(r'program : statement')
def program(p):
    if len(p) == 1:
        return [ p[0] ]
    else:
        l = p[0]
        l.extend(p[1])
        return l

@pg.production(r'statement : assign')
@pg.production(r'statement : output')
def statement(p):
    return p[0]

@pg.production(r'assign : VARIABLE EQUALS binary_operation')
def assign(p):
    return Assign(p[0].value, p[2])
    
@pg.production(r'binary_operation : value PLUS value')
def binary_operation(p):
    return BinaryOperation(p[1].value, p[0], p[2])

@pg.production(r'value : INTEGER')
@pg.production(r'value : STRING')
def value(p):
    if p[0].gettokentype() == 'INTEGER':
        return Integer(p[0].value)
    else:
        return String(p[0].value)

@pg.production(r'output : PRINT LPAR VARIABLE RPAR')
def output(p):
    return Output(p[2])


class Parser(object):
    def __init__(self):
        self.scanner = Scanner()
        self.parser = pg.build()

    def parse(self, text):
        return self.parser.parse(self.scanner.scan(text))


def parse(text):
    p = Parser()
    return p.parse(text)

