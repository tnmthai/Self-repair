# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:06:40 2020

@author: trann5
"""
import numpy as np
import copy
import itertools
import random

# W1=np.array([[ 0.  ,  0.5 ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,
#           0.  ,  0.  ,  0.  ,  0.  ],
#         [-0.01,  0.  ,  0.3,  0.3,  0.3,  0.  ,  0.  ,  0.  ,  0.  ,
#           0.  ,  0.  ,  0.  ,  0.  ],
#         [ 0.  , -0.01,  0.  ,  0.3,  0.3,  0.3,  0.  ,  0.  ,  0.  ,
#           0.  ,  0.  ,  0.  ,  0.  ],
#         [ 0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,  0.3,  0.  ,  0.  ,
#           0.  ,  0.  ,  0.  ,  0.  ],
#         [ 0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,  0.  ,  0.3,  0.  ,
#           0.  ,  0.  ,  0.  ,  0.  ],
#         [ 0.  ,  0.  , -0.01,  0.  ,  0.  ,  0.  ,  0.3,  0.3,  0.3,
#           0.  ,  0.  ,  0.  ,  0.  ],
#         [ 0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.1 ,  0.  ,  0.  ,  0.  ,
#           0.3,  0.  ,  0.  ,  0.  ],
#         [ 0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,
#           0.  ,  0.3,  0.  ,  0.  ],
#         [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.  ,  0.  ,
#           0.3 ,  0.3 ,  0.3 ,  0.  ],
#         [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.1 ,
#           0.  ,  0.3,  0.  ,  0.  ],
#         [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.1 ,
#           0.  ,  0.  ,  0.3,  0.  ],
#         [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,
#         -0.01, -0.01,  0.  ,  0.38],
#         [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,
#           0.  ,  0.  , -0.01,  0.  ]])

W1=np.array([[ 0.  ,  0.5 ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [-0.01,  0.  ,  0.32,  0.32,  0.32,  0.  ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  , -0.01,  0.  ,  0.29,  0.29,  0.29,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,  0.39,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,  0.  ,  0.38,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  ,  0.  , -0.01,  0.  ,  0.  ,  0.  ,  0.29,  0.29,  0.29,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.1 ,  0.  ,  0.  ,  0.  ,
          0.36,  0.  ,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.36,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.  ,  0.  ,
          0.3 ,  0.3 ,  0.3 ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.1 ,
          0.  ,  0.34,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.1 ,
          0.  ,  0.  ,  0.36,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,
        -0.01, -0.01,  0.  ,  0.38],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  , -0.01,  0.  ]])
# B=[0.2903901, 0.1956955, 0.2410408, 0.1953952, 0.1980979, 0.2009007,
#        0.1523522, 0.1543542, 0.1562561, 0.1048047, 0.1060059, 0.9678669,
#        0.8625617]
W=np.array([[ 0.  ,  0.5 ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [-0.01,  0.  ,  0.32,  0.32,  0.32,  0.  ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  , -0.01,  0.  ,  0.29,  0.29,  0.29,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,  0.36,  0.  ,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,  0.  ,  0.38,  0.  ,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  ,  0.  , -0.01,  0.  ,  0.  ,  0.  ,  0.29,  0.29,  0.29,
          0.  ,  0.  ,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.1 ,  0.  ,  0.  ,  0.  ,
          0.36,  0.  ,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.1 ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.36,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.  ,  0.  ,
          0.3 ,  0.3 ,  0.3 ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.  ,  0.1 ,
          0.  ,  0.34,  0.  ,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,  0.1 ,
          0.  ,  0.  ,  0.36,  0.  ],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.01,
        -0.01, -0.01,  0.  ,  0.38],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,
          0.  ,  0.  , -0.01,  0.  ]])

B=[0.445, 0.168, 0.132, 0.301, 0.303, 0.123, 0.285, 0.284, 0.12 ,0.247, 0.26 , 0.303, 0.299]
B1=[0.4,0.15,0.13,0.3,0.3,0.13,0.3,0.3,0.13,0.25,0.25,0.3,0.3]

def updateW(P):
    
    global W,B,B1
    for p in range (len(P)):
        if P[p]==0:
            B[p]=B1[p]
            
            for i in range (13):  
                if W[i,p] >0:
                    W[i,p]=0.3
                elif W[i,p] <0:
                    W[i,p]= -0.01
                    
                if W[p,i] >0 :
                    W[p,i]=0.3
                elif W[p,i] <0:
                    W[p,i]= -0.01
    W[0,1]=0.5
    W[11,12]=0.38
                

    # return W

def distance(v, u):
   return sum((v_i - u_i)**2 for v_i, u_i in zip(v, u))**0.5


def Check(A):

    B=copy.copy(A)
    C=HNN(A)
    D=[0.8, 0.7, 0.6, 0.55, 0.55, 0.55, 0.5, 0.5, 0.5, 0.45, 0.45, 0.4, 0.3]
    # print ('d',distance(C,B))
    for i in range( len(B)):
        if B[i]==0:
            return i,0
            break

    if distance(C,B)>0.0001:
        # print ("Changed")
        return -1,D#C
    elif distance(C,B)>0.01:
        return 0,0 #damage
    else:
        # print ("Normal")
        return -2,D#C

def testing(A):
    for _ in range(100):
        for i in range(len(A)):#
            a= np.dot(W[i], A) + B[i]
            A[i] = 1.0 if a >= 1.0 else 0.0 if a <0.0 else round(a,2)

    if distance(A,T)==0:
        return A,"OK"
    else:
        return A,distance(A,T)
    

def perturbation(per1,per2):
    global W
    total=156
    # no=int(round((100*total)/100,0))
    rdlist=random.sample(range(total),total)

    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    results = list(itertools.permutations(numbers, 2)) #all pairs

    # print (rdlist, len(rdlist))

    for l in rdlist:
        W[results[l]] += W[results[l]]*np.random.choice([-1,1])*np.random.randint(per1, per2)/100
        # W[results[l]] += W[results[l]]*-1*per2/100
        # np.random.choice([-1,1])*int(np.random.choice(5, 1))/100

    return W
def pertBias(per1,per2):
    global B
    for i in range (len (B)):
        B[i] += B[i]*np.random.choice([-1,1])*np.random.randint(per1, per2)/100
        # B[i] += B[i]*-1*per2/100
        # np.random.choice([-1,1])*int(np.random.choice(5, 1))/100
        # print (B)



def HNN(A):
    # print (W)
    global W
    for _ in range(100):
        for i in range(len(A)):            
            a= np.dot(W[i], A) + B[i]
            A[i] = 1.0 if a >= 1.0 else 0.0 if a <=0.0 else round(a,2)
        
    return A

T=[0.8, 0.7, 0.6, 0.55, 0.55, 0.55, 0.5, 0.5, 0.5, 0.45, 0.45, 0.4, 0.3]
X=[0.8, 0.7, 0.6, 0.55, 0.55, 0.55, 0, 0.5, 0.5, 0.45, 0.45, 0.4, 0.3]
X2 =[0.8, 0.7, 0.6, 0.6, 0.6, 0.55, 0.55, 0.55, 0.5, 0.5, 0.5, 0.4, 0.3]



# updateW(X)
# print (W)
print (testing(X))
# print (B)

# per1=0
# per2=5
# perturbation(per1,per2)
# print (HNN(X))
# pertBias(per1,per2)
# print (B)
# print (HNN(X))
# print (testing(X2))
# print (HNN(X))
# with open('data13.txt') as f:
#     lines = f.readlines();
#     for line in lines:
#         line = line.strip()
#         line = line.split(",")
#         i = list(line)
#         inputs =list(map(float, i))
#         C = copy.copy(inputs)
#         print('\nTest:', testing(C))


# c=0
# per=0
# for i in range (13):
#     for j in range (13):
#         if W1[i,j]!=0:
#             c+=1
#             per += (W1[i,j]/W[i,j] -1)
#             print(per)
# print (c,per/c)
# for i in range (len(B)):
#     per += (B1[i]/B[i] - 1)
#     c+=1
    
# print (c,per/c)
