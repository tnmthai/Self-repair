"""
@author: Thai Tran
@Date: 06-04-2019
"""    
    
class Main:
        
    def worm(self,d0):
       from sleepdots import sleep        
       from Dlist import Node       
       from loaddata import data      
       from Grow import Grow       
       import matplotlib.pyplot as plt  
       import numpy as np
       from Algorithms import automata
       from Algorithms import NN
       from Algorithms import DT
       from entropy import entropy
       #New worm
       Worm = Grow()
       Head,mid1=Worm.Head(d0) 
       Body,mid2=Worm.Body(d0)
       Tail,mid3=Worm.Tail(d0)
#stem cells list 
       stemcells=[]
       stemcells.append(mid1)
       stemcells.append(mid2)
       stemcells.append(mid3)
# =============================================================================
#Load data 
       Htissue=Head.extractdata(d0)
       Btissue=Body.extractdata(3*d0)
       Ttissue=Tail.extractdata(d0)
# Normal entropy       
       Ehead= entropy(Htissue,mid1)
       Ebody= entropy(Btissue,mid2)
       Etail= entropy(Ttissue,mid3)
       M1=automata()
# =============================================================================       
       print(' Menu')
       print('- Normal worm (1)')
       print('- Damage:')
       print('     Damage case 1  (2)') 
       print('     Damage case 2a (3)') 
       print('     Damage case 2b (4)') 
       print('     Damage case 3a (5)') 
       print('     Damage case 3b (6)')
       print('- Quit (0)')
       
       while True:
           print('***************************************************')
           do = input('What would you like to do? ')
        
             
           if do == 1:
               x,y=data(Htissue,Btissue,Ttissue)
               plt.scatter(x, y)    
               print  'Total cells: ',(len(x))
               x=[]
               y=[]
               for s in stemcells:
                   if s[0]!=-1 and s[1]!=-1:
                       x.append(s[0])
                       y.append(s[1])
               plt.scatter(x, y,c='r')
               plt.show()
               
           elif do==2:# Case 1: head damage a part    
                              
               try:
                   
                   Head.damagecase1(d0)
                   Htissue=Head.extractdata(d0)
                   NEhead=entropy(Htissue,mid1)                  
                   NEbody= entropy(Btissue,mid2)
                   NEtail= entropy(Ttissue,mid3)    

                   raise Exception('Damage detected!!!')
               except Exception as err:
                   print err
                   ## damage detect             
                   
                   print 'Checking stem cells...'
                   r1=M1.Switch(M1.head(mid1,mid2,mid3),1)
                   print 'Head detects',r1,' (missing).'
                   r2=M1.Switch(M1.body(mid1,mid2,mid3),2)
                   print 'Body detects',r2,' (missing).'
                   r3=M1.Switch(M1.tail(mid1,mid2,mid3),3)
                   print 'Tail detects',r3,' (missing).'
                   print '***************************'
                   
                   if r1=='Normal' or r2=='Normal' or r3=='Normal':
                       #Entropy: detect damage region
                       print 'Checking entropy...'
                       p=-1
                       for i in range (0,4):
                           if Ehead[i]!=NEhead[i]:
                               p=i
                               print 'Head damage area:',p
                       if p>=0:
                           x,y=data(Htissue,Btissue,Ttissue)
                           plt.scatter(x, y) 
                                               #draw stem cells     
                           x=[]
                           y=[]
                           for s in stemcells:
                               x.append(s[0])
                               y.append(s[1])
                           plt.scatter(x, y, c='red')
                           level,Dlist=Head.Detectcase1(d0,p)   
                           print Dlist,'Dlist'
                           x=[]
                           y=[]
                           for t in Dlist:
                               x.append(t[0])
                               y.append(t[1])
                           plt.scatter(x, y)
                           plt.show()

                       p=-1
                       for i in range (0,4):
                           if Ebody[i]!=NEbody[i]:
                               p=i
                               print 'Body damage area:',p        
                      
                       p=-1
                       for i in range (0,4):
                           if Etail[i]!=NEtail[i]:
                               p=i
                               print 'Tail damage area:',p
               
               #repair
       
                       minx,miny=Dlist[0]
                       maxx,maxy=Dlist[len(Dlist)-1]
                       
                       while minx >= 0:
                           for y in np.arange (miny, maxy+0.5,0.5):
                               Head.insert_at_end(Node([minx-1,y]),11-minx)
                
                           minx = minx - 1
                           miny= miny + 0.5
                           maxy = maxy -0.5
                          
#draw waorm after repaired Fig 4   
                       
                       sleep() # for fun :)
                       Htissue=Head.extractdata(d0)
                       x,y=data(Htissue,Btissue,Ttissue)
                       plt.scatter(x, y)     
                           
                    #draw stem cells     
                       x=[]
                       y=[]
                       for s in stemcells:
                           x.append(s[0])
                           y.append(s[1])
                       plt.scatter(x, y, c='red')
                       
                       plt.show()
           elif do==3:# Case 1: head damage a part    
               pass               
