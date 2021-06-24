# -*- coding: utf-8 -*-
"""
@author: Thai Tran
"""

import numpy as np
import math  

def Distance(a,b):  
     x1,y1 = a
     x2,y2 = b
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     
     return dist  
   
def entropy(tissue,mid):
    
    s0=s1=s2=s3=e0=e1=e2=e3=0.0
    t0=t1=t2=t3=p=0
    E_list=[]
    #sum of distance per part
    for t in tissue:
        p = Distance(t,mid)   
        if p>0 and t[0]>mid[0] and t[1]>=mid[1]:# and t[1]<= 2*mid[1] :
            s0 = s0 + Distance(t,mid)                  
            t0 = t0 + 1
        if p>0 and t[0]<=mid[0] and t[1]>=mid[1]:# and t[1]<= 2*mid[1] :
            s1 = s1 + Distance(t,mid)      
            t1 = t1 + 1
                        
        if p>0 and t[0]<=mid[0] and t[1]< mid[1] :#and t[1]>=0
            s2 = s2 + Distance(t,mid)      
            t2 = t2 + 1
        
        if p>0 and t[0]>mid[0]  and t[1]< mid[1] :#and t[1]>=0
            s3 = s3 + Distance(t,mid)      
            t3 = t3 + 1
    print t0,t1,t2,t3
    print s0,s1,s2,s3    

    #entropy per part
    for t in tissue:   
        p= Distance(t,mid)
        
        if p>0 and t[0]>mid[0] and t[1]>=mid[1] and s0>0:            
            e0 = e0 + p/s0 * np.log(p/s0)      
                    
        if p>0 and t[0]<=mid[0] and t[1]>=mid[1] and s1>0:
            e1 = e1 + p/s1 * np.log(p/s1)      
                    
        if p>0 and t[0]<=mid[0] and t[1]< mid[1] and s2>0:
            e2 = e2 + p/s2 * np.log(p/s2)      
                
        if p>0 and t[0]>mid[0]  and t[1]< mid[1] and s3>0:
            e3 = e3 + p/s3 * np.log(p/s3)      
                    
    E_list.append(-e3/np.log(t3))        
    E_list.append(-e0/np.log(t0))
    E_list.append(-e1/np.log(t1))
    E_list.append(-e2/np.log(t2))
    
#    print E_list
    
    return E_list

        
#tissue=[[0,0],[-0.5, 0],[0.5, 0],[-0.5, 1],[0.0, 1],[0.5, 1],[-1.0, 0],[1.0, 0],[-1.0, 1],[1.0, 1],[-1.0, 2],[-0.5, 2],[0.0, 2],[0.5, 2],[1.0, 2]]        
#print entropy(tissue)