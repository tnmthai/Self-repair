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
       
       fig1 = plt.figure(figsize=(10, 8))
       ax1 = fig1.add_subplot(321, aspect='equal')
       ax2 = fig1.add_subplot(322, aspect='equal')
       ax3 = fig1.add_subplot(323, aspect='equal')
       ax4 = fig1.add_subplot(324, aspect='equal')
       ax5 = fig1.add_subplot(325, aspect='equal')
       ax6 = fig1.add_subplot(326, aspect='equal')
       
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
# ============================================================================= 
# Make damage: kill 
       worm.Case6(d0)    
       worm.Case5()
 # =============================================================================       
#draw damage worm Fig 1
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax1.scatter(x, y,marker='s',s=10,c=z)     
       ax1.set_title('A. Head, tail and interior damage')
       ax1.set_xlim(-5,110)
       ax1.set_ylim(0,50)
       ax1.axes.xaxis.set_visible(False)
       ax1.axes.yaxis.set_visible(False)
       # print (worm.SCdata(d0))
 # =============================================================================       
# Repair
       # worm.Repairc4(d0)
       damage, results, mid_head,mid_tail=worm.identifyPart(d0)
       # print (damage, results, mid_head,mid_tail)
       worm.repair_head(damage,d0-15)
       worm.repair_tail(damage,d0-15)
       worm.Repairc7(45)
# =============================================================================       
#draw recover worm Fig 2
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax2.scatter(x, y,marker='s',s=10,c=z)     
       ax2.set_title('B. Regenerating 1')
       ax2.set_xlim(-5,110)
       ax2.set_ylim(0,50)
       ax2.axes.xaxis.set_visible(False)
       ax2.axes.yaxis.set_visible(False)
       

# =============================================================================       
#draw recover worm Fig 3
       worm.repair_head(damage,d0-10)
       worm.repair_tail(damage,d0-10)
       worm.Repairc7(50)
       
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax3.scatter(x, y,marker='s',s=10,c=z)     
       ax3.set_title('C. Regenerating 2')
       ax3.set_xlim(-5,110)
       ax3.set_ylim(0,50)
       ax3.axes.xaxis.set_visible(False)
       ax3.axes.yaxis.set_visible(False)
       
# =============================================================================       
#draw recover worm Fig 3
       worm.repair_head(damage,d0-5)
       worm.repair_tail(damage,d0-5)
       worm.Repairc7(55)
       
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax4.scatter(x, y,marker='s',s=10,c=z)     
       ax4.set_title('D. Regenerating 3')
       ax4.set_xlim(-5,110)
       ax4.set_ylim(0,50)
       ax4.axes.xaxis.set_visible(False)
       ax4.axes.yaxis.set_visible(False)
# =============================================================================       
# Repair
       # worm.Repairc4(d0)
       # damage, results, mid_head,mid_tail=worm.identifyPart(d0)
       worm.repair_headz(damage,d0-1)
       worm.repair_tail(damage,d0)
       worm.Repairc7(80)
# =============================================================================       
#draw recover worm Fig 3
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax5.scatter(x, y,marker='s',s=10,c=z)     
       ax5.set_title('E. Regenerating 4')
       ax5.set_xlim(-5,110)
       ax5.set_ylim(0,50)
       ax5.axes.xaxis.set_visible(False)
       ax5.axes.yaxis.set_visible(False)
# =============================================================================        
       bigsc=worm.GetBigSC(d0)      
       print ('Current electricity: ',bigsc)
       nn,big=HNN.Check(bigsc)
       worm.UpdateVolG(big,d0)
       bigsc1=worm.GetBigSC(d0)
       print ('Restored electricity: ',bigsc1)
   
# =============================================================================       
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)
       ax6.scatter(x, y,marker='s',s=10,c=z)     
       ax6.set_title('F. Recovered bioelectricity')
       ax6.set_xlim(-5,110)
       ax6.set_ylim(0,50)
       ax6.axes.xaxis.set_visible(False)
       ax6.axes.yaxis.set_visible(False)
#=============================================================================       
       plt.tight_layout()
       plt.show()
#=============================================================================       
# =============================================================================             

s=Main()
s.grow(23)
        
