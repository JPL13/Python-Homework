#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 12:25:42 2018

@author: AppleMoony
"""
import string
str='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
words=string.split(str)

#method 1
dict={i:words.count(i) for i in set(words)}
print dict['dolore']
print len(dict)

#method 2
#initialize the dictionary
dictionary={i: 0 for i in set(words)}
for word in words:
    dictionary[word] += 1
print dictionary['dolore']  
print len(dictionary)

import time


f = open('gutenberg.txt')
text=f.read()
text_words=string.split(text)

#method 2
begin=time.clock()
book_dct={i: 0 for i in set(text_words)}
for word in text_words:
    book_dct[word] += 1
end=time.clock()
print  end-begin
print book_dct['found'] 


#method 1
begin=time.clock()
dict1={i:words.count(i) for i in set(text_words)}
end=time.clock()
print  end-begin
print book_dct['found'] 