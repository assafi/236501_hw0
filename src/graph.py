'''
Created on 2012-11-04

@author: assafi
'''

class Graph(object):
    '''
    A simple rooted-Graph implementation.
    '''

    def __init__(self, root):
        self.root = root
        self.nodes = set([root])
        
    def op_path(self, node):
        path = [node]
        while path[-1] is not self.root and path[-1].parent not in path:
            path.append(path[-1].parent)
        if path[-1] is not self.root:
            return None
        return path[::-1] #reverse path


class Node(object):
    '''
    A simple node abstraction
    '''
    
    def __init__(self, data, parent = None, operators = ()):
        self.data = data
        self.operators = operators
        self.parent = parent
    
    def succ(self):
        successors = set([])
        for op in self.operators:
            successors = successors.union(op(self))
        return successors
    
      
    def __repr__(self):
        return "<Node data:%s operators:%s parent:%s>" % (self.data, self.operators, self.parent)
    
    def __str__(self):
        return self.data
    
    

   
        
        