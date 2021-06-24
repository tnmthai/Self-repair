class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
       self.up   = None
       self.down = None
       
class DoublyLinkedList:
    def __init__(self):
        self.first= [None]*30
        self.last = [None]*30

    def updateUD (self,d):#update up and down
        #update  None for 1st list
        
        current0 = self.first[0]  
            
        while current0 != None: 
            current0.down = None
            current1 = self.first[1]
            while current1 != None and current0.data[0]>current1.data[0]:
                current1 = current1.next
            if current0.data[0]==current1.data[0]:     
                current0.up   = current1
            else:
                current0.up   = None
                
            current0 = current0.next
            
       
        #update None for the end list
        current0 = self.first[d-1]
        current1 = self.first[d-2]          
            
        while current0 != None: 
            
            current1 = self.first[d-2]
            while current1 != None and current0.data[0]>current1.data[0]:
                current1 = current1.next
                
            if current0.data[0]==current1.data[0]:     
                current0.down = current1
            else:
                current0.down = None
            current0.up   = None
            
            current0 = current0.next
            
        #update up/down for middle
        for i in range(1,d-1):
            
            current1 = self.first[i]           
            current0 = self.first[i-1]
            current2 = self.first[i+1]
            
            while current1 != None: 
            
                if current1.data[0] >= self.first[i-1].data[0] and current1.data[0]<=self.last[i-1].data[0]:
                    while current0 != None:
                        if current0.data[0] < current1.data[0]:         
                            current0 = current0.next 
                        elif current0.data[0] == current1.data[0]:                            
                            current1.down   = current0
                            break
                            
                else:       
                    current1.down   = None                 

                if current1.data[0] >= self.first[i+1].data[0] and current1.data[0]<=self.last[i+1].data[0]:
                    while current2 != None:
                        if current2.data[0] < current1.data[0]:         
                            current2 = current2.next 
                        elif current2.data[0] == current1.data[0]:                            
                            current1.up   = current2
                            break
                else:       
                    current1.up   = None

                current1 = current1.next
 
    def get_node(self, index,level):
        
        current = self.first[level]
        for i in range(index):
            if current is None:
                return None
            current = current.next
#            print current.data
        return current.data
        
    def search (self, element,d):
        
        for i in range(0,d):
            current = self.first[i]
            index=0
            while current != None:
                if current.data == element:
                    return index,i
                current = current.next
                index += 1
        return -1

    def insert_after(self, ref_node, new_node,level):
        new_node.prev = ref_node
        if ref_node.next is None:
            self.last[level] = new_node
        else:
            new_node.next = ref_node.next
            new_node.next.prev = new_node
            
        ref_node.next = new_node
        
    def insert_before(self, ref_node, new_node,level):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.first[level] = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        ref_node.prev = new_node

      
    def insert_at_beg(self, new_node,level):
        
        if self.first[level] is None:
            self.first[level] = new_node
            self.last[level] = new_node
        else:
            self.insert_before(self.first[level], new_node,level)
            
          
    def insert_at_end(self, new_node,level):
        if self.last[level] is None:
            self.last[level] = new_node
            self.first[level] = new_node
        else:
            self.insert_after(self.last[level], new_node,level)
            
    def remove(self, node):
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next
 
        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev
 
    def display(self,d):

        fileout=open('datastructure.txt','w')
        for i in range(0,d):
            current = self.first[i]
            x=[]
            y=[]
            
            print "level",i
            fileout.write("Level:" + repr(i))
            fileout.write('\n') 
            while current:
                print(current.data)
                fileout.write(repr(current.data))
                fileout.write('\n')  
                
                x+=current.data[:1]
                y+=current.data[1:]
                current = current.next
#            plt.scatter(x, y)
        fileout.close()   
        
    def extractdata(self,d):
        Tissue=[]
        for i in range(0,d):
            current = self.first[i]
            
            while current:                
                Tissue.append(current.data)
                current = current.next
        
        return Tissue
        
    def damage1(self,d): # make a damage part (case 1 a.)

        
        for i in range(0,d):
            current = self.first[i]
            while current != None:
                if current.data[0] >3 and current.data[1]>=0 and current.data[1]<11:
#               
                    if current.prev is None:
                        self.first[i] = current.next
                    else:
                        current.prev.next = current.next
                    if current.next is None:
                        self.last[i] = current.prev
                    else:
                        current.next.prev = current.prev               
                   
                current = current.next
    
    def displayud(self): #display up and down 
        
        for i in range(5,6):
            current = self.first[i]
           
            print "level-down",i

            while current:
                print(current.down.data)           

                current = current.next
                
        for i in range(5,6):
            current = self.first[i]
           
            print "level-up",i

            while current:
                print(current.up.data)           

                current = current.next   

    def countnei(self,d): # COunt missing neighbours
        
        for i in range(0,d):
            current = self.first[i]
           
            print "level",i
            
            while current != None:
                k=0
                if current.down is None:
                    k=k+1
                if current.up is None:
                    k=k+1    
                if current.prev is None:
                    k=k+1
                if current.next is None:
                    k=k+1
                    
                print(current.data , k)           

                current = current.next

    def detect(self,d,seg): # make a damage part (case 1 a.)
        level=[]
        index=[]
        D_list=[]
        for i in range(0,d):
            current = self.first[i]
            
            idx=0
            while current != None:
                idx += 1
                current = current.next
            
            if idx <(d-1)*2 and seg<=1 and seg>=0:
                level.append(i)
