'''
Created on 7/11/2012

@author: Assaf
'''

def bfs(graph, goal_predicate):
    opened = [graph.root]
    closed = set()
    while len(opened) > 0:
        node = opened.pop(0);
        if goal_predicate(node.data):
            return graph.op_path(node)
        if node.data not in closed:
            closed.add(node.data)
            opened += node.succ()
    return None
            
            
        