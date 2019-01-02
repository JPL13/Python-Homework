#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:19:59 2018

@author: AppleMoony
"""

#If  there  is  a  single  numerical  argument  (assumed  to  be  an  integer),  
#the  MathVector should  represent  a  zero  vector  (vector  of  all  zero  components)
# of  the  specified  number  of  dimensionson
# If  there  is  a  single  list  or  tuple
# argument or  if  there  are  multiple  arguments  (assumed  to  be  numerical),  
#the  MathVectorshould  represent  a  vector  with  the  specified  (Cartesian)  components.o

class MathVector:
    def __init__(self, *args):
        if len(args)==1 and isinstance(args[0], int):
            #print args
            self.x_list=[0 for x in range(args[0])]
            self.n=args[0]
        
        elif len(args)==1 and isinstance(args, tuple):
           # print '2', args
            self.x_list= list(args[0])
            self.n=len(args[0])
        else:
#            print '3', args
#            print 'length', len(args)
#            print 'type', type(args)
            self.x_list= list(args)
            self.n=len(args)
            
        
    def get_el(self, i): 
        #returns  the  i-th  component  of  the  vector
        return self.x_list[i-1]
    
    def neg(self):
    #returns  the  negative  of  the  original  vector(leaving  the  original  unchanged)
        new_list=[-x for x in self.x_list]
        return MathVector(new_list)
    
    def mag(self):
    #returns  the  magnitude  of  the  vector   
        return sum([x**2 for x in self.x_list])**0.5
  
    def dot(self, other):
    #dot–returns  the  dot  product  of  the  vector  and  another  vectoro
        return sum([x*y for x, y in zip(self.x_list, other.x_list)])
        
    def plus(self, other):
        #simplify
        new_a=[]
        for i in range(self.n):
            new_a.append(self.x_list[i]+other.x_list[i])
        return MathVector(new_a)
        
    def sp(self, scalar):
    #sp–returns  the  product  of  the  vector  and  a  scalar  (“scalar  product”)
        #self.x_list=[scalar * x for x in self.x_list ]
        return MathVector([scalar * x for x in self.x_list ])
    
    def print_me(self):
    #print_me–prints  a  representation  of  the  vectorto  the  consolelike  “[1,  0,  0]”
        print str(self.x_list)
   
    def __str__(self):
        return str(self.x_list)
        
    def __getitem__(self, i):
        return self.get_el(i)
    
    def __neg__(self):
        return self.neg()
    
    def __abs__(self):
        return self.mag()
        
    
    def __add__(self, other):
        return self.plus(other)
    
    def __mul__(self, other):
        
        if isinstance(other, int):
         
            return self.sp(other)
 
               
        else:

            return self.dot(other)
   
    __rmul__=__mul__

        
        
        
    
    
u = MathVector(5)
print "u =",
u.print_me()
 
v = MathVector([2,3,6])
print "v =",
v.print_me()
 
w = MathVector(1,2,3)
print "w =",
w.print_me()
 
print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()
# 

print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v