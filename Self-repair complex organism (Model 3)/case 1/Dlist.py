"""
@author: Thai Tran
"""
import random
from loaddata import distance
import numpy as np

class Node:
    def __init__(self, data,value):
       self.data = data #coordinate
       self.value= value #voltage
       self.type = 'd' #d-cell or stem cell
       self.group= None
       self.status = None
       #short range neighbours
       self.next = None
       self.prev = None
       self.up   = None
       self.down = None
       #long range neighbours (stem cells only)
       self.one = None
       self.two = None
       self.three= None
       self.four = None


class DoublyLinkedList:
    def __init__(self):
        self.first= [None]*120
        self.last = [None]*120

    def updateUD (self,d0):#update up and down
        d=5*d0-9
        current0 = self.first[0]

        while current0 != None:
            current0.up = None
            current1 = self.first[1]

            if current0.data[1] >= self.first[1].data[1] and current0.data[1]<=self.last[1].data[1]:
                while current1 != None:
                    if current1.data[1] < current0.data[1]:
                        current1 = current1.next
                    elif current0.data[1]==current1.data[1]:
                        current0.down   = current1
                        break
            else:
                current0.down   = None

            current0 = current0.next

#        #update None for the end list
        current0 = self.first[d-1]
        current1 = self.first[d-2]

        while current0 != None:
            current0.down   = None
            if current0.data[1] >= self.first[d-2].data[1] and current0.data[1]<=self.last[d-2].data[1]:
                while current1 != None:
                    if current0.data[1] > current1.data[1]:
                        current1 = current1.next
                    elif current0.data[1]==current1.data[1]:
                        current0.up = current1
                        break
                    else:
                        break
            current0 = current0.next
####
#        #update up/down for middle
        for i in range(1,d-1):

            current1 = self.first[i]
            current0 = self.first[i-1]
            current2 = self.first[i+1]

            while current1 != None:

                if current1.data[1] >= self.first[i-1].data[1] and current1.data[1]<=self.last[i-1].data[1]:
                    while current0 != None:
                        if current0.data[1] < current1.data[1]:
                            current0 = current0.next
                        elif current0.data[1] == current1.data[1]:
                            current1.up   = current0
                            break
                        else:
                            break
                else:
                    current1.up   = None

                if current1.data[1] >= self.first[i+1].data[1] and current1.data[1]<=self.last[i+1].data[1]:
                    while current2 != None:
                        if current2.data[1] < current1.data[1]:
                            current2 = current2.next
                        elif current2.data[1] == current1.data[1]:
                            current1.down   = current2
                            break
                        else:
                            break
                else:
                    current1.down   = None

                current1 = current1.next
# ##
    def get_node(self, index,level):

        current = self.first[level]
        for i in range(index):
            if current is None:
                return None
            current = current.next
#            print current.data
        return current,current.data

    def getnode (self, data,d):

        for i in range(0, 5*d-9):
            current = self.first[i]

            while current != None:
                if current.data == data:
                    return current
                    break
                else:
                    current = current.next
        return -1

    def search (self, element,d):

        for i in range(0, 5*d-9):
            current = self.first[i]
            index=0
            while current != None:
                if current.data == element:
                    return index,i
                    break
                else:
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

    def display(self,d): #

        for i in range(0,d):
            current = self.first[i]
            print ("Level ",i)
            while current:
                print(current.data)

                current = current.next
