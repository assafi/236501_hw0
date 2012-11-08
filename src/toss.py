'''
Created on 2012-11-08

@author: Gal
'''
import random

def printGraph():
    print ""

def generateTossesStatistics(minimum,maximum,maxN):
    stats = []
    for i in range (1,maxN+1):
        tosses = generateTosses(minimum,maximum, i)
        tails = sum(tosses)
        heads = i - sum(tosses)
        stats.append((i,heads,tails))
    return stats
    
def generateTosses(minimum,maximum,N):
    p = random.uniform(minimum,maximum)
    tosses = list()
    for i in range(1,N+1):
        tosses.append(toss(p))
    return tosses

def toss(p):
    num = random.uniform(0,1)
    if (num<=p):
        return 0 #"Heads"
    return 1 #"Tails"