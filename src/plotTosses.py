'''
Created on 2012-11-08

@author: Gal
'''
from toss import generateTossesStatistics
import matplotlib.pyplot as plt

def plotN(N):
        
    minimum = 0.8
    maximum = 0.9
    tosses1 = generateTossesStatistics(minimum,maximum,N)
    tosses2 = generateTossesStatistics(minimum,maximum,N)
    
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
    plt.plot(tosses1X,tosses1Y,'ro-',tosses2X,tosses2Y,'bs--')
    plt.axis([0, N+1, 0, N+1])
    plt.ylabel('bla bla')
    #plt.show()
    plt.savefig('plot'+ str(N) +'.png')

if __name__ == '__main__':
    plotN(20)
    plotN(50)
    plotN(100)