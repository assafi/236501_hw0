'''
Created on 2012-11-08

@author: assafi
'''
from graph import Node
import copy

class HungarianCube(object):
    def __init__(self):
        self.top = [1]*9
        self.right = [2]*9
        self.bottom = [3]*9
        self.left = [4]*9
        self.back = [5]*9
        self.front = [6]*9
    
    def __eq__(self,other):
        return self.top == other.top and \
            self.right == other.right and \
            self.bottom == other.bottom and \
            self.left == other.left and \
            self.back == other.back and \
            self.front == other.front 
    
    def __repr__(self):
        space = "         "
        msg = space + str(self.top[0:3]) + "\n"
        msg += space + str(self.top[3:6]) + "\n"
        msg += space + str(self.top[6:10]) + "\n"
        msg += str(self.left[0:3]) + str(self.front[0:3]) + str(self.right[0:3]) + "\n"
        msg += str(self.left[3:6]) + str(self.front[3:6]) + str(self.right[3:6]) + "\n"
        msg += str(self.left[6:10]) + str(self.front[6:10]) + str(self.right[6:10]) + "\n"
        msg += space + str(self.bottom[0:3]) + "\n"
        msg += space + str(self.bottom[3:6]) + "\n"
        msg += space + str(self.bottom[6:10]) + "\n"
        msg += space + str(self.back[0:3]) + "\n"
        msg += space + str(self.back[3:6]) + "\n"
        msg += space + str(self.back[6:10]) + "\n"
        return msg
    
    def __str__(self):
        space = "         "
        msg = space + str(self.top[0:3]) + "\n"
        msg += space + str(self.top[3:6]) + "\n"
        msg += space + str(self.top[6:10]) + "\n"
        msg += str(self.left[0:3]) + str(self.front[0:3]) + str(self.right[0:3]) + "\n"
        msg += str(self.left[3:6]) + str(self.front[3:6]) + str(self.right[3:6]) + "\n"
        msg += str(self.left[6:10]) + str(self.front[6:10]) + str(self.right[6:10]) + "\n"
        msg += space + str(self.bottom[0:3]) + "\n"
        msg += space + str(self.bottom[3:6]) + "\n"
        msg += space + str(self.bottom[6:10]) + "\n"
        msg += space + str(self.back[0:3]) + "\n"
        msg += space + str(self.back[3:6]) + "\n"
        msg += space + str(self.back[6:10]) + "\n"
        return msg

def rotateSideRight(side):
    newSideOrder = [6,3,0,7,4,1,8,5,2]
    sideClone = copy.copy(side)
    for i in xrange(0,9,1):
        side[i] = sideClone[newSideOrder[i]]

def rotateSideLeft(side):
    newSideOrder = [2,5,8,1,4,7,0,3,6]
    sideClone = copy.copy(side)
    for i in xrange(0,9,1):
        side[i] = sideClone[newSideOrder[i]]

def flipSide(side):
    reverse = side[::-1]
    for i in xrange(0,9,1):
        side[i] = reverse[i]
    
def rotateCubeSideRight(side,leftSide,rightSide,upperSide,lowerSide):
    rotateSideRight(side)
    copyUpperLower = upperSide[6:10]
    upperSide[6:9] = leftSide[2:9:3]
    leftSide[2:9:3] = lowerSide[0:3]
    lowerSide[0:3] = rightSide[0:7:3]
    rightSide[0:7:3] = copyUpperLower
    
def rotateCubeSideLeft(side,leftSide,rightSide,upperSide,lowerSide):
    rotateSideLeft(side)
    copyUpperLower = upperSide[6:10]
    upperSide[6:9] = rightSide[0:7:3]
    rightSide[0:7:3] = lowerSide[0:3]
    lowerSide[0:3] = leftSide[2:9:3]
    leftSide[2:9:3] = copyUpperLower

'''
Cube Operators
'''
    
def rotateTopLeft(node):
    cube = copy.deepcopy(node.data)
    rotateSideRight(cube.left)
    rotateSideLeft(cube.right)
    rotateCubeSideLeft(cube.top,cube.left,cube.right,cube.back,cube.front)
    rotateSideLeft(cube.left)
    rotateSideRight(cube.right)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateTopRight(node):
    cube = copy.deepcopy(node.data)
    rotateSideRight(cube.left)
    rotateSideLeft(cube.right)
    rotateCubeSideRight(cube.top,cube.left,cube.right,cube.back,cube.front)
    rotateSideLeft(cube.left)
    rotateSideRight(cube.right)
    return [Node(cube,node,hungrarianCubeOperators())]
    
