"""
@author: Thai Tran 15/03/2020
"""
# Normal system: Changing volatge value of 1 d-cell and restore the value using HNN
import matplotlib.pyplot as plt       
from loaddata import data,datasc       
from loaddata0 import data as dt,datasc as dtsc

from Grow import Grow
import HNN
class Main:
        
    def grow(self,d0):

       #New worm
       Worm = Grow()
       worm=Worm.Worm(d0) 
       
       fig1 = plt.figure(figsize=(8, 6))
       ax1 = fig1.add_subplot(221, aspect='equal')
       ax2 = fig1.add_subplot(222, aspect='equal')
       ax3 = fig1.add_subplot(223, aspect='equal')
       ax4 = fig1.add_subplot(224, aspect='equal')
# =============================================================================
# Update Initial parameters
       worm.updateUD(d0)       
       worm.UpdateSC(d0) 
       worm.UpdateGroup(d0)          
       worm.UpdateSCNet(d0)           
       big=HNN.HNN(worm.GetBigSC(d0))
       worm.UpdateVolG(big,d0)   
# =============================================================================
#Load data and draw normal worm Fig 1 
       worm.case11()
       
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)       
       ax1.scatter(x, y,marker='o',s=10,c=z)     
       ax1.set_title('A. One cell damage')
       ax1.set_xlim(-1,106)
       ax1.set_ylim(0,50)       
       bigsc=worm.GetBigSC(d0)
       ax1.axes.xaxis.set_visible(False)
       ax1.axes.yaxis.set_visible(False)
       print ('Normal bioelectricity:')
       print (bigsc)
# ============================================================================= 
# Make damage: kill 1 d-cell
       sc,_=worm.Case2(1,None)      
       print(sc.data,sc.group)
# =============================================================================       
#draw damage worm Fig 2
       Tissue=worm.extractgroup(d0,sc.group)
       x,y,z=dt(Tissue)       
       ax2.scatter(x, y,marker='o',s=100,c=z)     
       ax2.set_title('B. Identify damage')
       ax2.set_xlim(60,85)
       ax2.set_ylim(15,31)
       ax2.axes.xaxis.set_visible(False)
       ax2.axes.yaxis.set_visible(False)
# =============================================================================       
# Repair
       worm.SCRepair(sc)
# =============================================================================       
#draw recover worm Fig 3
       Tissue=worm.extractgroup(d0,sc.group)
       x,y,z=dt(Tissue)       
       ax3.scatter(x, y,marker='o',s=100,c=z)     
       ax3.set_title('C. Regenerated missing cell')
       ax3.set_xlim(60,85)
       ax3.set_ylim(15,31)
       ax3.axes.xaxis.set_visible(False)
       ax3.axes.yaxis.set_visible(False)
# =============================================================================       
       big=worm.GetBigSC(d0)
       print ('Current bioelectricity:',big)        
       big=HNN.HNN(bigsc)        
       worm.UpdateVolG(big,d0)
       big=worm.GetBigSC(d0)       
       print ('Recovered bioelectricity:',big)        
# =============================================================================       
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)
       ax4.scatter(x, y,marker='o',s=10,c=z)     
       ax4.set_title('D. Recovered bioelectricity')
       ax4.set_xlim(-1,106)
       ax4.set_ylim(0,50)
       ax4.axes.xaxis.set_visible(False)
       ax4.axes.yaxis.set_visible(False)
#=============================================================================       
       plt.tight_layout()
       plt.savefig("case2.jpg", dpi=1200)
       plt.show()
#=============================================================================       
# =============================================================================             

       
       
s=Main()
s.grow(23)
        
