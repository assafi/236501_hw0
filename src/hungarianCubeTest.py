'''
Created on 8/11/2012

@author: Assaf
'''
import unittest
from graph import Graph
from bfs import *
from dfs import *
from hungarianCube import *
import time

class Test(unittest.TestCase):
    def __init__(self,argToSuper):
        super(Test,self).__init__(argToSuper)
        self.rotations = []
        cube = HungarianCube()
        node = Node(cube)
        self.rotations+=[node]
        node = rotateRightRight(node)[0]
        self.rotations+=[node]
        node = rotateTopRight(node)[0]
        self.rotations+=[node]
        node = rotateBackRight(node)[0]
        self.rotations+=[node]
        node = rotateLeftRight(node)[0]
        self.rotations+=[node]
        node = rotateBackRight(node)[0]
        self.rotations+=[node]
        node = rotateRightLeft(node)[0]
        self.rotations+=[node]
        node = rotateBottomRight(node)[0]
        self.rotations+=[node]
        node = rotateTopLeft(node)[0]
        self.rotations+=[node]
        node = rotateFrontRight(node)[0]
        self.rotations+=[node]
        node = rotateFrontRight(node)[0]
        self.rotations+=[node]
    
    def test_rotateSideRight(self):
        a = [1,2,3,4,5,6,7,8,9]
        rotateSideRight(a)
        self.assertEquals([7,4,1,8,5,2,9,6,3], a)
    
    def test_rotateSideLeft(self):
        a = [1,2,3,4,5,6,7,8,9]
        rotateSideRight(a)
        rotateSideLeft(a)
        self.assertEquals(range(1,10,1), a)
        
    def test_rotateTopCubeSideToRight(self):
        cube = HungarianCube()
        afterCube = rotateTopRight(Node(cube))[0].data
        self.assertEquals(afterCube.top,[1]*9)
        self.assertEquals(afterCube.left,[6]*3 + [4]*6)
        self.assertEquals(afterCube.back, [5]*6 + [4]*3)
    
    def test_rotateTopCubeSideToLeft(self):
        cube = HungarianCube()
        node = rotateTopRight(Node(cube))[0]
        afterCube = rotateTopLeft(node)[0].data
        self.assertEquals(cube,afterCube)
    
    def test_rotateRightCubeSideToRight(self):
        cube = HungarianCube()
        afterCube = rotateRightRight(Node(cube))[0].data
        self.assertEquals(afterCube.right, [2]*9)
        self.assertEquals(afterCube.bottom, [3,3,5]*3)
    
    def test_rotateRightCubeSideToLeft(self):
        cube = HungarianCube()
        node = rotateRightRight(Node(cube))[0]
        afterCube = rotateRightLeft(node)[0].data
        self.assertEquals(afterCube, cube)
        
    def test_rotateLeftCubeSideToRight(self):
        cube = HungarianCube()
        afterCube = rotateLeftRight(Node(cube))[0].data
        self.assertEquals(afterCube.left, [4]*9)
        self.assertEquals(afterCube.top, [5,1,1]*3)
    
    def test_rotateLeftCubeSideToLeft(self):
        cube = HungarianCube()
        node = rotateLeftRight(Node(cube))[0]
        afterCube = rotateLeftLeft(node)[0].data
        self.assertEquals(afterCube, cube)
    
    def test_rotateBottomCubeSideToRight(self):
        cube = HungarianCube()
        afterCube = rotateBottomRight(Node(cube))[0].data
        self.assertEquals(afterCube.bottom, [3]*9)
        self.assertEquals(afterCube.back, [2]*3 + [5]*6)
    
    def test_rotateBottomCubeSideToLeft(self):
        cube = HungarianCube()
        node = rotateBottomRight(Node(cube))[0]
        afterCube = rotateBottomLeft(node)[0].data
        self.assertEquals(afterCube, cube)
        
    def test_rotateFrontCubeSideToRight(self):
        cube = HungarianCube()
        afterCube = rotateFrontRight(Node(cube))[0].data
        self.assertEquals(afterCube.front, [6]*9)
        self.assertEquals(afterCube.right, [1,2,2]*3)
    
    def test_rotateFrontCubeSideToLeft(self):
        cube = HungarianCube()
        node = rotateFrontRight(Node(cube))[0]
        afterCube = rotateFrontLeft(node)[0].data
        self.assertEquals(afterCube, cube)
        
    def test_rotateBackCubeSideToRight(self):
        cube = HungarianCube()
        afterCube = rotateBackRight(Node(cube))[0].data
        self.assertEquals(afterCube.back, [5]*9)
        self.assertEquals(afterCube.bottom, [3]*6 + [4]*3)
    
    def test_rotateBackCubeSideToLeft(self):
        cube = HungarianCube()
        node = rotateBackRight(Node(cube))[0]
        afterCube = rotateBackLeft(node)[0].data
        self.assertEquals(afterCube, cube)    
        
    def test_simpleHungarianCube(self):
        cube = HungarianCube()
        g = Graph(cube,hungrarianCubeOperators())
        path = bfs(g,hungarianCubePredicate)
        self.assertEquals(map(lambda x: x.data, path),[cube])
        
    def test_oneStepHCube(self):
        cube = HungarianCube()
        node = Node(cube,None,[])
        cube2 = rotateFrontLeft(node)[0].data
        g = Graph(cube2,hungrarianCubeOperators())
        path = bfs(g,hungarianCubePredicate)
        self.assertEquals(len(path),2)
        print path[0].data
        print "-----"
        print path[1].data
        
    def test_twoStepsHCube(self):
        cube = HungarianCube()
        print "original"
        node = Node(cube)
        print node.data
        print "*****"
        node = rotateFrontLeft(node)[0]
        print node.data
        print "*****"
        cube2 = rotateRightRight(node)[0].data
        print cube2
        print "*****"
        g = Graph(cube2,hungrarianCubeOperators())
        path = bfs(g,hungarianCubePredicate)
        self.assertEquals(len(path),3)
        print "Solution"
        print path[0].data
        print "-----"
        print path[1].data
        print "-----"
        print path[2].data
        print "-=-=-=-=-=-"
    def test_stressTestBfs(self):
        print "Stress Test BFS"
        node = self.rotations[4]
        g = Graph(node.data,hungrarianCubeOperators())
        path = bfs(g,hungarianCubePredicate)
        
        for x in path:
            print x.data
            print "------"
        print "*&*&*&*&*&*&"

    def test_stressTestIdDfs(self):
        print "Stress Test ID-DFS"
        node = self.rotations[6]
        g = Graph(node.data,hungrarianCubeOperators())
        path = idDfs(g,hungarianCubePredicate,6)
        self.assertTrue(path is None)
        for x in path:
            print x.data
            print "------"
        print "*&*&*&*&*&*&"
    
    def test_stressTestIdDfsFail(self):
        print "Stress Test ID-DFS"
        node = self.rotations[6]
        g = Graph(node.data,hungrarianCubeOperators())
        path = idDfs(g,hungarianCubePredicate,4)
        self.assertFalse(path is None)
    
    def stressTestBfsLevel(self,count):
        print "Started BFS with " + str(count)
        start = time.clock()
        node = self.rotations[count]
        g = Graph(node.data,hungrarianCubeOperators())
        path = bfs(g,hungarianCubePredicate)
        self.assertFalse(path is None)
        elapsed = (time.clock() - start)
        print "Done BFS with " + str(count)+ " levels " +"on " + str(elapsed) +" seconds"
    
    def stressTestIdDfsLevel(self,count):
        print "Started ID-DFS with " + str(count)
        start = time.clock()
        node = self.rotations[count]
        g = Graph(node.data,hungrarianCubeOperators())
        path = idDfs(g,hungarianCubePredicate,count+1)
        self.assertFalse(path is None)
        elapsed = (time.clock() - start)
        print "Done ID-Dfs with " + str(count)+ " levels " +"on " + str(elapsed) +" seconds"

    def stressTestLimitedDfsLevel(self,count):
        print "Started Limited-DFS with " + str(count)
        start = time.clock()
        node = self.rotations[count]
        g = Graph(node.data,hungrarianCubeOperators())
        path = limitedDfs(g,hungarianCubePredicate,count+1)
        elapsed = (time.clock() - start)
        if (path is None):
            print "Failed Limited-Dfs with " + str(count)+ " levels " +"on " + str(elapsed) +" seconds"
        else:
            print "Done Limited-Dfs with " + str(count)+ " levels " +"on " + str(elapsed) +" seconds"

    
    def test_CompareDFS_BFS(self):
        print "started master test"
        DFS_LIMIT = 3
        BFS_LIMIT = 4 
        for i in xrange(1,DFS_LIMIT+1):
            self.stressTestLimitedDfsLevel(i)
        for i in xrange(1,DFS_LIMIT+1):
            self.stressTestIdDfsLevel(i)
        for i in xrange(1,BFS_LIMIT+1):
            self.stressTestBfsLevel(i)
        print "done"
        
if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testHungrarianCube']
    unittest.main()