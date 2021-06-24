"""
@author: Thai Tran 15/03/2020
"""
# Normal system: Changing volatge value of 1 d-cell and restore the value using HNN
class Main:
        
    def grow(self,d0):
       import matplotlib.pyplot as plt       
       from loaddata import data,datasc       
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
       worm.updateUD(d0)
       worm.UpdateSC(d0) 
       worm.UpdateGroup(d0)
       # worm.UpdateVol(d0)   
       worm.UpdateSCNet(d0)   
       bigsc=worm.GetBigSC(d0)
       big=HNN.HNN(bigsc)
       worm.UpdateVolG(big,d0)
# =============================================================================
#draw normal worm Fig 1 
#Load data and entropy
       Tissue=worm.extractdata(d0)

       x,y,z=data(Tissue)       
       ax1.scatter(x, y,marker='s',s=10,c=z)     
       ax1.set_title('Normal worm')
       ax1.set_xlim(-1,106)
       ax1.set_ylim(0,50)
# ============================================================================= 
# Make damage: kill 1 d-cell
       worm.Case6(d0)

       
       # resc=worm.SendMsgSC(node)
       # print ('Damage cell: ', node.data)
       # print ('Stem cell closes the damage',resc.data)
 # =============================================================================       
#draw damage worm Fig 2
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax2.scatter(x, y,marker='s',s=100,c=z)     
       ax2.set_title('Group of cells damage')
       ax2.set_xlim(-1,106)
       ax2.set_ylim(0,50)

 # =============================================================================       
# Repair
       # worm.Repairc4(d0)
       
       # worm.RepairCase3(sc2)
       # worm.RepairCase3(sc3)
       # worm.RepairCase3(sc4)
       # # print (sc.data)
# =============================================================================       
#draw recover worm Fig 3
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax3.scatter(x, y,marker='s',s=100,c=z)     
       ax3.set_title('Regeneration missing cells')
       ax3.set_xlim(-1,106)
       ax3.set_ylim(0,50)

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
       x,y,z=data(Tissue)
       ax4.scatter(x, y,marker='s',s=10,c=z)     
       ax4.set_title('Restoration bioelectricity')
       ax4.set_xlim(-1,106)
       ax4.set_ylim(0,50)
#=============================================================================       

#=============================================================================       
# =============================================================================             

s=Main()
s.grow(23)
        
