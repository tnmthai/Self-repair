# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:06:40 2020

@author: trann5
"""
import numpy as np
import copy

W= np.array([
    
(0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),
(-0.09,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),
(-0.09,-0.09,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,0,0.1,0.1,0.1,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,0,0.1,0.1,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,0,0.1,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,0,0.1,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,0,0.1,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,0,0.1),
(-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,-0.09,0)
    ])

# B=[0.1649648, 0.2197195, 0.2411409, 0.3107104, 0.4201197, 0.5307302,       0.5908903, 0.6927921, 0.7956949, 0.8459451, 0.9398389, 0.9671662,       0.9490481]

B=[0.15,0.23,0.31,0.39,0.47,0.55,0.63,0.71,0.79,0.87,0.95,0.95,0.95]

def distance(v, u):
   return sum((v_i - u_i)**2 for v_i, u_i in zip(v, u))**0.5


def Check(A):
    
    B=copy.copy(A)
    C=HNN(A)
    # print ('d',distance(C,B))
    for i in range( len(B)):
        if B[i]==0:
            return i,0
            break
        
    if distance(C,B)>0.0001:
        # print ("Changed")
        return -1,C
    elif distance(C,B)>0.01:
        return 0,0 #damage
    else:
        # print ("Normal")
        return -2,C
        
def testing(A,W,B,T):   
    for _ in range(10):
        for i in range(len(A)):#               
            a= np.dot(W[i], A) + B[i]            
            A[i] = 1.0 if a >= 1.0 else 0.0 if a <0.0 else round(a,2)

    if distance(A,T)==0:
        return A,"OK"
    else:
        return A,distance(A,T)   
    
def HNN(A):   
    k=0
    while True:
        k+=1
        for i in range(len(A)): 
            p=copy.copy(A)
            a= np.dot(W[i], A) + B[i]
            A[i] = 1.0 if a >= 1.0 else 0.0 if a <=0.0 else round(a,2)
        
        if distance(A,p)<=0.00 or k>100:   
            break

    return A
def LTF(x):
    x=float(x)
    if x >= 1.0:
        return 1.0
    elif x <= -1.0:
        return -1.0
    else:
        return x
import random    
def updateW():
    rate= 0.00001
    for _ in range(100): 
        for i in range(13):
           
            B[i] += round(rate,10)
            for j in range(13):
                nw =  (W[i, j] +  random.random()*rate)
                f = 1.0 if W[i, j]>0.0 else -1.0 if W[i, j]<0.0 else 0.0
    
                if i==j:
                    W[i, j] =  0
                elif f*nw > 0:
                    W[i, j]= nw         
                                    
    return W       

# # X =[0.80,0.70,0.60,0.55,0.55,0.50,0.50,0.45,0.45,0.40,0.40,0.40,0.31]
# X=[0.8, 0.7, 0.6, 0.55, 0.55, 0.55, 0.5, 0.5, 0.5, 0.45, 0.4503, 0.4, 0.3]
T =[0.8, 0.7, 0.6, 0.55, 0.55, 0.55, 0.5, 0.5, 0.5, 0.45, 0.45, 0.4, 0.3]
# print (HNN(X))
# W=updateW()
print (W,B)
with open('test13new.txt') as f:
    lines = f.readlines();
    for line in lines:
        line = line.strip()
        line = line.split(",")
        i = list(line)        
        inputs =list(map(float, i))    
        C = copy.copy(inputs)  
        print('\nTest:', testing(C,W,B,T))  


    
    
    
    
    
    

