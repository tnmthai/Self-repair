import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Acc_11 = [1,2,3,4,6,7]
Acc_12 = [2,2,2,2,2,2]

# Scatter plot
fig = plt.figure(figsize = (5,5))


def ani(coords):
     return plt.scatter([coords[0]],[coords[1]], color='g')

def frames():
    for acc_11_pos, acc_12_pos in zip(Acc_11, Acc_12):
        yield acc_11_pos, acc_12_pos

ani = FuncAnimation(fig, ani, frames=frames, interval=1000)

plt.show()