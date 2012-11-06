'''
Created on 2012-11-04

@author: assafi
'''
import unittest
from graph import *

def op1(node):
    return [Node(chr(ord(node.data) + 1),node,[op1])]

class Test(unittest.TestCase):

    def testName(self):
        g = Graph(Node('a',None,[op1]))
        b = g.root.succ().pop()
        print g.op_path(b)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()