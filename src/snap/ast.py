'''
Created on Apr 26, 2015

@author: nick
'''

from rply.token import BaseBox

class Node(BaseBox):
    """ The abstract AST node
    """
    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self == other

class Integer(Node):
    def __init__(self, value):
        self.value = int(value)
    
    def __repr__(self):
        return "Integer(%d)" % self.value


class String(Node):
    def __init__(self, value):
        self.value = str(value)
    
    def __repr__(self):
        return "String(%s)" % self.value


class BinaryOperation(Node):
    def __init__(self, op, first, second):
        self.op = op
        self.first = first
        self.second = second

    def __repr__(self):
        return "BinaryOperation(%s, %s, %s)" % ( self.op, self.first, self.second )


class Assign(Node):
    def __init__(self, var, value):
        self.var = var
        self.value = value
    
    def __repr__(self):
        return "Assign(%s, %s)" % ( self.var, self.value )


class Output(Node):
    def __init__(self, var):
        self.var = var
    
    def __repr__(self):
        return "Output(%s)" % self.var

