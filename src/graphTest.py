'''
Created on 2012-11-04

@author: Assaf Israel
email: assafi@cs.technion.ac.il
'''
import unittest
from graph import *
from bfs import *

def op1(node):
    return [Node(chr(ord(node.data) + 1),node,[op1])]

def op2(node):
    node1 = Node(chr(ord(node.data) + 1),node,[op2])
    node2 = Node(chr(ord(node.data) + 2),node,[op2])
    return [node1,node2]

def goal_predicate1(data):
    return data == "d"

class Test(unittest.TestCase):

    def test_opPath(self):
        g = Graph('a',[op1])
        b = g.root.succ().pop()
        path = g.op_path(b)
        self.assertEqual(map(lambda x: x.data, path), ['a','b'])
    
    def test_bfs(self):
        g = Graph('a',[op2])
        path = bfs(g,goal_predicate1)
        self.assertTrue(['a', 'c', 'd'] == map(lambda x: x.data, path) or \
                        ['a', 'b', 'd'] == map(lambda x: x.data, path))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()