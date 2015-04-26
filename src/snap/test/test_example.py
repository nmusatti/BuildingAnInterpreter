'''
Created on Apr 26, 2015

@author: nick
'''
import unittest

from snap.ast import Assign, BinaryOperation, Integer
from snap.parser import parse


_text = """
foo = 2 + 7
bar = "cat" + "dog"
print(foo)
print(bar)
"""

class Test(unittest.TestCase):


    def test_example(self):
        self.assertEqual(parse(_text), Assign("foo", BinaryOperation("+", Integer(2), Integer(7))))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_example']
    unittest.main()