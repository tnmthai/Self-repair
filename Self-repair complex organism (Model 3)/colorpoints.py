# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:46:12 2020

@author: trann5
"""
import matplotlib.pyplot as plt
import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.colors.ListedColormap([
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])
cmap.set_over('blue')
cmap.set_under('red')

bounds = [0.3,0.4,0.5,0.6,0.7,0.8]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb3 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                norm=norm,
                                boundaries=[-10] + bounds + [10],
                                extend='both',
                                extendfrac='auto',
                                ticks=bounds,
                                spacing='uniform',
                                orientation='horizontal')
cb3.set_label('Custom extension lengths, some other units')
fig.show()


















# from matplotlib import pyplot as plt

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [125, 32, 54, 253, 67, 87, 233, 56, 67]

# color = [str(item/255.) for item in y]
# print (color)
# plt.scatter(x, y, s=500, c=(0,0.66,0.35))
# plt.colorbar()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np


# def discrete_cmap(N, base_cmap=None):
#     """Create an N-bin discrete colormap from the specified input map"""

#     # Note that if base_cmap is a string or None, you can simply do
#     #    return plt.cm.get_cmap(base_cmap, N)
#     # The following works for string, None, or a colormap instance:

#     base = plt.cm.get_cmap(base_cmap)
#     color_list = base(np.linspace(0, 1, N))
#     cmap_name = base.name + str(N)
#     return base.from_list(cmap_name, color_list, N)


# if __name__ == '__main__':
#     N = 13

#     x = np.random.randn(40)
#     y = np.random.randn(40)
#     c = np.random.randint(N, size=40)

#     # Edit: don't use the default ('jet') because it makes @mwaskom mad...
#     plt.scatter(x, y, c=c, s=50, cmap=discrete_cmap(N, 'cubehelix'))
#     plt.colorbar(ticks=range(N))
#     plt.clim(-0.5, N - 0.5)
#     plt.show()
    
    
    

# import numpy as np

# x = np.random.random(20)
# y = np.random.random(20)
# z = np.random.randint(-2,3,20)
# cmap=plt.cm.rainbow
# norm = matplotlib.colors.BoundaryNorm(np.arange(-2.5,3,1), cmap.N)
# plt.scatter(x,y,c=z,cmap=cmap,norm=norm,s=100,edgecolor='none')
# plt.colorbar(ticks=np.linspace(-2,2,5))
# plt.show()