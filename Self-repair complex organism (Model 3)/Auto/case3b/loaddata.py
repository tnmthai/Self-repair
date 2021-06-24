"""
@author: Thai Tran
"""    

def data(Htissue,Btissue,Ttissue):
       x=[]
       y=[]
       for t in Htissue:
           x.append(t[0])
           y.append(t[1])
       for t in Btissue:
           x.append(t[0])
           y.append(t[1])
       for t in Ttissue:
           x.append(t[0])
           y.append(t[1])
       return x,y