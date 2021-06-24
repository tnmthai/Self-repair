# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:14:43 2019

@author: tnmt
"""

import matplotlib.pyplot as plt

ax1 = plt.subplot(131)
ax1.scatter([1, 2], [3, 4])
ax1.set_xlim([0, 5])
ax1.set_ylim([0, 5])


ax2 = plt.subplot(132)
ax2.scatter([1, 2],[3, 4])
ax2.set_xlim([0, 5])
ax2.set_ylim([0, 5])