#               try:
#                   
#                   Btissue=[]
#                   mid2=[-1,-1]
#                   stemcells[1]=mid2
#                   Ttissue=[]
#                   mid3=[-1,-1]
#                   stemcells[2]=mid3   
#
#                   raise Exception('Damage detected!!!')
#               except Exception as err:
#                   print err
#                   ## damage detect             
#                   
#                   print 'Checking stem cells...'
#                   r1=M1.Switch(M1.head(mid1,mid2,mid3),1)
#                   print 'Head detects',r1,' (missing).'
#                   r2=M1.Switch(M1.body(mid1,mid2,mid3),2)
#                   print 'Body detects',r2,' (missing).'
#                   r3=M1.Switch(M1.tail(mid1,mid2,mid3),3)
#                   print 'Tail detects',r3,' (missing).'
#                   print '***************************'


                    
           elif do==4:
               try:
                   Htissue=[]
                   mid1=[-1,-1]
                   stemcells[0]=[-1,-1]
                   Btissue=Body.extractdata(3*d0)
                   Ttissue=Tail.extractdata(d0)
                   raise Exception('Damage detected!!!')
               except Exception as err:
                   print err
                   ## damage detect             
                   
                   print 'Checking stem cells...'
                   r1=M1.Switch(M1.head(mid1,mid2,mid3),1)
                   print 'Head detects',r1,' (missing).'
                   r2=M1.Switch(M1.body(mid1,mid2,mid3),2)
                   print 'Body detects',r2,' (missing).'
                   r3=M1.Switch(M1.tail(mid1,mid2,mid3),3)
                   print 'Tail detects',r3,' (missing).'
                   print '***************************'
                   if r1=='Both' or r2=='Head' or r3=='Head':
                       
                       x,y=data(Htissue,Btissue,Ttissue)
                       plt.scatter(x, y)     
                       
                    
                        #draw stem cells     
                       x=[]
                       y=[]
                       for s in stemcells:
                           if s[0]!=-1 and s[1]!=-1:
                               x.append(s[0])
                               y.append(s[1])
                       plt.scatter(x, y, c='red')
                       plt.show()
                       
                       
                       sleep()
                       Head,mid1=Worm.Head(5)
                       stemcells[0]=mid1
                       Htissue=Head.extractdata(5)
                
                       x,y=data(Htissue,Btissue,Ttissue)
                       plt.scatter(x, y)     
                       
                    
                        #draw stem cells     
                       x=[]
                       y=[]
                       for s in stemcells:
                           if s[0]!=-1 and s[1]!=-1:
                               x.append(s[0])
                               y.append(s[1])
                       plt.scatter(x, y, c='red')
                       plt.show()
                       sleep()
                       Head,mid1=Worm.Head(d0)
                       stemcells[0]=mid1
                       Htissue=Head.extractdata(d0)
                
                       x,y=data(Htissue,Btissue,Ttissue)
                       plt.scatter(x, y)     
                       
                    
                        #draw stem cells     
                       x=[]
                       y=[]
                       for s in stemcells:
                           if s[0]!=-1 and s[1]!=-1:
                               x.append(s[0])
                               y.append(s[1])
                       plt.scatter(x, y, c='red')
                       plt.show()
                       
                       
                       
                       
                    
           elif do == 6:#'2. Make damage'
               #   Make damage
               try:
                   Body.damagecase3b(3*d0)
                   stemcells[1]=[-1,-1]
                   mid2=[-1,-1]
                   Btissue=Body.extractdata(3*d0)
                   raise Exception('Damage detected!!!')
               except Exception as err:
                   print err
                   ## =============================================================================
            #draw damage worm Fig 2       
                   x,y=data(Htissue,Btissue,Ttissue)
#                   print 'After damage, total cells: ',len(x)
                   plt.scatter(x, y)  

         ## damage detect             
                   
                   print 'Checking stem cells...'
                   r1=M1.Switch(M1.head(mid1,mid2,mid3),1)
                   print 'Head detects',r1,' (missing).'
                   r2=M1.Switch(M1.body(mid1,mid2,mid3),2)
                   print 'Body detects',r2,' (missing).'
                   r3=M1.Switch(M1.tail(mid1,mid2,mid3),3)
                   print 'Tail detects',r3,' (missing).'
                   print '***************************'
         ##Identify border      
                   if r1=='Body':
                       print 'Start to repair body damage...'
                       Body.updateUD(3*d0)
                       Dlist = Body.detect3b(3*d0)
                       
                       x=[]
                       y=[]
                       for s in Dlist:           
                           x.append(s[0])
                           y.append(s[1])
                       plt.scatter(x, y)
                       x=[]
                       y=[]
                       for s in stemcells:
                           if s[0]!=-1 and s[1]!=-1:
                               x.append(s[0])
                               y.append(s[1])
                       plt.scatter(x, y,c='r')
                       plt.show() 
                       sleep() # for fun :)
                       ##repair
                       for d in Dlist:
                           
                           idx,lv = Body.search(d,3*d0)
                           
                           d1=d[1]+0.5           
                           i=1
                           while i<10:
                               ref,dat = Body.get_node(idx+1,lv)
                                                 
                               if dat[1] != d1:
                                   ref,_ = Body.get_node(idx,lv)
                                   Body.insert_after(ref,Node([dat[0],d1]),lv)
                                   d1 += 0.5
                                   idx += 1
                                   i +=1
                               else:
                                   break
                               
                                
                       Btissue=Body.extractdata(3*d0)    
                       x,y=data(Htissue,Btissue,Ttissue)
                       print '\nAfter regeneration, total cells: ', len(x)
                       plt.scatter(x, y)
                       stemcells[1]=[25,5]
                       x=[]
                       y=[]
                       for s in stemcells:
                           if s[0]!=-1 and s[1]!=-1:
                               x.append(s[0])
                               y.append(s[1])
                       plt.scatter(x, y,c='r')
                       plt.show()
                   else:
                       pass
           elif do == 0:
               break
## =============================================================================
       
s=Main()
s.worm(10)
        
