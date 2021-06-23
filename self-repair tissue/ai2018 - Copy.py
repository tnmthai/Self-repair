"""
@author: Thai Tran
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt
from random import randint, choice
from entropy import entropy
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
import matplotlib.animation as animation

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

def noise(tissue,r):#r: rate
#        a=0.01745 # (pi/180)

        for d in tissue:  
            rd0 = randint(0,r)*choice([-1, 1])
                
            rd2= rd0*0.01
            rd1= 0 #rd0*0.01 

            d[0] = d[0] + rd2
            
            if d[1] + rd1 < 0:
                d[1] = 2*np.pi + d[1] + rd1
            elif d[1] + rd1 > 2*np.pi:    
                d[1] = d[1] + rd1 - 2*np.pi
            else:
                d[1] = d[1] + rd1
        
        return tissue
    
def distance(a,b):
    if a[2] != 0 and b[2] != 0:
        return np.sqrt(a[0]*a[0]+b[0]*b[0]-2*a[0]*b[0]*np.cos(a[1]-b[1]))
    else: return -1
    
def neighbours(tissue,d):
    k=0
    result=[]
    c=0
    for p in tissue:
        k=0
        for p1 in tissue:
            if distance(p,p1)> 0 and distance(p,p1) <d:  #0.565
                k+=1            
        result.append([])
        result[c].append(p)
        result[c].append(k)
        c+=1
    return result

def normsys(tissue):
    nei=neighbours(tissue,0.565)
    for i in range (0, len(tissue)):
        if nei[i][1] == 3:
            tissue[i][2]=2
    return tissue
######
# 0: deleted (black)
# 1: interior cells (blue) 
# 2: border cells (green)
# 3: cells miss neighbours (yellow)

######    
def checkdamage(tissue,nei,angle):
    a=np.pi/180
    for i in range (len(tissue)):         
        if round(tissue[i][1],7) < round((angle+15)*a,7) and round(tissue[i][1],7)>= round((angle - 30)*a,7):
            if (tissue[i][2]== 2 and nei[i][1] < 3) or (tissue[i][2] == 1 and nei[i][1] < 4):
                tissue[i][2]=3
#                print 'd',tissue[i]
    return tissue

def short(tissue,angle):
    a=np.pi/180
    r=[]
    for t in tissue:         
        if t[2]==3 and round(t[1],7) < round(angle*a,7) and round(t[1],7)>= round((angle - 15)*a,7):
            r=t
            break

    y = np.arange(0.5,round(2*r[0],0)/2+0.5, 0.5)
    x=[]
    for y1 in y:
        x.append(r[1])
    return x,y

def plottissue(tissue):
#    fig = plt.figure()
    ax = plt.subplot(111, polar=True)
    
    ax.scatter(0, 0,200,color='red')
    
    co=''
    
    for i in range (0,len(tissue)):
        if tissue[i][2] == 0: 
            co='black'
        elif tissue[i][2]==1:
            co='blue'
        elif tissue[i][2]==2:
            co='green'
        else:
            co='yellow'
   
        ax.scatter(tissue[i][1],tissue[i][0],100,color=co)
    ax.set_yticklabels([])
    plt.savefig('model1.jpg',dpi=100, format='jpg', bbox_inches='tight')
    ax.plot()



def delete(tissue,num):
     angle=45
     a=np.pi/180
     k=0
     dead=[]
#    for i in range(100,100+num):
     for t in tissue:         
        if t[0]> 5 and round(t[1],7) < round(angle*a,7) and round(t[1],7)>= round((angle - 15)*a,7):
 
#        k=randint(0,len(tissue)-1)
#            tissue[i][2]=0
            t[2]=0
            dead += [t]
            k+=1
        if k==num:
            break
#        print (i,k)
     return tissue,dead
    
##############################################
# main                                  
##############################################
n=newtissue()
n1=[[n[x][y] for y in range(len(n[0]))] for x in range(len(n))] 

###############    
normtissue=normsys(n)
noisetissue=noise(normtissue,2)
#normal entropy
normentropy=[]
j=0
for i in xrange (15,361,15):         
    normentropy.append([])
    normentropy[j].append(i)
    normentropy[j].append(entropy(n,i)[0])
    j += 1
#print normentropy    
################

dele,dead=delete(noisetissue,20)
nei2=neighbours(dele,0.579)

#print 'dead', dead,len (dead)
#checkdamage(noisetissue,nei2)
#print (nei2)

curentropy=[]
j=0  
for i in xrange (15,361,15):         
    curentropy.append([])
    curentropy[j].append(i)
    curentropy[j].append(entropy(noisetissue,i)[0])
    j += 1
#print curentropy
### damaged segments
segs=[]
for i in range (0, len(curentropy)):
    if np.abs(normentropy[i][1]-curentropy[i][1]) > 0.0001:
#        print normentropy[i][0]
        segs.append(normentropy[i][0])
#print seg
        
for s in segs:
    checkdamage(noisetissue,nei2,s)
    x,y=short(noisetissue,s)
#    print s
    
#print x,y

# stem cell moves to damage region
Acc_12 = y
Acc_11 = x
# Set up formatting for the movie files
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=50, metadata=dict(artist='Me'), bitrate=1800)

# Scatter plot
fig = plt.figure(figsize = (8,8))
axes = plt.subplot(111, polar=True)
axes.set_xlim(0, 2*np.pi)
axes.set_ylim(0, 8.5)

#axes.scatter(0, 0,100,color='red')
    
co=''

for i in range (0,len(noisetissue)):
    if noisetissue[i][2] == 0: 
        co='black'
    elif noisetissue[i][2]==1:
        co='blue'
    elif noisetissue[i][2]==2:
        co='green'
    else:
        co='yellow'
   
    axes.scatter(noisetissue[i][1],noisetissue[i][0],70,color=co)

#point, = axes.plot([Acc_11[0]],[Acc_12[0]], 'ro')
point, = axes.plot(0,0, 'ro')
def ani(coords):
    point.set_data([coords[0]],[coords[1]])
    return point

def frames():
    for acc_11_pos, acc_12_pos in zip(Acc_11, Acc_12):
        yield acc_11_pos, acc_12_pos

ani = animation.FuncAnimation(fig, ani, frames=frames, interval=1000, repeat=False)
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
#mywriter = FFMpegFileWriter(fps=1,codec="libx264")
#ani.save("test.mp4", writer=mywriter)
##plt.show

##x1=[]
##y1=[]
##for d in dead:
##    x1 += [d[0]]
##    y1 += [d[1]]
##Acc_11 = y1
##Acc_12 = x1
###plt.scatter(0,0, color='r')
##def anim(coords):
##     
##     if coords[1]>=7.9:
##
##         return plt.scatter([coords[0]],[coords[1]], color='g')
##     else:
##        
##        return plt.scatter([coords[0]],[coords[1]], color='blue')
##    
##
##def repair():
##    for acc_11_pos, acc_12_pos in zip(Acc_11, Acc_12):
##        yield acc_11_pos, acc_12_pos
##
##
##ani2 = animation.FuncAnimation(fig, anim, frames=repair, interval=1000,repeat=False)
###Writer = animation.writers['ffmpeg']
###mywriter = Writer(fps=1, metadata=dict(artist='Me'), bitrate=1800)
####mywriter = FFMpegFileWriter(fps=1,codec="libx264")
####ani2.save("test.mp4", writer=mywriter)
####ani2.save('basic_animation.mp4', fps=1, extra_args=['-vcodec', 'libx264'])

##plt.show()





















