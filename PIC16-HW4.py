#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 20:30:33 2018

@author: AppleMoony
"""
# my_divide1 = [x/flote(y) for x, y in zip(a,b) ]

import numbers    
import time
def my_divide2(a, b):
    quotient=[]
    begin=time.clock()

    for ai, bi in zip(a, b):
        if (isinstance(ai, numbers.Number) and isinstance(bi, numbers.Number) and bi != 0):
            quotient.append(ai/float(bi))
        else:
            print "Something is wrong. Can't perform division"
            
    end=time.clock()
    print end-begin


def my_divide3(a, b):
    quotient=[]
    begin=time.clock()
    for ai, bi in zip(a, b):
        try:
            quotient.append(ai/float(bi))
        except: 
            print 'Something went wrong'          
    end=time.clock()
    print end-begin

def my_divide4(a, b):
    quotient=[]
    begin=time.clock()
    for ai, bi in zip(a, b):
        try:
            quotient.append(float(ai)/bi)
        except TypeError:
            print 'Non-numeric  data  detected'
        except ZeroDivisionError:
            print 'There  is  a  zero  in  b'
        except:
            print 'Something went wrong'
            
    end=time.clock()
    print end-begin


a  =  range(0,1000000);  b  =  range(1,1000001)
print '1: '     
my_divide2(a, b)
my_divide3(a, b)     

a  =  range(0,1000000);  b  =  range(1,1000000)+  [0]
print '2: '    
my_divide2(a, b)
my_divide3(a, b)
my_divide4(a, b)  

a  =  range(0,1000000);  b  =  range(1,1000000)+  ['a']
print '3: '    
my_divide2(a, b)
my_divide3(a, b)
my_divide4(a, b)  