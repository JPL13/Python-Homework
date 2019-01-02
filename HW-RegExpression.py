#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:07:02 2018

@author: AppleMoony
"""

import csv
import re
with open("data.csv", "rb") as f:
    r=csv.reader(f)
    t=[]
    for row in r:
        t.append(row)
    #print t[0][0], "\t\t", t[0][1]
    
    t[0]=["First", "M.I.", "Last", "Phone"]
    
    first=""
    middle=""
    last=""
    phone=""
    
    table=[]  
    table.append(t[0])
    for row in t[1: ]:
        
        if ',' in row[0]:
            regex = r"([a-zA-Z]{3,30}), ([a-zA-Z]{3,30}\s*)+\s*([a-zA-Z\.]*)"
            match = re.search(regex, row[0])
            
            last=match.group(1)
            first=match.group(2)
            middle=match.group(3)
            
            #print last            
            #print first
            #print middle
        
        if not ',' in row[0]:   
            regex = r"([-'a-zA-Z]{3,30})\s?([A-Za-z]?\.?)\s([-'a-zA-Z]{3,30})"
            match = re.search(regex, row[0])
            
            first=match.group(1)
            middle=match.group(2)
            last=match.group(3)
            
        if len(row[1])<9:
            phone=None
        else:    
            regex = r"\d?-?\(?(\d{3})\)?[\s\.-]?(\d{3})[\s\.-]?(\d{4})"
            match2 = re.search(regex, row[1])
#            print match.group(1)
#            print match.group(2)
#            print match.group(3)
#       
        
            if not match2.group(1) is None:
                phone="(" + str(match2.group(1))+ ")"+str(match2.group(2))+"-"+str(match2.group(3))
            else:
                phone=None
        
        if not phone is None:
            #row=[first, middle, last, phone]
            row=[]
            row.append(first)
            row.append(middle)
            row.append(last)
            row.append(phone)
            
            print row
            
            table.append(row)
    
        
        
    with open("data2.csv", "wb") as f:
        w=csv.writer(f, delimiter=",")
        for row in table:
            print row
            w.writerow(row)