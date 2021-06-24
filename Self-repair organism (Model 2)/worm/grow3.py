"""
@author: Thai Tran
"""

class Grow:
    
    def Head(self,d0):
       from Dlist import Node
       from Dlist import DoublyLinkedList
       #New list of Head
       Head = DoublyLinkedList()
#       Head.insert_at_beg(Node([10,5]),0) 
       sc=[-1,-1]
       if d0>0:
           sc=[10-d0/2,5]
           
       for d in range(1,d0):  #range(1,d0):
           k = d/2.0
           for i in range(0,d+1):# range(0,d+1): #np.arange(0,0.5,d+1)

               if i==d:
                   Head.insert_at_end(Node([10-i,5]),i)    
                   pass
                       
               else:
                   for j in [-k,k]:
                       if j<0:
                           Head.insert_at_beg(Node([10-i,j+5]),i)

                       else:
                           Head.insert_at_end(Node([10-i,j+5]),i)
                           
                   k = k - 0.5       
       return Head, sc        
    
    def Body(self,d0):
       from Dlist import Node
       from Dlist import DoublyLinkedList
       #body part
       Body = DoublyLinkedList()
       Body.insert_at_beg(Node([10,5.0]),0)
       
       for d in range(1,d0):  
         
           for i in range(0,d+1):
               
               if i==d:
                   for j in range(-d,d+1):
                       if Body.search([10+i,j/2.0+5],d0)==-1:
                           Body.insert_at_end(Node([10+i,j/2.0+5]),i)    
                       
               else:
                   for j in [-d,d]:
                       if j<0 and Body.search([10+i, j/2.0 + 5],d0)==-1:
                           Body.insert_at_beg(Node([10+i, j/2.0 + 5]),i)
                           
                       elif Body.search([10+i, j/2.0 + 5],d0)==-1:
                           Body.insert_at_end(Node([10+i, j/2.0 + 5]),i)
                           
       _,data=Body.get_node(0,d0-1)
       y=data[1]
       
       for i in range (d0,3*d0):
          y=data[1]
          for j in range (1,2*d0):
              Body.insert_at_end(Node([10+i,y]),i)    
              y += 0.5
       
       return Body,[10+3*d0/2,5]
   
    def Tail(self,d0):
       from Dlist import Node
       from Dlist import DoublyLinkedList
       #tail part
       Tail = DoublyLinkedList()
       Tail.insert_at_beg(Node([40,5]),0)
       
       for d in range(1,d0):  #range(1,d0):
           k = d/2.0
           for i in range(0,d+1):# range(0,d+1): #np.arange(0,0.5,d+1)

               if i==d:
                   Tail.insert_at_end(Node([40+i,5]),i)    
                       
               else:
                   for j in [-k,k]:
                       if j<0:
                           Tail.insert_at_beg(Node([40+i,j+5]),i)

                       else:
                           Tail.insert_at_end(Node([40+i,j+5]),i)
                           
                   k = k - 0.5  
       return Tail,[40+d0/2,5]
  