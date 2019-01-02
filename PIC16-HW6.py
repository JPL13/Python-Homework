class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)
    def __repr(self):
        return str(self.data)
 
import itertools
    
class LinkedList:
    def __init__(self, data):
        self.newnode=Node(data)
        self.first = self.newnode
        self.last = self.newnode
        self.n=1
        self.i=0
        
    def append(self, data2):
         self.newGuy=Node(data2)
         self.last.next=self.newGuy
         self.last=self.newGuy
         self.newGuy.next=self.first #?
         self.n+=1
    
    def __iter__(self):
        for self.i in range( self.n):
            current=self.first
            self.first=self.first.next
            self.i+=1
            yield current
    
    def __str__(self):
        out_str = '['
        for node in self:
            out_str += str(node.data)+'->'
        out_str += ']'
        return (out_str)
        
    def __repr__(self):
        out_str = '\'['
        for node in self:
            out_str += str(node.data)+'->'
        out_str += ']\''
        return str(out_str)
    
    def __len__(self):
        return (self.n) 
    
#    def __getitem__(self, pos):
#        if pos<self.n:
#    def __setitem__(a, b, c)
#        
#        else IndexError:
            
    def __add__(self, other): 
        if type(other) == int:
            print "I am in add len1"
            newGuy=Node(other)
            self.last.next=newGuy
        else:
            self.append(other)
            

        
    def __setitem__(self, index, v):
        current = self.first
        count=0
        if index >= self.n or (index)<0: 
            print "Index out of range"
            raise
        else:
            while count<index:
                current=current.next
                count+=1
            current.data=v
    
    def __getitem__(self,index):
#        if isinstance(index, slice):
#            result = LinkedList()
#            for i in self._iterslice(1:index):
#                result.append(i.item)
#            return result
#            
#        else:
        current = self.first
        count=0
        if index >= self.n or index<0: 
            print "Index out of range"
            raise
        else:
            while count<index:
                current=current.next
                count+=1
            return current
     
    def __iadd__(self, other):   
        self.append(other)
        return self

    extend = __iadd__
#     
#    def next(self):
#        if self.i<self.n:
#            current=self.first
#            self.first=self.first.next
#            self.i+=1
#            return current
#        else:
#            self.i=0
#            raise StopIteration()
#     
a = LinkedList(0);
a.append(1)
a.append(2)

print "40 points if this works"
for n in a:
    print n

print ""

print "10 points if this works"
for n in a:
    print n
    
print ""
    
print "15 points if both of these work"
for n in a:
    if n.data == 2: # if you wrote your code for n.data == 2, that's OK too
        break
    else:
        print n
 
print ""
       
for n in a:
    if n.data == 2: 
        break
    else:
        print n

print ""

a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)

print ""

print "5 points each"
print len(a)
print str(a)
print repr(a)

print ""

print "5 points each. That is, 10 points if the output of the next line is correct"
a[5] = 20
print a[5]

print ""

print "10 points for correct operation of +"
a+9 # doesn't modify a
print a

print ""

a = a + 9 # appends 9 to a
print a
    
print ""

#print "10 bonus points if all the following work"
#print a[1:5]
#print a[1:]
#print a[:5]
#print a[1::2]
#print a[::]