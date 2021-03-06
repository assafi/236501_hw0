'''
Created on 2012-11-04

@author: Assaf Israel, Gal Cohen
email: assafi@cs.teh chnion.ac.il
email: galtechnion@gmail.com
'''

class Graph(object):
    '''
    A simple rooted-Graph implementation.
    '''

    def __init__(self, data, operators = ()):
        self.root = Node(data, None, operators)
        
    '''
    op_path returns an order list of nodes of the shortest path from 
    the specified node to the root of the graph, starting from the root.
    In case no route is found None is returned.
    '''
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
    
    '''
    Each Node contains data, can be linked to a parent, and contains a set of operators 
    (methods) which can be invoked upon to return the next set of Nodes.
    '''
    def __init__(self, data, parent = None, operators = ()):
        self.data = data
        self.operators = operators
        self.parent = parent
    
    '''
    succ returns a list of nodes generated by activating the of Nodes operators on itself.
    '''
    def succ(self):
        successors = set([])
        for op in self.operators:
            successors.update(op(self))
        return list(successors)
    
      
    def __repr__(self):
        return "<Node data:%s operators:%s parent:%s>" % (self.data, self.operators, self.parent)
    
    def __str__(self):
        return str(self.data)
    
    

   
        
        