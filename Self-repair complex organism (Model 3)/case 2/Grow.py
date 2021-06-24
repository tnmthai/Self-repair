"""
@author: Thai Tran
"""

class Grow:
    
    def Worm(self,d0):
       from Dlist import Node
       from Dlist import DoublyLinkedList
       
       #New list of Head
       Worm = DoublyLinkedList()
       
       value=0.7
       seed=[22,23]
       s=seed[0]
       Worm.insert_at_beg(Node(seed,value),s) 
           
       for d in range(1,d0):  #range(1,d0):
           k = d
           
           for i in range(0,d+1):# range(0,d+1): #np.arange(0,0.5,d+1)
               
               if i <10:
                   value=0.7
               else: value=0.8    
                   
               if i==d:
                   Worm.insert_at_end(Node([seed[0]-i,seed[1]],value),s-i)    

               else:
                   for j in [-k,k]:
                       if j<0:
                           Worm.insert_at_beg(Node([seed[0]-i,j+seed[1]],value),s-i)

                       else:
                           Worm.insert_at_end(Node([seed[0]-i,j+seed[1]],value),s-i)
     
                   k = k - 1       
       
    
### body
       value=0.6
       seed=[23,23]
       s=seed[0]

       Worm.insert_at_beg(Node(seed,value),s)
       
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
                       if Worm.search([seed[0]+i,j+seed[1]],d0)==-1:
                           Worm.insert_at_end(Node([seed[0]+i,j+seed[1]],value),s+i)    
                       
               else:
                   for j in [-d,d]:
                       if j<0 and Worm.search([seed[0]+i, j + seed[1]],d0)==-1:
                           Worm.insert_at_beg(Node([seed[0]+i, j + seed[1]],value),s+i)
                           
                       elif Worm.search([seed[0]+i, j + seed[1]],d0)==-1:
                           Worm.insert_at_end(Node([seed[0]+i, j + seed[1]],value),s+i)
                           
       _,data=Worm.get_node(0,s)
       y=data[1]
       value=0.55
       for i in range (s,3*d0-9):
          y=data[1]
          if i<40:
              value=0.55
          else:
              value=0.5
          for j in range (1,2*d0):
              Worm.insert_at_end(Node([s+i,y],value),s+i)    
              y += 1
       
### Tail       
   
    
       value=0.4
       seed=[83,23]
       s=seed[0]
       Worm.insert_at_beg(Node(seed,value),s)
       
       for d in range(1,d0):  #range(1,d0):
           k = d
           for i in range(0,d+1):# range(0,d+1): #np.arange(0,0.5,d+1)
               if i>=10:
                   value=0.3
               else:
                   value=0.4
               if i==d:
                   Worm.insert_at_end(Node([seed[0]+i,seed[1]],value),s+i)    
                       
               else:
                   for j in [-k,k]:
                       if j<0:
                           Worm.insert_at_beg(Node([seed[0]+i,j+seed[1]],value),s+i)

                       else:
                           Worm.insert_at_end(Node([seed[0]+i,j+seed[1]],value),s+i)
                           
                   k = k - 1 
       return Worm
  