#------------------------------------------------------------------------------
    def UpdateGroup(self,d):    #update group for each cell

        for j in range (0, 5*d-9):
            current = self.first[j]
            index=0
            while current != None:
                if j<13:
                    current.group=0
                elif j<=22 :
                    current.group=1
                elif index < 15 and j<=42 :
                    current.group=3
                elif index < 30 and j<=42 :
                    current.group=2
                elif index < 45 and j<=42 :
                    current.group=4
                elif index < 15 and j<=62:
                    current.group=8
                elif index < 30 and j<=62:
                    current.group=5
                elif index < 45 and j<=62:
                    current.group=7
                elif index < 15 and j<=82:
                    current.group=9
                elif index < 30 and j<=82:
                    current.group=6
                elif index < 45 and j<=82:
                    current.group=10
                elif j<=92:
                    current.group=11
                else :
                    current.group=12
                index += 1
                current = current.next

    def UpdateVolG(self,bigsc,d):#update voltage for each cell

        for i in range (0, 5*d-9):
            current = self.first[i]
            while current != None:
                g=current.group
                if current.value!=bigsc[g]:
                    current.value=bigsc[g]
                current = current.next

    def GetBigSC(self,d): # get values from big stem cells
        Bigsc=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        k=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        i=0
        for j in range (0, 5*d-9):
            current = self.first[j]
            while current != None:
                i=current.group
                Bigsc[i] += current.value
                k[i] += 1
                current = current.next
        for i in range (len(k)):
            Bigsc[i]=round(Bigsc[i]/k[i],4)
            
        print ('cells',k)    
        return Bigsc

    def UpdateSC (self, d): #update type=stem cells

        for j in [1,104]:
            current = self.first[j]
            index=0
            while current != None:
                if index == 1:
                    current.type='s'
                index += 1
                current = current.next

        for i in range(5,5*d-9,5):
            current = self.first[i]
            index=0
            t1=0
            while current != None:

                if index == 2:
                    current.type='s'

                    t1=index
                elif index == t1+5:
                    current.type='s'

                    t1=index
                index += 1
                current = current.next

    def width(self,i):        #length of list- DV direction
        current = self.first[i]
        count=0
        while current:
            count+=1
            current = current.next
        return count

    def SCdata(self,d): # get stem cell data
        Sc=[]
        for i in range(0,5*d-9):
            current = self.first[i]
            while current:
                if current.type=='s':
                    Sc.append(current.data)
                current = current.next

        return Sc

    def UpdateSCNet(self,d): # Update stem cell neighbourhood

        sc=self.SCdata(d)
        for s in sc:
            i=1
            for c in sc:
                if distance(s, c)> 0 and distance(s, c)<6:

                    node1=self.getnode(s, d)
                    node2=self.getnode(c,d)
                    if i==1:
                        node1.one=node2
                    elif i==2:
                        node1.two=node2
                    elif i==3:
                        node1.three=node2
                    else:
                        node1.four=node2

                    i += 1

    def extractdata(self,d):
        Tissue=[]
        k=0
        for i in range(0,5*d-9):
            current = self.first[i]

            while current:
                Tissue.append([])
                Tissue[k].append(current.data)
                Tissue[k].append(current.value)
                Tissue[k].append(current.type)
                Tissue[k].append(current.status)

                k+=1
                current = current.next

        return Tissue


##### Normal
    def Case1a(self,position=0): # change value 1 cell
        if position==0:
            i=random.randint(0, 100)
            current = self.first[i]
            ind=random.randint(0,self.width(i))
            index=0
            while current != None:
                if index==ind:
                    current.value += current.value*1
                    # current.next.value += current.next.value*1
                    # current.prev.value += current.prev.value*1
                    # current.up.value += current.up.value*1
                    # current.down.value += current.down.value*1
                    # current.next.next.value += current.next.next.value*1
                    # current.next.up.value += current.next.up.value*1
                    # current.next.down.value += current.next.down.value*1
                    break
                else:
                    index +=1
                current = current.next
                
            i=random.randint(0, 100)
            current = self.first[i]
            ind=random.randint(0,self.width(i))
            index=0
            while current != None:
                if index==ind:
                    current.value += current.value*1
                    current.next.value += current.next.value*1
                    current.prev.value += current.prev.value*1
                    current.up.value += current.up.value*1
                    current.down.value += current.down.value*1
                    current.next.next.value += current.next.next.value*1
                    current.next.up.value += current.next.up.value*1
                    current.next.down.value += current.next.down.value*1
                    break
                else:
                    index +=1
                current = current.next
                

    def Case1b(self,d,position=0): # change value many cells
        if position==0:
            for i in range(0,5*d-9):
                current = self.first[i]
                while current != None:
                    current.value += current.value*0.2* random.choice([-1,1])
                    current = current.next

#------------------------------------------------------