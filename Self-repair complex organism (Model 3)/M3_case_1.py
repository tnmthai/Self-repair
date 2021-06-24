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
       fig.tight_layout()
# 4 figures
       ax1 = fig.add_subplot(221, aspect='equal')
       ax2 = fig.add_subplot(222, aspect='equal')
       ax3 = fig.add_subplot(223, aspect='equal')
       ax4 = fig.add_subplot(224, aspect='equal')
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
       ax1.scatter(x, y,marker='s',s=10,c=z)
       ax1.set_title('Normal bioelectricity')
       ax1.set_xlim(-1,106)
       ax1.set_ylim(0,50)
       bigsc=worm.GetBigSC(d0)

       print ('Normal bioelectricity:')
       print (bigsc)
# =============================================================================
# Change value 1 d-cell
       worm.Case1a(0)
       bigsc=worm.GetBigSC(d0)
       print ('1 bioelectricity:')
       print (bigsc)

# =============================================================================
#Load data and draw normal worm Fig 2
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)
       ax2.scatter(x, y,marker='s',s=10,c=z)
       ax2.set_title('Perturbation a single cell')
       ax2.set_xlim(-1,106)
       ax2.set_ylim(0,50)
# =============================================================================
# Change value all cells
       worm.Case1b(d0,0)
# =============================================================================
#Load data and draw normal worm Fig 3
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)
       ax3.scatter(x, y,marker='s',s=10,c=z)
       ax3.set_title('Perturbation all cells')
       ax3.set_xlim(-1,106)
       ax3.set_ylim(0,50)

# =============================================================================
# Call HNN to restore bioelectricity
       bigsc=worm.GetBigSC(d0)
       print ('Many cells changes bioelectricity:')
       print (bigsc)
       big=HNN.HNN(bigsc)
       print ('Recovered bioelectricity:')
       print (big)
       worm.UpdateVolG(big,d0)

# =============================================================================
#Load data and draw normal worm Fig 14
       Tissue=worm.extractdata(d0)
       x,y,z=data(Tissue)
       ax4.scatter(x, y,marker='s',s=10,c=z)
       ax4.set_title('Recovered bioelectricity')
       ax4.set_xlim(-1,106)
       ax4.set_ylim(0,50)

# =============================================================================
#Run
s=Main()
s.grow(23)