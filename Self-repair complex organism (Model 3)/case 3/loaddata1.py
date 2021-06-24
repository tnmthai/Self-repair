"""
@author: Thai Tran
"""    

def RGB(value,sc,ss):
    if sc=='s' and value==0.9:
        z=(185/255,0/255,0/255)  
    elif sc=='s' and value!=0.9:
        z=(1,0/255,0/255)
    elif value==0:
        z=(0,0,0)
    elif value==0.05:
        z=(114/255,153/255,23/255)
        
    elif value ==0.1:
        z=(255/255,255/255,0/255)   
    elif value <= 0.3:
        z=(45/255,70/255,150/255)   
    elif value <= 0.4:
        z=(30/255,143/255,140/255)
    elif value <= 0.45:
        z=(16/255,169/255,75/255)       
    elif value <= 0.5:
        z=(62/255,182/255,60/255)    
    elif value <= 0.55:
        z=(153/255,207/255,32/255)
    elif value <= 0.6:
        z=(203/255,221/255,17/255)    
    elif value <= 0.7:
        z=(240/255,195/255,10/255)
    elif value <= 0.8:
        z=(163/255,0/255,0/255)    
    else:
        z=(100/255,0/255,0/255)        
    # if ss==-1:
        # z=(0,0,0)        
        # print (ss)    
    return z
def distance(v, u):
   return sum((v_i - u_i)**2 for v_i, u_i in zip(v, u))**0.5
def data(tissue):
    x=[]
    y=[]
    z=[]
    
    for t in tissue:           
        x.append(t[0][0])
        y.append(t[0][1])
        z.append(RGB(t[1],t[2],t[3]))      
    
    return x,y,z

def datasc(tissue):
    sc=[]      
       
    for t in tissue:  
        if t[2]=='s':
            sc.append(t[0])
                       
    
    return sc