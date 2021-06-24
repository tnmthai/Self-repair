# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:58:22 2020

@author: trann5
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.random.random(50)
y = np.random.random(50)
c = np.random.random(50)  # color of points
s = 500 * np.random.random(50)  # size of points

fig, ax = plt.subplots()
im = ax.scatter(x, y, c=c, s=s, cmap=plt.cm.jet)

# Add a colorbar
cbar=fig.colorbar(im, ax=ax)

# set the color limits - not necessary here, but good to know how.
im.set_clim(-25, -60)
cbar.set_label('mV', rotation=270)
plt.savefig("gradient.jpg", dpi=1200)