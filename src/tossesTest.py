'''
Created on 2012-11-08

@author: Gal
'''
import unittest
from toss import generateTosses,generateTossesStatistics

class Test(unittest.TestCase):

    def testgenerateTossesStatistics(self):
        N = 10
        tosses = generateTossesStatistics(N,0.8)
        for x in tosses:
            print x
        '''
        (X,Y)
        (#Tosses,#heads,#tails)
        '''  

    def testTosses(self):
        N = 10
        tosses = generateTosses(N,0.85)
        for x in tosses:
            print x
            '''
        for x in tosses:
            self.assertFalse(x<minimum or x>maximum)
            '''
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTosses']
    unittest.main()