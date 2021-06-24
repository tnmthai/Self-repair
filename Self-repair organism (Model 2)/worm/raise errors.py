# -*- coding: utf-8 -*-
"""
Created on Thu Apr 04 15:54:16 2019

@author: trann5
"""


try:
    x = 10
    if x > 5:
        raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
except Exception as err:
    print 'aaa',err
    
    
    
import math
pi = math.pi

def PointsInCircum(r,n=100):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

#print PointsInCircum(2,12)    

def abc():
    
    return 1,2
_,_=abc()
print _




print(' Menu')
print('1. insert <data> after <index>')
print('2. insert <data> before <index>')
print('3. quit')
 
while True:
    
    
    print()
    do = input('What would you like to do? ')

     
    if do == 1:
        print 'choose 1'
         
    elif do == 2:
        print 'choose 2'
 
    elif do == 3:
        break