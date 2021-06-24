"""
@author: Thai Tran 15/03/2020
"""
# Normal system: Changing volatge value of 1 d-cell and restore the value using HNN
class Main:
        
    def grow(self,d0):
       import matplotlib.pyplot as plt       
       from loaddata import data,datasc       
       from loaddata0 import data as dt,datasc as dtsc
       from Grow import Grow
       import HNN
       #New worm
       Worm = Grow()
       worm=Worm.Worm(d0) 
       
       fig1 = plt.figure(figsize=(8, 6))
       ax1 = fig1.add_subplot(221, aspect='equal')
       ax2 = fig1.add_subplot(222, aspect='equal')
       ax3 = fig1.add_subplot(223, aspect='equal')
       ax4 = fig1.add_subplot(224, aspect='equal')
# =============================================================================
       worm=Worm.Worm(d0) 
       worm.updateUD(d0)
       worm.UpdateSC(d0) 
       worm.UpdateGroup(d0)       
       worm.UpdateSCNet(d0)     
       bigsc=worm.GetBigSC(d0)
       big=HNN.HNN(bigsc)
       worm.UpdateVolG(big,d0)
# =============================================================================
#draw normal worm Fig 1 
#Load data and entropy
       node=worm.Case4only(1)
       Tissue=worm.extractdata(d0)

       x,y,z=dt(Tissue)       
       ax1.scatter(x, y,marker='o',s=10,c=z)     
       ax1.set_title('A. A stem cell and surrounding tissue damage')
       ax1.set_xlim(-5,110)
       ax1.set_ylim(0,50)
       ax1.axes.xaxis.set_visible(False)
       ax1.axes.yaxis.set_visible(False)
# ============================================================================= 
# Make damage: kill 1 d-cell
       worm=Worm.Worm(d0) 
       worm.updateUD(d0)
       worm.UpdateSC(d0) 
       worm.UpdateGroup(d0)       
       worm.UpdateSCNet(d0)     
       bigsc=worm.GetBigSC(d0)
       big=HNN.HNN(bigsc)
       worm.UpdateVolG(big,d0)
       
       node=worm.Case4(1)
       
       # resc=worm.SendMsgSC(node)
       # print ('Damage cell: ', node.data)
       # print ('Stem cell closes the damage',resc.data)
 # =============================================================================       
#draw damage worm Fig 2
       Tissue=worm.extractgroup(d0,node.group)
       x,y,z=data(Tissue)       
       ax2.scatter(x, y,marker='o',s=100,c=z)     
       ax2.set_title('B. Identify damage')
       ax2.set_xlim(62,77.6)
       ax2.set_ylim(15,31)
       ax2.axes.xaxis.set_visible(False)
       ax2.axes.yaxis.set_visible(False)
 # =============================================================================       
# Repair
       worm.Repairc4(d0)
       
       # worm.RepairCase3(sc2)
       # worm.RepairCase3(sc3)
       # worm.RepairCase3(sc4)
       # # print (sc.data)
# =============================================================================       
#draw recover worm Fig 3
       Tissue=worm.extractgroup(d0,node.group)
       x,y,z=data(Tissue)       
       ax3.scatter(x, y,marker='o',s=100,c=z)     
       ax3.set_title('C. Regenerated missing cells')
       ax3.set_xlim(62,77.6)
       ax3.set_ylim(15,31)
       ax3.axes.xaxis.set_visible(False)
       ax3.axes.yaxis.set_visible(False)
# =============================================================================       
# =============================================================================        
       bigsc=worm.GetBigSC(d0)
       
       print ('Current bioelectricity:')
       print (bigsc)
       nn,big=HNN.Check(bigsc)
       if nn>=0:
           print ('Not recover due to damage')
       elif nn==-2:
           print ('System is normal')
       else:
           print ('Bioelectricity recovered')
           worm.UpdateVolG(big,d0)
           bigsc1=worm.GetBigSC(d0)
           print (bigsc1)
           
# =============================================================================       
       Tissue=worm.extractdata(d0)
       x,y,z=dt(Tissue)
       ax4.scatter(x, y,marker='o',s=10,c=z)     
       ax4.set_title('D. Recovered bioelectricity')
       ax4.set_xlim(-5,110)
       ax4.set_ylim(0,50)
       ax4.axes.xaxis.set_visible(False)
       ax4.axes.yaxis.set_visible(False)
#=============================================================================       
       plt.tight_layout()
       plt.show()
#=============================================================================       
# =============================================================================             

s=Main()
s.grow(23)
        
