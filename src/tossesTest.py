'''
Created on 2012-11-08

@author: Gal
'''
import unittest
from toss import generateTosses,generateTossesStatistics

class Test(unittest.TestCase):

    def testgenerateTossesStatistics(self):
        minimum = 0.8
        maximum = 0.9
        N = 10
        tosses = generateTossesStatistics(minimum,maximum,N)
        for x in tosses:
            print x
        '''
        (X,Y)
        (#Tosses,#heads,#tails)
        '''  

    def testTosses(self):
        minimum = 0.8
        maximum = 0.9
        N = 10
        tosses = generateTosses(minimum,maximum,N)
        for x in tosses:
            print x
            '''
        for x in tosses:
            self.assertFalse(x<minimum or x>maximum)
            '''
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTosses']
    unittest.main()