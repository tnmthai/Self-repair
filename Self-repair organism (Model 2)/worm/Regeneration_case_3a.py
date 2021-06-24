"""
@author: Thai Tran
"""    
    
class Main:
        
    def grow(self,d0):
       
       from entropy import entropy
       from Dlist import Node
       from Dlist import DoublyLinkedList
       from loaddata import data
       from Algorithms import automata
       from Algorithms import NN
       from Algorithms import DT
       from Grow2 import Grow
       import numpy as np
       import matplotlib.pyplot as plt
       stemcells=[]

       #create figures
       fig1 = plt.figure()
       ax1 = fig1.add_subplot(221, aspect='equal')
       ax2 = fig1.add_subplot(222, aspect='equal')
       ax3 = fig1.add_subplot(223, aspect='equal')
       ax4 = fig1.add_subplot(224, aspect='equal')
       #New worm
       Worm = Grow()
       Head,mid1=Worm.Head(d0,[10,5.0]) 
       Body,mid2=Worm.Body(4,[10,5.0])
       Tail,mid3=Worm.Tail(d0,[40,5.0])

       #stem cells list 
       stemcells.append(mid1)
       stemcells.append(mid2)
       stemcells.append(mid3)
       
# =============================================================================
#Load data 
       Htissue=[] #Head.extractdata(d0)
       mid1=[-1,-1]
       stemcells[0]=mid1
       Btissue=Body.extractdata(3)             
       Ttissue=[]
       mid3=[-1,-1]
       stemcells[2]=mid3
# =============================================================================       
#draw normal worm Fig 1       
       x,y=data(Htissue,Btissue,Ttissue)
       ax1.scatter(x, y)     
       ax1.set_xlim(-1,51)
       ax1.set_ylim(-1,11)
# =============================================================================       
#draw stem cells     
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       ax1.scatter(x, y, c='red')
       ax1.set_title('A. Identification of stem cell polarities')
# =============================================================================       
#Detect damage: 3 approaches
       M1=automata()
       r1=M1.Switch(M1.body(mid1,mid2,mid3),1)
       r2=M1.Switch(M1.tail(mid1,mid2,mid3),2)
       r3=M1.Switch(M1.tail(mid1,mid2,mid3),3)
       print r1,r2,r3

#=============================================================================       
#repair
       startb=[10,5.0]
       
       Body,mid2=Worm.Body(3,startb)
       stemcells[1]=mid2
       startb[0]=startb[0]+3*3
       Tail,mid3=Worm.Tail(3,startb)
       stemcells[2]=mid3
       print mid3,'mid3'
       Btissue=Body.extractdata(3*3)
       Ttissue=Tail.extractdata(3)
       
       x,y=data(Htissue,Btissue,Ttissue)
       ax2.scatter(x, y)     
       ax2.set_xlim(-1,51)
       ax2.set_ylim(-1,11) 
#draw stem cells     
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       ax2.scatter(x, y, c='red')
       ax2.set_title('B. Regenerating worm - 1')
       
#=============================================================================       
#=============================================================================       
#repair
       startb=[10,5.0]
       
       Body,mid2=Worm.Body(5,startb)
       stemcells[1]=mid2
       startb[0]=startb[0]+3*5
       Tail,mid3=Worm.Tail(3,startb)
       stemcells[2]=mid3
       print mid3,'mid3'
       Btissue=Body.extractdata(3*5)
       Ttissue=Tail.extractdata(5)
       
       x,y=data(Htissue,Btissue,Ttissue)
       ax3.scatter(x, y)     
       ax3.set_xlim(-1,51)
       ax3.set_ylim(-1,11) 
#draw stem cells     
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       ax3.scatter(x, y, c='red')
       ax3.set_title('B. Regenerating worm - 2')
       

# =============================================================================       
#repair
       startb=[10,5.0]
       
       Body,mid2=Worm.Body(d0,startb)
       stemcells[1]=mid2
       startb[0]=startb[0]+3*d0
       Tail,mid3=Worm.Tail(d0,startb)
       stemcells[2]=mid3
       print mid3,'mid3'
       Btissue=Body.extractdata(3*d0)
       Ttissue=Tail.extractdata(d0)
       
       x,y=data(Htissue,Btissue,Ttissue)
       ax4.scatter(x, y)     
       ax4.set_xlim(-1,51)
       ax4.set_ylim(-1,11) 
#draw stem cells     
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       ax4.scatter(x, y, c='red')
       ax4.set_title('B. Regenerated worm')
       
s=Main()
s.grow(11)
        
