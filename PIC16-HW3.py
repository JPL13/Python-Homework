#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 19:38:50 2018

@author: AppleMoony
"""

def  f(x):  
    return  x**2
x  =  range(10000000)
y  =  []

import time
begin  = time.clock()#  record  start  time#  
for  i  in  x:

    y.append(f(i))
    
end  = time.clock()#  record  end  time
print 'f function: ' +str(end-begin)

g=lambda x: x**2

# Then,  write  additional  code  to  time  the  execution  of  forloops  
#that  do  the  same  job,  except  in  one  case  use  g and  in  the  other  case 
#do  not  use  g or  f  (just  write  out  the  **2 operation  inside  the  loop).
z  =  []
begin  = time.clock()#  record  start  time#  
for  i  in  x:
    z.append(g(i)) 
end  = time.clock()#  record  end  time
print 'lambda function: ' +str(end-begin)

h= []
begin  = time.clock()#  record  start  time#  
for  i  in  x:
    h.append(i**2)   
end  = time.clock()#  record  end  time
print 'no function: ' +str(end-begin)


#Rather  than  appending  to  the  list  y,  first  initialize  y to  range(N)
#then  square  the  elements  in-place.  
#That  is,  is  it  more  efficient  to  re-use  an  existing  list  (if  possible)?
y=range(1000000)
begin  = time.clock()#  record  start  time#  
for i in y:
    y[i]=i**2

end  = time.clock()#  record  end  time
print 're-use list: ' +str(end-begin)

#Use  list  comprehension  to  generate  the  list  of  squares
begin  = time.clock()#  record  start  time#  
[f(i) for i in x]
end  = time.clock()#  record  end  time
print 'list comprehension: ' +str(end-begin)

# Use  map to  generate  the  list  of  squares
begin  = time.clock()#  record  start  time#  
map(f, x)
end  = time.clock()#  record  end  time
print 'MAP: ' +str(end-begin)
