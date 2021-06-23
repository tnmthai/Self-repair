# -*- coding: utf-8 -*-
"""
@author: Thai Tran
"""
import numpy as np

def entropy(tissue,angle):
        s0=si=0.0  
        k=0                
        a=np.pi/180
        for d in tissue:            
            if d[2] != 0 and round(d[1],7) < round(angle*a,7) and round(d[1],7)>= round((angle - 15)*a,7):
                s0 = s0 + d[0]
        for d in tissue:
            if d[2] != 0 and round(d[1],7) < round(angle*a,7) and round(d[1],7)>= round((angle - 15)*a,7):
                k=k+1
                si = si + (d[0]/s0) * np.log(d[0]/s0)    

        return (-si/np.log(k)),k
