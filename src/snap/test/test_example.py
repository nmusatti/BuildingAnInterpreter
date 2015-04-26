'''
Created on Apr 26, 2015

@author: nick
'''
import unittest

from snap.ast import Assign, BinaryOperation, Integer
from snap.scanner import scan
from snap.parser import parse


_text = """
foo = 2 + 7
bar = "cat" + "dog"
print(foo)
print(bar)
"""

class Test(unittest.TestCase):

    def test_scanner(self):
        l = [ t for t in scan(_text) ]
        for i in ( 0, 5, 12, 16 ):
            self.assertEqual(l[i].gettokentype(), 'VARIABLE')
        for i in ( 1, 6 ):
            self.assertEqual(l[i].gettokentype(), 'EQUALS')
        for i in ( 2, 4 ):
            self.assertEqual(l[i].gettokentype(), 'INTEGER')
        for i in ( 7, 9 ):
            self.assertEqual(l[i].gettokentype(), 'STRING')

    def test_example(self):
        a = parse(r'foo = 2 + 7')[0]
        self.assertEqual(a, Assign("foo", BinaryOperation("+", Integer(2), Integer(7))))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_example']
    unittest.main()