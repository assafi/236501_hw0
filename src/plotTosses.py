'''
Created on 2012-11-08

@author: Gal
'''
from toss import generateTossesStatistics
import matplotlib.pyplot as plt
#import random

def plotN(N,p1,p2):
    tosses1 = generateTossesStatistics(N,p1)
    tosses2 = generateTossesStatistics(N,p2)
    
    tosses1X = map(lambda x: x[0], tosses1)
    tosses1Y = map(lambda x: x[1], tosses1)
    tosses2X = map(lambda x: x[0], tosses2)
    tosses2Y = map(lambda x: x[1], tosses2)
    '''
    (X,Y)
    (#Tosses,#heads,#tails)
    '''  
    
    #plt.plot([1,2,3,4],[1,4,9,16],'ro')
    #plt.plot([1,2,3,4],[1,2,3,4],'ro',[1,2,3,4],[1,4,9,16],'bs')
    plt.plot(tosses1X,tosses1Y,'ro--',[0,N+1],[p1,p1],'ro-',tosses2X,tosses2Y,'bs--',[0,N+1],[p2,p2],'bs-')
    plt.axis([0, N+1, 0, 1])
    plt.ylabel('average heads probability for each coin')
    #plt.show()
    s = "plot N_%d p1_%0.3f p2_%0.3f.png" %(N,p1,p2)
    #plt.savefig('plot'+ str(N)+"_p1_" +str(p1)+"_p2_" +str(p2)+'.png')
    '''plt.annotate('local max', xy=(10, 10), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
            '''
    plt.savefig(s)
if __name__ == '__main__':
    '''
    minimum = 0.8
    maximum = 0.9
    p1 = random.uniform(minimum,maximum)
    p2 = random.uniform(minimum,maximum)
    '''
    p1 = 0.8
    p2 = 0.9
    plotN(20,p1,p2)
    plotN(50,p1,p2)
    plotN(100,p1,p2)
    plotN(500,p1,p2)
    plotN(1000,p1,p2)
    plotN(10000,p1,p2)
    plotN(20000,p1,p2)