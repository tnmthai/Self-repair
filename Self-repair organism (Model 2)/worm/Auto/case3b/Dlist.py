"""
@author: Thai Tran
"""

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
       self.up   = None
       self.down = None
       
class DoublyLinkedList:
    def __init__(self):
        self.first= [None]*35
        self.last = [None]*35

    def updateUD (self,d):#update up and down
                
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
# ##     
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
        
    def search (self, element,d):
        
        for i in range(0,d):
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
 
    def display(self,d):

        
        for i in range(0,d):
            current = self.first[i]            
            print "Level ",i
            while current:
                print(current.data)
                
                current = current.next

        
    def extractdata(self,d):
        Tissue=[]
        for i in range(0,d):
            current = self.first[i]
            
            while current:                
                Tissue.append(current.data)
                current = current.next
        
        return Tissue
        
    def damagecase1(self,d): # make a damage part (case 1 a.)

        
        for i in range(0,d):
            current = self.first[i]
            while current != None:
                if current.data[0] <3 and current.data[1]>=0 and current.data[1]<11:
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
    def damagecase3b(self,d): # make a hole (case 3b.)

        
        for i in range(0,d):
            current = self.first[i]
            while current != None:
                if current.data[0] >=21 and current.data[0] <=27 and current.data[1]>=3 and current.data[1]<=7:
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
        
        for i in range(0,7):
            current = self.first[i]
           
            print "level-down",i

            while current:
                print current.data
                print(current.down.data)           

                current = current.next
                
        for i in range(0,7):
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
                elif current.data[1]!= current.down.data[1]:
                    k=k+1
                    
                if current.up is None:
                    k=k+1  
                elif current.data[1]!= current.up.data[1]:
                    k=k+1
                    
                if current.prev is None:
                    k=k+1
                elif current.data[1]!= current.prev.data[1]+0.5:
                    k=k+1
                    
                if current.next is None:
                    k=k+1
                elif current.data[1]!= current.next.data[1]-0.5:
                    k=k+1    
                print(current.data , k)           

                current = current.next
    def Headdetect(self,d,seg): # make a damage part (case 1 a.)
        level=[]
        index=[]
        D_list=[]

        for i in range(1,d-1):
            current = self.first[i]
            
            idx=0
            while current != None:
                idx += 1
                current = current.next
            
            if idx <fidx and seg<=1 and seg>=0:
                level.append(i)
#                print i,idx, self.last[i].data
#                D_list.append(self.last[i].data)
            if idx <fidx and seg>=2 and seg <4:
                level.append(i)
#                print i,idx, self.last[i].data
#                D_list.append(self.first[i].data)   
            fidx = fidx - 2
        #find up/down border   
        border=[min(level)-1, max(level)+1]
        for lm in border:
            current = self.first[lm]  
            
            idx=0
            while current != None and current != self.last[lm]:
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
                        if k >=1 and idx <d-1 and idx >0  and lm>0 and lm<d-1:
                            index.append([lm,idx])
                            D_list.append(current.data)
                        if idx <d and idx >0  and lm == d-1 and k>=2:
                            index.append([lm,idx])
                            D_list.append(current.data)
                        
                    current = current.next
                    idx += 1

        print 'Damage list',D_list
        return level,D_list
    
    def Detectcase1(self,d,seg): # make a damage part (case 1 a.)
        level=[]
        index=[]
        D_list=[]
        fidx=0
        current = self.first[0]
        while current != None:
            
           fidx += 1
           current=current.next

        for i in range(0,d):
            current = self.first[i]
            
            idx=0
            while current != None:
                idx += 1
                current = current.next
            
            if idx <fidx and seg<=1 and seg>=0:
                level.append(i)
#                print i,idx, self.last[i].data
#                D_list.append(self.last[i].data)
            if idx <fidx and seg>=2 and seg <4:
                level.append(i)
#                print i,idx, self.last[i].data
#                D_list.append(self.first[i].data)   
            fidx = fidx - 2
        #find up/down border   
        border=[min(level)-1, max(level)+1]
        for lm in border:
            current = self.first[lm]  
            
            idx=0
            while current != None and current != self.last[lm]:
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
                        if k >=1 and idx <d-1 and idx >0  and lm>0 and lm<d-1:
                            index.append([lm,idx])
                            D_list.append(current.data)
                        if idx <d and idx >0  and lm == d-1 and k>=2:
                            index.append([lm,idx])
                            D_list.append(current.data)
                        
                    current = current.next
                    idx += 1

        print 'Damage list',D_list
        return level,D_list
    
    def detect3b(self,d): # detect damage (case 3b)

        D_list=[]
        
        for i in range(1,d-1):
            current = self.first[i]
            current = current.next
            
#            print "level",i
            
            while current.next != None :
                k=0
                if current.down is None:
                    k=k+1
                elif current.data[1]!= current.down.data[1]:
                    k=k+1
                    
                if current.up is None:
                    k=k+1  
                elif current.data[1]!= current.up.data[1]:
                    k=k+1
                    
                if current.prev is None:
                    k=k+1
                elif current.data[1]!= current.prev.data[1]+0.5:
                    k=k+1
                    
                if current.next is None:
                    k=k+1
                elif current.data[1]!= current.next.data[1]-0.5:
                    k=k+1    
                if k>0:
                    D_list.append(current.data)

                current = current.next
        return D_list