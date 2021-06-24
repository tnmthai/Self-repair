"""
@author: Thai Tran 15/03/2020
"""
# Normal system: Changing volatge value of 1 d-cell and restore the value using HNN
class Main:

    def grow(self,d0):
       import matplotlib.pyplot as plt
       from loaddata import data
       from loaddata0 import data as dt
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
       worm.Case50()
       Tissue=worm.extractdata(d0)

       x,y,z=data(Tissue)
       ax1.scatter(x, y,marker='o',s=10,c=z)
       ax1.set_title('A. An AMN node missing')
       ax1.set_xlim(-5,110)
       ax1.set_ylim(0,50)
       ax1.axes.xaxis.set_visible(False)
       ax1.axes.yaxis.set_visible(False)
# =============================================================================
# Make damage: kill 1 d-cell
       worm.updateUD(d0)
       worm.UpdateSC(d0)
       worm.UpdateGroup(d0)
       # worm.UpdateVol(d0)
       worm.UpdateSCNet(d0)
       bigsc=worm.GetBigSC(d0)
       big=HNN.HNN(bigsc)
       worm.UpdateVolG(big,d0)
       
       worm.Case5()


 # =============================================================================
#draw damage worm Fig 2
       Tissue=worm.extractbody()
       x,y,z=dt(Tissue)
       ax2.scatter(x, y,marker='o',s=40,c=z)
       ax2.set_title('B. Identify damage')
       ax2.set_xlim(35,70)
       ax2.set_ylim(10,37)
       ax2.axes.xaxis.set_visible(False)
       ax2.axes.yaxis.set_visible(False)
 # =============================================================================
# Repair
       worm.Repairc4(d0)


# =============================================================================
#draw recover worm Fig 3
       Tissue=worm.extractbody()
       x,y,z=dt(Tissue)
       ax3.scatter(x, y,marker='o',s=40,c=z)
       ax3.set_title('C. Regenerated missing cells')
       ax3.set_xlim(35,70)
       ax3.set_ylim(10,37)
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
       x,y,z=data(Tissue)
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

