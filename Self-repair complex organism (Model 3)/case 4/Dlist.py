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
                    current.value += current.value*0.2
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
### Damge case 2: 1 d-cell damage
    def Case2(self, position, node):
        if node==None:
            if position==0:
                i=77#random.randint(25, 80)
            else:
                i=72
            current = self.first[i]
            ind=20
            index=0
            while current != None:
                if index==ind and current.type!='s':
                    current.status=-1
                    current.value=0
                    self.SendMsgdc(current)
                    return self.SendMsgSC(current),current
                    break
                index +=1
                current = current.next

        elif node!=None:
            f=0
            current=node
            current.status=-1
            current.value=0
            # change neighbours
            if current.next != None and current.next.type !='s' and current.next.value>0:
                current.next.value += 0.01
                current.next.status =-1
                self.SendMsgSC(current.next)
                f=1
            if current.prev != None and current.prev.type !='s' and current.prev.value>0:
                current.prev.value += 0.01
                current.prev.status =-1
                self.SendMsgSC(current.prev)
                f=1
            if current.up != None and current.up.type !='s' and current.up.value>0:
                current.up.value += 0.01
                current.up.status =-1
                self.SendMsgSC(current.up)
                f=1
            if current.down != None and current.down.type !='s' and current.down.value>0:
                current.down.value += 0.01
                current.down.status =-1
                self.SendMsgSC(current.down)
                f=1
            return f
    def SendMsgdc(self,node):
        try:
            if node.next.value!=0:
                node.next.status=-1
                node.next.value =0.1 #+=node.next.value*0.2
        except :
            pass
        try:
            if node.up.value!=0:

                node.up.status=-1
                node.up.value =0.1 #+=node.up.value*0.2
        except :
            pass
        try:
            if node.down.value!=0:
                node.down.status=-1
                node.down.value =0.1 #+=node.down.value*0.2
        except :
            pass        
        try:
            if node.prev.value!=0:
                node.prev.status=-1
                node.prev.value =0.1 #+=node.prev.value*0.2
        except :
            pass

    def SendMsgSC(self,dnode):
        node1=dnode.next
        node2=dnode.prev
        node3=dnode.up
        node4=dnode.down

        ### Next
        i=0
        f=0
        while node1 != None and f==0:

            if node1.type=='s':
                node1.status=-1
                # node1.value -= 0.1
                f = 1
                return node1
                break
            elif node1.down!= None and node1.down.type =='s':
                node1.down.status=-1
                # node1.down.value -= 0.1
                f = 1
                return node1.down
                break
            elif node1.down.down!= None and node1.down.down.type =='s':
                node1.down.down.status=-1
                # node1.down.down.value -= 0.1
                f = 1
                return node1.down.down
                break
            elif node1.up != None and node1.up.type =='s':
                node1.up.status=-1
                # node1.up.value -= 0.1
                f = 1
                return node1.up
                break
            elif node1.up.up != None and node1.up.up.type =='s':
                node1.up.up.status=-1
                # node1.up.up.value -= 0.1
                f = 1
                return node1.up.up
                break
            elif i<2:
                i += 1
            else:
                break
            node1 = node1.next

        #prev
        i=0
        while node2 != None and f==0:

            if node2.type=='s':
                node2.status=-1
                # node2.value -= 0.1
                f = 1
                return node2
                break
            elif node2.up != None and node2.up.type =='s':
                node2.up.status=-1
                # node2.up.value -= 0.1
                f = 1
                return node2.up
                break
            elif node2.up.up != None and node2.up.up.type =='s':
                node2.up.up.status=-1
                # node2.up.up.value -= 0.1
                f = 1
                return node2.up.up
                break
            elif node2.down != None and node2.down.type =='s':
                node2.down.status=-1
                # node2.down.value -= 0.1
                f = 1
                return node2.down
                break
            elif node2.down.down != None and node2.down.down.type =='s':
                node2.down.down.status=-1
                # node2.down.down.value -= 0.1
                f = 1
                return node2.down.down
                break
            elif i<2:
                i += 1
            else:
                break
            node1 = node1.next
        #up
        i=0
        while node3 != None and f==0:

            if node4.type=='s':
                node4.status=-1
                # node4.value -= 0.1
                f=1
                return node4
                break
            elif i<2:
                i += 1
            else:
                break
            dnode = node4.up
        #down
        i=0
        while node4 != None and f==0:

            if node4.type=='s':
                node4.status=-1
                # node4.value -= 0.1
                f=1
                return node4
                break
            elif i<2:
                i += 1
            else:
                break
            dnode = node4.down
    def extractgroup(self,d,g):
        Tissue=[]
        k=0
        for i in range(0,5*d-9):
            current = self.first[i]
            while current:
                if current.group==g:
                    Tissue.append([])
                    Tissue[k].append(current.data)
                    Tissue[k].append(current.value)
                    Tissue[k].append(current.type)
                    Tissue[k].append(current.status)
                    k+=1
                current = current.next

        return Tissue
    def restore(self,node,sc):
        node.value=0.05
        node.status=None

    def SCRepair(self,sc):

        print ('Stem cell at ',sc.data,'is repairing.')
        sc.value=0.9
        i=0
        j=0
        if sc.next!= None:
            n=sc.next
            i+=1
            while n!=None and i<=2:
                if n.value==0:
                    self.restore(n,sc)
                if n.down!=None:
                    d=n.down
                    j+=1
                    while d!=None and j<=2:
                        if d.value==0:
                            self.restore(d,sc)
                        d=d.down
                        j+=1
                n=n.next
                i+=1
                j=0
        ##### Prev
        i=0
        j=0
        if sc.prev!= None:
            n=sc.prev
            i+=1
            while n!=None and i<=2:

                if n.value==0:
                    self.restore(n,sc)
                if n.up!=None:
                    d=n.up
                    j+=1
                    while d!=None and j<=2:

                        if d.value==0:
                            self.restore(d,sc)
                        d=d.up
                        j+=1
                n=n.prev
                i+=1
                j=0
           ### Up
        i=0
        j=0
        if sc.up!= None:
            n=sc.up
            i+=1
            while n!=None and i<=2:

                if n.value==0:
                    self.restore(n,sc)
                if n.next!=None:
                    d=n.next
                    j+=1
                    while d!=None and j<=2:

                        if d.value==0:
                            self.restore(d,sc)
                        d=d.next
                        j+=1
                n=n.up
                i+=1
                j=0
        ### Down
        i=0
        j=0
        if sc.down!= None:
            n=sc.down
            i+=1
            while n!=None and i<=2:

                if n.value==0:
                    self.restore(n,sc)
                if n.prev!=None:
                    d=n.prev
                    j+=1
                    while d!=None and j<=2:

                        if d.value==0:
                            self.restore(d,sc)
                        d=d.prev
                        j+=1
                n=n.down
                i+=1
                j=0