def rotateRightRight(node):
    cube = copy.deepcopy(node.data)
    rotateSideRight(cube.top)
    flipSide(cube.back)
    rotateSideLeft(cube.bottom)
    rotateCubeSideRight(cube.right,cube.front,cube.back,cube.top,cube.bottom)
    rotateSideLeft(cube.top)
    flipSide(cube.back)
    rotateSideRight(cube.bottom)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateRightLeft(node):
    cube = copy.deepcopy(node.data)
    rotateSideRight(cube.top)
    flipSide(cube.back)
    rotateSideLeft(cube.bottom)
    rotateCubeSideLeft(cube.right,cube.front,cube.back,cube.top,cube.bottom)
    rotateSideLeft(cube.top)
    flipSide(cube.back)
    rotateSideRight(cube.bottom)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateBottomRight(node):
    cube = copy.deepcopy(node.data)
    rotateSideLeft(cube.left)
    rotateSideRight(cube.right)
    rotateCubeSideRight(cube.bottom,cube.left,cube.right,cube.front,cube.back)
    rotateSideRight(cube.left)
    rotateSideLeft(cube.right)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateBottomLeft(node):
    cube = copy.deepcopy(node.data)
    rotateSideLeft(cube.left)
    rotateSideRight(cube.right)
    rotateCubeSideLeft(cube.bottom,cube.left,cube.right,cube.front,cube.back)
    rotateSideRight(cube.left)
    rotateSideLeft(cube.right)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateLeftRight(node):
    cube = copy.deepcopy(node.data)
    flipSide(cube.back)
    rotateSideRight(cube.bottom)
    rotateSideLeft(cube.top)
    rotateCubeSideRight(cube.left,cube.back,cube.front,cube.top,cube.bottom)
    flipSide(cube.back)
    rotateSideLeft(cube.bottom)
    rotateSideRight(cube.top)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateLeftLeft(node):
    cube = copy.deepcopy(node.data)
    flipSide(cube.back)
    rotateSideRight(cube.bottom)
    rotateSideLeft(cube.top)
    rotateCubeSideLeft(cube.left,cube.back,cube.front,cube.top,cube.bottom)
    flipSide(cube.back)
    rotateSideLeft(cube.bottom)
    rotateSideRight(cube.top)
    return [Node(cube,node,hungrarianCubeOperators())]
    
def rotateBackRight(node):
    cube = copy.deepcopy(node.data)
    flipSide(cube.left)
    flipSide(cube.right)
    rotateCubeSideRight(cube.back,cube.left,cube.right,cube.bottom,cube.top)
    flipSide(cube.left)
    flipSide(cube.right)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateBackLeft(node):
    cube = copy.deepcopy(node.data)
    flipSide(cube.left)
    flipSide(cube.right)
    rotateCubeSideLeft(cube.back,cube.left,cube.right,cube.bottom,cube.top)
    flipSide(cube.left)
    flipSide(cube.right)
    return [Node(cube,node,hungrarianCubeOperators())]
    
def rotateFrontRight(node):
    cube = copy.deepcopy(node.data)
    rotateCubeSideRight(cube.front,cube.left,cube.right,cube.top,cube.bottom)
    return [Node(cube,node,hungrarianCubeOperators())]

def rotateFrontLeft(node):
    cube = copy.deepcopy(node.data)
    rotateCubeSideLeft(cube.front,cube.left,cube.right,cube.top,cube.bottom)
    return [Node(cube,node,hungrarianCubeOperators())]

'''
Cube predicate
'''

def hungarianCubePredicate(cube):
    return cube.top == [cube.top[0]]*9 and \
        cube.right == [cube.right[0]]*9 and \
        cube.bottom == [cube.bottom[0]]*9 and \
        cube.left == [cube.left[0]]*9 and \
        cube.back == [cube.back[0]]*9 and \
        cube.front == [cube.front[0]]*9 


def hungrarianCubeOperators():
    return [rotateTopLeft,rotateTopRight,rotateRightRight,\
            rotateRightLeft,rotateBottomRight,rotateBottomLeft,\
            rotateLeftRight,rotateLeftLeft,rotateBackRight,\
            rotateBackLeft,rotateFrontRight,rotateFrontLeft]
