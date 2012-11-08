'''
Created on 2012-11-08

@author: Gal
'''
import random

def printGraph():
    print ""
def avg(l):
    return (float(sum(l)))/(len(l))
def generateTossesStatistics(maxN, p):
    stats = []
    tosses = generateTosses(maxN,p)
    for i in xrange (1,maxN+1):
        tails = avg(tosses[:i+1])
        heads = 1 - tails
        stats.append((i,heads,tails))
    return stats
    
def generateTosses(N,p):
    #p = random.uniform(minimum,maximum)
    tosses = list()
    for i in xrange(1,N+1):
        tosses.append(toss(p))
    return tosses

def toss(p):
    num = random.uniform(0,1)
    if (num<=p):
        return 0 #"Heads"
    return 1 #"Tails"