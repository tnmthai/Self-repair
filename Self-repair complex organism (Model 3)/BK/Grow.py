"""
@author: Thai Tran
"""

class Grow:
    
    def Head(self,d0):
       from Dlist import Node
       from Dlist import DoublyLinkedList
       #New list of Head
       Head = DoublyLinkedList()
       
       value=0.7
       seed=[25,23]
       Head.insert_at_beg(Node(seed,value),0) 
           
       for d in range(1,d0):  #range(1,d0):
           k = d
           
           for i in range(0,d+1):# range(0,d+1): #np.arange(0,0.5,d+1)
               
               if i <10:
                   value=0.7
               else: value=0.8    
                   
               if i==d:
                   Head.insert_at_end(Node([seed[0]-i,seed[1]],value),i)    

               else:
                   for j in [-k,k]:
                       if j<0:
                           Head.insert_at_beg(Node([seed[0]-i,j+seed[1]],value),i)

                       else:
                           Head.insert_at_end(Node([seed[0]-i,j+seed[1]],value),i)
     
                   k = k - 1       
       return Head     
    
    def Body(self,d0):
       from Dlist import Node
       from Dlist import DoublyLinkedList
       #body part
       value=0.6
       seed=[26,23]
       Body = DoublyLinkedList()
       Body.insert_at_beg(Node(seed,value),0)
       
       for d in range(1,d0):  
         
           for i in range(0,d+1):
               if i<20:
                   value=0.6
               elif i<40:
                   value=0.55
               else:
                   value=0.5
               if i==d:
                   for j in range(-d,d+1):
                       if Body.search([seed[0]+i,j+seed[1]],d0)==-1:
                           Body.insert_at_end(Node([seed[0]+i,j+seed[1]],value),i)    
                       
               else:
                   for j in [-d,d]:
                       if j<0 and Body.search([seed[0]+i, j + seed[1]],d0)==-1:
                           Body.insert_at_beg(Node([seed[0]+i, j + seed[1]],value),i)
                           
                       elif Body.search([seed[0]+i, j + seed[1]],d0)==-1:
                           Body.insert_at_end(Node([seed[0]+i, j + seed[1]],value),i)
                           
       _,data=Body.get_node(0,d0-1)
       y=data[1]
       value=0.55
       for i in range (d0,3*d0-9):
          y=data[1]
          if i<40:
              value=0.55
          else:
              value=0.5
          for j in range (1,2*d0):
              Body.insert_at_end(Node([seed[0]+i,y],value),i)    
              y += 1
       
       return Body
   
    def Tail(self,d0):
       from Dlist import Node
       from Dlist import DoublyLinkedList
       #tail part
       Tail = DoublyLinkedList()
       value=0.4
       seed=[86,23]
       Tail.insert_at_beg(Node(seed,value),0)
       
       for d in range(1,d0):  #range(1,d0):
           k = d
           for i in range(0,d+1):# range(0,d+1): #np.arange(0,0.5,d+1)
               if i>=10:
                   value=0.3
               else:
                   value=0.4
               if i==d:
                   Tail.insert_at_end(Node([seed[0]+i,seed[1]],value),i)    
                       
               else:
                   for j in [-k,k]:
                       if j<0:
                           Tail.insert_at_beg(Node([seed[0]+i,j+seed[1]],value),i)

                       else:
                           Tail.insert_at_end(Node([seed[0]+i,j+seed[1]],value),i)
                           
                   k = k - 1 
       return Tail
  