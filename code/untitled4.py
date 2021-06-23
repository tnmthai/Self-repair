import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

Acc_12 = [1,2,3,4]
Acc_11 = [0,0,0,0]

# Scatter plot
fig = plt.figure(figsize = (5,5))
axes = plt.subplot(111, polar=True)
axes.set_xlim(0, 2*np.pi)
axes.set_ylim(0, 10)

point, = axes.plot([Acc_11[0]],[Acc_12[0]], 'go')

def ani(coords):
    point.set_data([coords[0]],[coords[1]])
    return point

def frames():
    for acc_11_pos, acc_12_pos in zip(Acc_11, Acc_12):
        yield acc_11_pos, acc_12_pos

ani = FuncAnimation(fig, ani, frames=frames, interval=1000, repeat =False)

plt.show()