#--------------------------------------------------------------------------------
    def Case3(self,position=0):# remove 3 d-cells

        if position==1:
            _,node=self.Case2(position,None)
            try:
                self.Case2(position,node.next)
                self.Case2(position,node.prev)
                self.Case2(position,node.up)
                self.Case2(position,node.down)
            except:
                pass
        return node

    def SCscan(self,d): # stem cell scan and repair
        for i in range(0,5*d-9):
            current = self.first[i]
            while current:
                if current.type=='s' and current.status==-1:
                    self.SCRepair(current)
                current = current.next


#------------------------------------------------------------------------------
    def Case4(self,position=0):# remove sc - a block
        try:
            sc,_ =self.Case2(position,None)
            print (sc.data)
            self.removeablock(sc)

        except:
            pass
        return sc
    
    def Case4only(self,position=0):# remove sc - a block
        try:
            sc,_ =self.Case20(position,None)
            print (sc.data)
            self.removeblock(sc)

        except:
            pass
        return sc
    
    def CheckSCNei(self,node):

        if node.one.value!=0 and node.two.value!=0 and node.three.value!=0 and node.four.value!=0:
            node.status=0

    def Repairc4(self,d):
        for i in range(0,5*d-9):
            current = self.first[i]
            while current:
                try:
                    if current.type=='s' and current.status==-1:
                        
                        self.SCRepair(current)
                        self.CheckSCNei(current)
                        newnode = self.SCNet(current)
                        self.SCRepair(newnode)
                        self.CheckSCNei(newnode)
                    current = current.next
                except:
                    pass


    def removeablock(self,sc):

        print ('Stem cell at ',sc.data)
        i=0
        j=0
        sc.value=0
        sc.status=-1
        self.SendSCnet(sc)

        if sc.next!= None:
            n=sc.next
            i+=1
            while n!=None and i<=2:
                if n.value!=0:
                    n.value =0
                    n.status=-1
                    # print ('n',n.data)
                    self.SendMsgdc(n)
                if n.down!=None:
                    d=n.down
                    j+=1
                    while d!=None and j<=2:
                        if d.value!=0:
                            d.value=0
                            d.status=-1
                            # print ('d',d.data)
                            self.SendMsgdc(d)
                        d=d.down
                        j+=1
                n=n.next
                i+=1
                j=0
        ##### Prev
        i=0
        j=0
        if sc.prev!= None:
            n=sc.prev
            i+=1
            while n!=None and i<=2:

                if n.value!=0:
                    n.value =0
                    n.status=-1
                    # print (n.data)
                    self.SendMsgdc(n)
                if n.up!=None:
                    d=n.up
                    j+=1
                    while d!=None and j<=2:

                        if d.value!=0:
                            d.value=0
                            d.status=-1
                            # print (d.data)
                            self.SendMsgdc(d)
                        d=d.up
                        j+=1
                n=n.prev
                i+=1
                j=0
           ### Up
        i=0
        j=0
        if sc.up!= None:
            n=sc.up
            i+=1
            while n!=None and i<=2:

                if n.value!=0:
                    n.value =0
                    n.status=-1
                    # print (n.data)
                    self.SendMsgdc(n)
                if n.next!=None:
                    d=n.next
                    j+=1
                    while d!=None and j<=2:

                        if d.value!=0:
                            d.value=0
                            d.status=-1
                            # print (d.data)
                            self.SendMsgdc(d)
                        d=d.next
                        j+=1
                n=n.up
                i+=1
                j=0
        ### Down
        i=0
        j=0
        if sc.down!= None:
            n=sc.down
            i+=1
            while n!=None and i<=2:

                if n.value!=0:
                    n.value =0
                    n.status=-1
                    # print (n.data)
                    self.SendMsgdc(n)
                if n.prev!=None:
                    d=n.prev
                    j+=1
                    while d!=None and j<=2:

                        if d.value!=0:
                            d.value=0
                            d.status=-1
                            # print (d.data)
                            self.SendMsgdc(d)
                        d=d.prev
                        j+=1
                n=n.down
                i+=1
                j=0

    def SCNet(self,sc):
        try:
            if sc.one.value ==0:
                sc.one.value = 0.9 #sc.value +0.05
                # print ('1',sc.one.data)
                return sc.one
            elif sc.two.value == 0:
                sc.two.value =sc.value
                # print ('2',sc.two.data)
                return sc.two
            elif sc.three.value == 0:
                sc.three.value =sc.value
                # print ('3',sc.three.data)
                return sc.three
            elif sc.four.value == 0:
                sc.four.value = 0.9 #=sc.value -0.05
                # print ('4',sc.four.data)
                return sc.four
            else:
                return sc
        except :
            pass

    def SendSCnet(self,sc):
        try:
            if sc.one.value !=0:
                sc.one.status=-1
                sc.one.value =0.9#+=sc.one.value*0.1
                print ('a',sc.one.data)
            if sc.two.value != 0:
                sc.two.status=-1
                sc.two.value =0.9#+=sc.two.value*0.1
                print ('b',sc.two.data)
            if sc.three.value != 0:
                sc.three.status=-1
                sc.three.value =0.9#+=sc.three.value*0.1
                print ('c',sc.three.data)
            if sc.four.value != 0:
                sc.four.status=-1
                sc.four.value =0.9#+=sc.four.value*0.1
                print ('d',sc.four.data)
        except :
            pass
    
    def Case20(self, position, node):
        if node==None:
            if position==0:
                i=77#random.randint(25, 80)
            else:
                i=72
            current = self.first[i]
            ind=20
            index=0
            while current != None:
                if index==ind and current.type!='s':
                    current.status=-1
                    current.value=0
                    # self.SendMsgdc(current)
                    return self.SendMsgSC(current),current
                    break
                index +=1
                current = current.next
                
                
    
    def removeblock(self,sc):

        print ('Stem cell at ',sc.data)
        i=0
        j=0
        sc.value=0
        sc.status=-1
        # self.SendSCnet(sc)

        if sc.next!= None:
            n=sc.next
            i+=1
            while n!=None and i<=2:
                if n.value!=0:
                    n.value =0
                    n.status=-1

                if n.down!=None:
                    d=n.down
                    j+=1
                    while d!=None and j<=2:
                        if d.value!=0:
                            d.value=0
                            d.status=-1

                        d=d.down
                        j+=1
                n=n.next
                i+=1
                j=0
        ##### Prev
        i=0
        j=0
        if sc.prev!= None:
            n=sc.prev
            i+=1
            while n!=None and i<=2:

                if n.value!=0:
                    n.value =0
                    n.status=-1

                if n.up!=None:
                    d=n.up
                    j+=1
                    while d!=None and j<=2:

                        if d.value!=0:
                            d.value=0
                            d.status=-1

                        d=d.up
                        j+=1
                n=n.prev
                i+=1
                j=0
           ### Up
        i=0
        j=0
        if sc.up!= None:
            n=sc.up
            i+=1
            while n!=None and i<=2:

                if n.value!=0:
                    n.value =0
                    n.status=-1

                if n.next!=None:
                    d=n.next
                    j+=1
                    while d!=None and j<=2:

                        if d.value!=0:
                            d.value=0
                            d.status=-1

                        d=d.next
                        j+=1
                n=n.up
                i+=1
                j=0
        ### Down
        i=0
        j=0
        if sc.down!= None:
            n=sc.down
            i+=1
            while n!=None and i<=2:

                if n.value!=0:
                    n.value =0
                    n.status=-1

                if n.prev!=None:
                    d=n.prev
                    j+=1
                    while d!=None and j<=2:

                        if d.value!=0:
                            d.value=0
                            d.status=-1

                        d=d.prev
                        j+=1
                n=n.down
                i+=1
                j=0

#--------------------------------------------------------------------------------