#                print i,idx, self.last[i].data
                D_list.append(self.last[i].data)
            if idx <(d-1)*2 and seg>=2 and seg <4:
                level.append(i)
#                print i,idx, self.last[i].data
                D_list.append(self.first[i].data)   
        #find up/down border   
        border=[min(level)-1, max(level)+1]
        for lm in border:
            current = self.first[lm]   
            idx=0
            while current != None:
                    k=0
                    
                    if current.down is None:
                        k=k+1
                    if current.up is None:
                        k=k+1    
                    if current.prev is None:
                        k=k+1
                    if current.next is None:
                        k=k+1
                        
                    if seg<=1:
                        if k >=1 and idx >0 and lm>0 and lm<d-1:
                            index.append([lm,idx])
                            D_list.append(current.data)
                        if idx >0  and lm == d-1 and k>=2:
                            index.append([lm,idx])
                            D_list.append(current.data)
                    if seg >=2:
                        if k >=1 and idx <d-1 and lm>0 and lm<d-1:
                            index.append([lm,idx])
                            D_list.append(current.data)
                        if idx <d  and lm == d-1 and k>=2:
                            index.append([lm,idx])
                            D_list.append(current.data)
                        
                    current = current.next
                    idx += 1
#        print 'level',level
#        print 'index',index
        print 'Damage list',D_list
        return level,D_list

class Main:
        
    def grow(self,d0):
       import matplotlib.pyplot as plt
       import matplotlib.patches as patches
       import numpy as np
       from entropy import entropy
       
       Body = DoublyLinkedList()
       Body.insert_at_beg(Node([0,0]),0)
       
       fig1 = plt.figure()
       ax1 = fig1.add_subplot(221, aspect='equal')
       ax2 = fig1.add_subplot(222, aspect='equal')
       ax3 = fig1.add_subplot(223, aspect='equal')
       ax4 = fig1.add_subplot(224, aspect='equal')
       lims = (-6, 6)
#       d0=11
       mid=[0,d0/2]
       
       x=[0]
       y=[0]
#       x1 = np.arange(0,0.5,d+1)
       for d in range(1,d0):  #range(1,d0):

           for i in range(0,d+1):# range(0,d+1): #np.arange(0,0.5,d+1)

               if i==d:
                   for j in range(-d,d+1):#range(-d,d+1):                       
                       Body.insert_at_end(Node([j/2.0,i]),i)    
                       
               else:
                   for j in [-d,d]:
                       if j<0:
                           Body.insert_at_beg(Node([j/2.0,i]),i)

                       else:
                           Body.insert_at_end(Node([j/2.0,i]),i)
           
#               ax1.add_patch(patches.Rectangle((-d, 0), d*2, d*2,fill=None))

       Body.updateUD(d0)    
#       Body.display(d0)
#       Body.displayud()
       Body.countnei(d0)
       tissue=Body.extractdata(d0)
#       print tissue
       normal= entropy(tissue,mid)
       x=[]
       y=[]
       for t in tissue:
           x.append(t[0])
           y.append(t[1])
       ax1.scatter(x, y)
       plt.ylim(0,11)
       plt.xlim(lims)
       
       print 'damage'
       Body.damage1(d0)
       Body.updateUD(d0)  
#       Body.countnei(d0)
       
       
       tissue=Body.extractdata(d0)
#       print tissue
       damage= entropy(tissue,mid)
       
       ## detect damage location
       p=-1
       for i in range (0,4):
           if normal[i]!=damage[i]:
               p=i
       print 'damage area',p
#       index = Body.search([10, 20])
#       print index
#       print Body.get_node(index[0],index[1])
       x=[]
       y=[]
       for t in tissue:
           x.append(t[0])
           y.append(t[1])
       ax2.scatter(x, y)
       plt.ylim(0,11)
       plt.xlim(lims)
       ax3.scatter(x, y)
       ###identify border of damage
       
       level,Dlist=Body.detect(d0,p)
       x=[]
       y=[]
       for t in Dlist:
           x.append(t[0])
           y.append(t[1])
       ax3.scatter(x, y)
       plt.ylim(0,11)
       plt.xlim(lims)
       
       ### repair

       for d in Dlist:
           print d
           xn=d[0]
           l=d[1]
           
           if p<=1:
               while xn <(d0-1)/2 and Body.search([xn+0.5,l],d0)<0:
                   Body.insert_at_end(Node([xn+0.5,l]),l)
                   xn += 0.5
           if p>=2:
               while xn >-(d0-1)/2 and Body.search([xn-0.5,l],d0)<0:
                   Body.insert_at_beg(Node([xn-0.5,l]),l)
                   xn -= 0.5
               
       tissue=Body.extractdata(d0)
       x=[]
       y=[]
       for t in tissue:
           x.append(t[0])
           y.append(t[1])
       ax4.scatter(x, y)
       plt.ylim(0,11)
       plt.xlim(lims)
#       Body.displayud()
s=Main()
s.grow(11)
        
