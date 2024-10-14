

name = "Lizz"
print(name[0:2])
print("\n")

var = "01234567"
print(var[::2])
print("\n")

def add(x):
    return(x+x)

result = add(2)
print(result)
result = add('2')
print(result)
print("\n")

A=['1','2','3'] 
for a in A: 
  print(2*a)
print("\n")

A=[1,2,3] 
for a in A: 
  print(2*a)
print("\n")

for i in range(1,5): 
   if (i!=1): print(i)
print("\n")

class Rectangle(object):
        def __init__(self,width=2,height =3,color='r'):
                                  self.height=height
                                  self.width=width
                                  self.color=color
        def drawRectangle(self):
                       import matplotlib.pyplot as plt
                       plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc=self.color))
                       plt.axis('scaled')
                       plt.show()

# What is the height of the rectangle in the class Rectangle?
# 3
                       

import numpy as np

a=np.array([0,1,0,1,0]) 
b=np.array([1,0,1,0,1]) 
print(a+b) 

a=np.array([1,1,1,1,1]) 
print(a+10)

# In Python what can be either a positive or negative number but does not contain a decimal point?
# int

# What is a tuple?
# A collection that is ordered and unchangeable

# Whatdata type must have unique keys?
# Dictionary

# What is the result of the following operation: '1:2,3:4'.split(':')?
# ['1','2,3','4']

# What happens with this segment of code: a=set(A) ?
# It casts the list "A" to the set "a"

# What is an error that occurs during the execution of code?
# Exception

# What method organizes the elements in a given list in a specific descending or ascending order?
# sort()
