import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
def newtissue():
    
    tissue=[]    
    k=0
    y=0.0  
    d=0
    x = np.arange(0.5,8.5, 0.5)
#    print x
    for r in x:
        d=int(r*2*np.pi/0.52)
        x1 = np.arange(0, 2*np.pi, 2*np.pi/d)
#        print 'x1',x1,'d',d,'r',r
        for i in x1:    
           y= i - np.pi/d
           tissue.append([]) 
           tissue[k].append(r)
           tissue[k].append(y)
           tissue[k].append(1)
           k=k+1
        
    return tissue

t=newtissue()
print t
beta = [1,2,3,4,5]
theta = [4.148513375894214,4.148513375894214,4.148513375894214,4.148513375894214,4.148513375894214]

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

line, = ax.plot([],[])


def update(b):
    
    line.set_xdata(b)
    line.set_ydata(theta)
    return line,

ani = FuncAnimation(fig, update, beta, blit=True)
plt.show()