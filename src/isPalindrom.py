'''
Created on 2012-11-04

@author: assafi
'''

def isPalindrom(st):
    for start, finish in zip(st,st[::-1]):
        if start != finish:
            return False
    return True
        
