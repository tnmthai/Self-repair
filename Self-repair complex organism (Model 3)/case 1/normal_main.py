"""
@author: Thai Tran 15/03/2020
"""
import matplotlib.pyplot as plt
from loaddata import data
from Grow import Grow
import HNN

# Normal system: Changing volatge value of 1 d-cell and many cells and restore the value using HNN
class Main:

    def grow(self,d0):
       #New worm
       Worm = Grow()
       worm=Worm.Worm(d0)

       fig = plt.figure(figsize=(10, 6))
       # fig.tight_layout()
# 4 figures
       ax1 = fig.add_subplot(111, aspect='equal')
       

       # ax2 = fig.add_subplot(222, aspect='equal')
       # ax3 = fig.add_subplot(223, aspect='equal')
       # ax4 = fig.add_subplot(224, aspect='equal')
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
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)
       im=ax1.scatter(x, y,marker='8',s=15,c=z)#,cmap='viridis'
       # ax1.set_title(' Normal worm')
       ax1.set_xlim(-5,110)
       ax1.set_ylim(0,50)
       ax1.axes.xaxis.set_visible(False)
       ax1.axes.yaxis.set_visible(False)
       
       cbar=fig.colorbar(im, ax=ax1)
       im.set_clim(-25, -60)
       cbar.set_label('mV', rotation=270)
       plt.savefig("normalworm.jpg", dpi=1200)
# =============================================================================
       plt.tight_layout()
       plt.show()
# =============================================================================
#Run
s=Main()
s.grow(23)
