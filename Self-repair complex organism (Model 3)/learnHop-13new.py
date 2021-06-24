import numpy as np
import copy

nb_patterns = 1
pattern_width = 13
pattern_height = 1
max_iterations = 1 
import itertools
import random




def thresFunc(w):
    for i in range(len(w)):
        for j in range (len(w[i])):
            if w[i][j]>0: w[i][j]=1
            elif w[i][j]<0: w[i][j]=-1
            
    return w

def thresw(a):
    if a>1: return 1.0
    elif a<-1: return -1.0
    else: return a
            

def transFunc(I):
    for i in range(0, len(I)):
        if I[i]>=1:
            I[i]=1.0
        elif I[i]<=0:
            I[i]=0.0
        
            
    return I
def distance(v, u):
   return sum((v_i - u_i)**2 for v_i, u_i in zip(v, u))**0.5

def stop(x,y):
    k=[i for i, j in zip(x, y) if i == j]
    if len(k)== 4:
        return 1
    else:
        return 0
    
def rand(pattern_width ):
    
    x=[]
    for i in range (pattern_width):
        x.append(i)
    y=[]
    np.random.shuffle(x)
    y = y + x
    return y



def testing(A,W,B,T):   
    for _ in range(100):
        for i in range(len(A)):#               
            a= np.dot(W[i], A) + B[i]            
            A[i] = 1.0 if a >= 1.0 else 0.0 if a <0.0 else round(a,2)

    if distance(A,T)==0:
        return A,'OK'
    else:
        return A,'NO'
  
    

# Initialize the patterns
#X = np.zeros((nb_patterns, pattern_width * pattern_height))

X =[0.80,0.70,0.60,0.55,0.55,0.55,0.50,0.5,0.50,0.45,0.45,0.40,0.30]

       
W= np.array([
[0.00,0.22,0.0,0.0,0.0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[-0.1,0.00,0.22,0.22,0.22,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.0,-0.1,0.00,0.22,0.22,0.22,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,-0.1,0.22,0.00,0.00,0.00,0.22,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,-0.1,0.22,0.00,0.00,0.00,0.00,0.22,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,-0.1,0.00,0.00,0.00,0.22,0.22,0.22,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,-0.1,0.00,0.22,0.00,0.00,0.00,0.22,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,-0.1,0.22,0.00,0.00,0.00,0.00,0.22,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,-0.1,0.00,0.00,0.00,0.22,0.22,0.22,0.0],
[0.00,0.00,0.00,0.00,0.00,0.00,-0.1,0.00,0.22,0.00,0.22,0.00,0.0],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,-0.1,0.22,0.00,0.00,0.22,0.0],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,-0.1,-0.1,-0.1,0.00,0.22],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.0,0.00,0.00,-0.1,0.00]

])

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
        
print('original w',W)        

import copy
import random

B =np.zeros((pattern_width))
# B=[0.186, 0.171, 0.075, 0.091, 0.149, 0.204, 0.219, 0.273, 0.325, 0.324, 0.37 , 0.358, 0.295]
B=[0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
print(W,'W',B)
n=0
zz=0
learning_rate=0.1


with open('Test10e.txt') as f:
    lines = f.readlines();
    while zz<=10:
        zz+=1
        print(zz, W,'W',B)
#        for line in lines:
        for _ in range (100):
            line = random.choice(lines)
            print(line)
            line = line.strip()
            line = line.split(",")
    #            line = [c for c in line]
            i = list(line)        
    
            inputs =list(map(float, i))
            
            A = copy.copy(inputs)    
            k=0
            while True:
                step=0
                k+=1
    
                for _ in range(100):
                    for i in range(len(A)):#               
                        a= np.dot(W[i], A) + B[i]            
                        A[i] = 1.0 if a >= 1.0 else 0.0 if a <0.0 else round(a,2)
                    # print (A)
                print(distance(A,X),A)            
                if distance(A,X)==0 :

                    break

                else:

                    per1=0
                    per2=2
                    # perturbation(per1,per2)

                    # pertBias(per1,per2)
                    for i in range(pattern_width):
                        e = X[i]-A[i] if len (X)>0 else 1.0
                        B[i] = round(B[i]+e*learning_rate,3)                        
                        for j in range(0,pattern_width):                                
                            
                            w0 = round(W[i, j]+( e*learning_rate),2)
                            
                            # print (w0)
                            if  W[i, j]*w0 > 0:#i!=j and
                                W[i, j] = w0
                            # if  W[j, i]*w1 > 0:#i!=j and
                            #     W[j, i] = w1
       
                
                n += 1
                
print('\n',A,W,B)   
np.set_printoptions(threshold=np.inf)
fb=open('testhnn.txt','w+')  

fb.write('Weights: \n'+repr(W)+'\n\n') 
fb.write('Bias: \n'+repr(B)+'\n\n') 

with open('Test10e.txt') as f:
    lines = f.readlines();
    for line in lines:
        line = line.strip()
        line = line.split(",")
        i = list(line)        
        inputs =list(map(float, i))    
        C = copy.copy(inputs)  
        print('\nTest:', testing(C,W,B,X))  
        kq1,kq2=testing(C,W,B,X)

        fb.write(repr(kq1))
        fb.write(repr(kq2))
        fb.write('\n')
           

fb.close()

