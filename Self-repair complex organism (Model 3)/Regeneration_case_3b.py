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
       from Grow import Grow
       import numpy as np
       import matplotlib.pyplot as plt
    

       #create figures
       fig1 = plt.figure()
       ax1 = fig1.add_subplot(221, aspect='equal')
       ax2 = fig1.add_subplot(222, aspect='equal')
       ax3 = fig1.add_subplot(223, aspect='equal')
       ax4 = fig1.add_subplot(224, aspect='equal')
       #New worm
       Worm = Grow()
       Head,mid1=Worm.Head(d0) 
       Body,mid2=Worm.Body(d0)
       Tail,mid3=Worm.Tail(d0)
#stem cells list 
       stemcells=[]
       stemcells.append(mid1)
       stemcells.append(mid2)
       stemcells.append(mid3)
# =============================================================================
#Load data 
       Htissue=Head.extractdata(d0)
       Btissue=Body.extractdata(3*d0)
       Ttissue=Tail.extractdata(d0)
       
# =============================================================================       
##draw normal worm Fig 1       
       x,y=data(Htissue,Btissue,Ttissue)
#       ax1.scatter(x, y)    
#       
#       print  'Total cells: ',(len(x))
#
#       x=[]
#       y=[]
#       for s in stemcells:
#           if s[0]!=-1 and s[1]!=-1:
#               x.append(s[0])
#               y.append(s[1])
#       ax1.scatter(x, y)
#       ax1.set_xlim(-3,54)
#       ax1.set_ylim(-1,11)
#       ax1.set(xlabel='x', ylabel='y')
#       ax1.set_title('Normal worm')
# =============================================================================
#   Make damage
       
       Body.damagecase3b(3*d0)
       stemcells[1]=[-1,-1]
       Btissue=Body.extractdata(3*d0)
# =============================================================================
#draw damage worm Fig 1       
       x,y=data(Htissue,Btissue,Ttissue)
       ax1.scatter(x, y)  
       ax3.scatter(x, y)
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       
       ax1.scatter(x, y, c='red')
       ax1.set(xlabel='x', ylabel='y')
       ax1.set_title('a) Damaged worm')
       ax1.set_xlim(-3,54)
       ax1.set_ylim(-1,11)
# =============================================================================
#draw damage worm Fig 2       
       x,y=data(Htissue,Btissue,Ttissue)
       ax2.scatter(x, y)  
       stemcells[1]=[19,5]
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       ax2.scatter(x, y, c='red')
       ax2.set(xlabel='x', ylabel='y')
       ax2.set_title('b) Produce a new stem cell')
       ax2.set_xlim(-3,54)
       ax2.set_ylim(-1,11)       
# =============================================================================
#Detect damage       
       Body.updateUD(3*d0)
       Dlist = Body.detect3b(3*d0)
       print 'After damage, total cells: ',len(Dlist )
       x=[]
       y=[]
       for s in Dlist:           
           x.append(s[0])
           y.append(s[1])
       ax3.scatter(x, y)
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       ax3.scatter(x, y, c='red')
       ax3.set(xlabel='x', ylabel='y')
       ax3.set_title('c) Identify damage border')
       ax3.set_xlim(-3,54)
       ax3.set_ylim(-1,11)
#repair
       for d in Dlist:
           
           idx,lv = Body.search(d,3*d0)
           
           d1=d[1]+0.5           
           i=1
           while i<10:
               ref,dat = Body.get_node(idx+1,lv)
                                 
               if dat[1] != d1:
                   ref,_ = Body.get_node(idx,lv)
                   Body.insert_after(ref,Node([dat[0],d1]),lv)
                   d1 += 0.5
                   idx += 1
                   i +=1
#                
               else:
                   break
               
###
       Btissue=Body.extractdata(3*d0)    
       x,y=data(Htissue,Btissue,Ttissue)
       print 'After regeneration, total cells: ', len(x)
       ax4.scatter(x, y)
       stemcells[1]=[25,5]
       x=[]
       y=[]
       for s in stemcells:
           if s[0]!=-1 and s[1]!=-1:
               x.append(s[0])
               y.append(s[1])
       ax4.scatter(x, y, c='red')
       ax4.set(xlabel='x', ylabel='y')
       ax4.set_title('c) Regenerated worm')
       ax4.set_xlim(-3,54)
       ax4.set_ylim(-1,11)
       
s=Main()
s.grow(10)
        
