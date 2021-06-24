"""
@author: Thai Tran
"""   
def Distance(a,b): 
    import math  
    x1,y1 = a
    x2,y2 = b
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist 
     
class automata: 
    def Switch(self,arg,p):
        if p==1:
            switcher = {
                0: "Both",
                1: "Tail",
                2: "Body",
                3: "Normal"
            }
#        return switcher.get(arg, "nothing")
        if p==2:
            switcher = {
                0: "Both",
                1: "Tail",
                2: "Head",
                3: "Normal"
            }
#        return switcher.get(arg, "nothing")
        if p==3:
            switcher = {
                0: "Both",
                1: "Head",
                2: "Body",
                3: "Normal"
            }
        return switcher.get(arg, "nothing")
     
    def head(self,hsc,bsc,tsc):
        result=0
        if Distance(hsc,bsc) < 25 and Distance(hsc,bsc) > 10:
            result += 1
        if Distance(hsc,tsc) > 25 and Distance(hsc,tsc) < 42:
            result += 2

        return result
    
    def body(self,hsc,bsc,tsc):
        result=0
        if Distance(hsc,bsc) < 25 and Distance(hsc,bsc) > 10:
            result += 1
        if Distance(tsc,bsc) < 25 and Distance(tsc,bsc) > 10:
            result += 2
        
        return result 
       
    def tail(self,hsc,bsc,tsc):
        result=0
        if Distance(tsc,bsc) < 25 and Distance(tsc,bsc) > 10:
            result += 1
        if Distance(tsc,hsc) > 25 and Distance(tsc,hsc) <42:
            result += 2
        
        return result       
    
class NN:
    def head(self,bsc,tsc):
        y=0
        if bsc !=[-1,-1]:
            y += 1*2
        if tsc !=[-1,-1]:
            y += 1*3
        return y
    
    def body(self,hsc,tsc):
        y=0
        if hsc !=[-1,-1]:
            y += 1*1
        if tsc !=[-1,-1]:
            y += 1*3
        return y
    def tail(self,hsc,bsc):
        y=0
        if bsc !=[-1,-1]:
            y += 1*2
        if hsc !=[-1,-1]:
            y += 1*1
        return y

class DT:
    def Decisiontree(self,j,k):
        y=-1
        if j<= 0:
            if k <=1:
                if k <=0:
                    y=0
                else:
                    y=1
            elif k <=2:
                y=2
            else:
                y=3
        elif k <=0:
            if j <=1:
                y=4
            elif j <=2:
                y=5
            else:
                y=6
        else:
            y=7
        
        return y

    
    
    
#    
#a=automata()
#a2=NN()
#a3=DT()
#h=[-1,-1]
#b=[25,5]
#t=[45,5]
#print Distance(h,b)
#kq=a.head(h,b,t)    
#print a.head(h,b,t) ,a.body(h,b,t) , a.tail(h,b,t) ,a.Switch(a.head(h,b,t),1)
#print a2.head(b,t) , a2.body(h,t),a2.tail(h,b)
#print a3.Decisiontree(0,0)