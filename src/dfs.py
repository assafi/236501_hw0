'''

@author: Gal
'''

def dfs(graph,isGoal):
    return dfsRec(graph,isGoal,graph.root, set())

def dfsRec(graph,isGoal,node,visited):
    if isGoal(node.data):
        return graph.op_path(node)
    if node in visited:
        return None#already searched here...
    visited.add(node)
    for succ in node.succ():
        recursionResult = dfsRec(graph,isGoal,succ,visited)
        if recursionResult != None:
            return recursionResult
    return None#did not find
def limitedDfs(graph,isGoal,maxDepth):
    #print "limitedDfs(_,_,depth:" + str(maxDepth) 
    return limitedDfsRec(graph,isGoal,graph.root,maxDepth,set())

def limitedDfsRec(graph,isGoal,node,maxDepth, visited):
    #print "depth = " + str(maxDepth)
    if maxDepth <= 0:
        return None#did not find
    if isGoal(node.data):
        #print "Found"
        return graph.op_path(node)
    if node in visited:
        #print "already visited node: " + str(node.data)
        return None#already searched here...
    visited.add(node)
    for succ in node.succ():
        recursionResult = limitedDfsRec(graph,isGoal,succ,maxDepth-1, visited)
        if recursionResult != None:
            return recursionResult
    return None#did not find

def idDfs(graph,isGoal,maxDepth):
    for i in range(1,maxDepth+1):
        solution = limitedDfs(graph,isGoal,i)
        if  solution != None:
            return solution
    return None