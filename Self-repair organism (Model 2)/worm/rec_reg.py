"""
@author: Thai Tran
"""

class Main:
        
    def grow(self,d0):
       import matplotlib.pyplot as plt
       from entropy import entropy
       from Dlist import Node
       from Dlist import DoublyLinkedList
       from loaddata import data
       import numpy as np
       from Grow import Grow
       stemcells=[]
       #New worm
       Worm = Grow()
       Head,mid1=Worm.Head(d0) 
       Body,mid2=Worm.Body(d0)
       Tail,mid3=Worm.Tail(d0)
       
       fig1 = plt.figure()
       ax1 = fig1.add_subplot(221, aspect='equal')
       ax2 = fig1.add_subplot(222, aspect='equal')
       ax3 = fig1.add_subplot(223, aspect='equal')
       ax4 = fig1.add_subplot(224, aspect='equal')

       #stem cells list 
       stemcells.append(mid1)
       stemcells.append(mid2)
       stemcells.append(mid3)
# =============================================================================
#Load data and entropy
       Htissue=[]#Head.extractdata(d0)
       Btissue=Body.extractdata(3*d0)
       Ttissue=[]#Tail.extractdata(d0)
       
#       Ehead= entropy(Htissue,mid1)
       Ebody= entropy(Btissue,mid2)
#       Etail= entropy(Ttissue,mid3)
#       print Ehead#, Ebody, Etail
# =============================================================================       
#draw normal worm Fig 1       
       x,y=data(Htissue,Btissue,Ttissue)
       ax1.scatter(x, y)     
       ax1.set(xlabel='x', ylabel='y')
       ax1.set_title('a) Normal tissue')
       ax1.set_xlim(9,41)
       ax1.set_ylim(-1,11)
# ============================================================================= 
# Case 1: head damage a part       
#       Head.damagecase1(d0)
#       Htissue=Head.extractdata(d0)
       Btissue=Body.extractdata(2*d0)
       abnormalbody=entropy(Btissue,mid2)
#       print abnormalhead
 # =============================================================================       
#draw abnormal worm Fig 2      
       x,y=data(Htissue,Btissue,Ttissue)
       ax2.scatter(x, y)   
       ax3.scatter(x, y)   
       ax2.set_xlim(9,41)
       ax2.set_ylim(-1,11)     
       ax2.set(xlabel='x', ylabel='y')
       ax2.set_title('a) Damaged tissue')
# =============================================================================       
#Entropy: detect damage region
       p=-1
       for i in range (0,4):
           if Ebody[i]!=abnormalbody[i]:
               p=i
               print 'damage area',p

# =============================================================================       
#draw damage border

#       level,Dlist=Head.Detectcase1(d0,p)       
       x=[]
       y=[]
       x1 = np.arange(0.5,10,0.5)
#       print x1,'x1'
       for i in x1:
           x.append(29.5)
           y.append(i)
#       for t in Dlist:
#           x.append(t[0])
#           y.append(t[1])
#       print x,y
       ax3.scatter(x, y)
       ax3.set_xlim(9,41)
       ax3.set_ylim(-1,11) 
       ax3.set(xlabel='x', ylabel='y')
       ax3.set_title('c) Identify damage border')
#=============================================================================       
#repair
#       
#       minx,miny=Dlist[0]
#       maxx,maxy=Dlist[len(Dlist)-1]
#       
#       while minx >= 0:
#           for y in np.arange (miny, maxy+0.5,0.5):
#               Head.insert_at_end(Node([minx-1,y]),11-minx)
#
#           minx = minx - 1
#           miny= miny + 0.5
#           maxy = maxy -0.5
#=============================================================================       
#draw waorm after repaired Fig 4               
       Btissue=Body.extractdata(3*d0)
       x,y=data(Htissue,Btissue,Ttissue)
       ax4.scatter(x, y)     
       ax4.set_xlim(9,41)
       ax4.set_ylim(-1,11)       
       ax4.set(xlabel='x', ylabel='y')
       ax4.set_title('d) Regenerated tissue')
#=============================================================================       
#draw stem cells     
       x=[]
       y=[]
       for s in stemcells:
           x.append(s[0])
           y.append(s[1])
       ax1.scatter(x, y, c='red')
       ax2.scatter(x, y, c='red')
       ax3.scatter(x, y, c='red')
       ax4.scatter(x, y, c='red')
       
       
s=Main()
s.grow(10)
        
