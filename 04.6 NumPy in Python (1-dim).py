####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### NumPy in Python (1-dim) #######
####### B. Ege ################

# In this lesson we will be covering numpy in 1D, in particular ND arrays. 
# Numpy is a library for scientific computing. It has many useful functions. 
# There are many other advantages like speed and memory. 
# Numpy is also the basis for pandas. 

import numpy as np
import matplotlib.pyplot as plt

print("\n")
# Checking NumPy Version
print("NumPy version:", np.__version__) 
# to upgrade
# C:\Users\boert\AppData\Local\Programs\Python\Python39>python.exe -m pip install --upgrade pip
print("\n")

################## 1-Dimensional NumPy ####################

a = np.array([0,1,2,3,4])
print("the array a:",a)
print("size of the array a:", a.size)
print("dimension of the array a:", a.ndim)
# The attribute shape is a tuple of integers indicating the size of the array in each dimension:
print("shape of the array a:", a.shape)
print("type of the array a:", type(a))
print("dtype of the array a:", a.dtype)
print("\n")

# We can also create numpy array with real numbers
b = np.array([3.1, 11.02,6.2,213.2,5.2])
print("the array b:",b)
print("size of the array b:", b.size)
print("dimension of the array b:", b.ndim)
# The attribute shape is a tuple of integers indicating the size of the array in each dimension:
print("shape of the array b:", b.shape)
print("type of the array b:", type(b))
print("dtype of the array b:", b.dtype)
print("\n")

########### INDEXING AND SLICING ###############
print("########### INDEXING AND SLICING ###############")
c = np.array([20,1,2,3,4])
print("the array c:",c)
c[0] = 100
print("the array c after the first element changed:",c)
print("select the elements from 1 to 3 by slicing c[1:4]:",c[1:4])
c[3:5] = 300,400
print("changing the 4. and 5. elements by slicing c[3:5] = 300,400:",c)
print("\n")

# We can also define the steps in slicing, like this: [start_pos:end_pos:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("arr:", arr)
print("arr[1:5:2]:", arr[1:5:2])
print("arr[1:7:2]:", arr[1:7:2])
print("arr[0:7:3]:", arr[0:7:3])
print("arr[:4]:", arr[:4])
print("arr[4:]:", arr[4:])
print("arr[1:5:]:", arr[1:5:])
print("\n")

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("arr2:", arr2)
print("the even elements in the given array:", arr2[1:8:2])
print("\n")

############### Assign Value with List ###########
print("############### Assign Value with List ###########")
arr3 = np.array([100, 1, 2, 3, 0])
select = [0, 2, 3, 4]
arr4 = arr3[select]
print("arr3[select]:",arr4)
print("\n")


################  BASIC OPERATIONS ###############

########### Vector Addition ans Substraction  ############ 
print("########### Array Addition, Subtraction, Multiplication and Division  ############ ")

# Iterating 1-D Arrays
# If we iterate on a 1-D array it will go through each element one by one
# If we execute the numpy array, we get in the array format 
# arr1 = np.array([1, 2, 3])
# print(arr1)
# But if you want to result in the form of the list, then you can use for loop:
# for x in arr1:
# print(x)


# Array Addition
u = np.array([1,0])
v = np.array([0,1])
z = u + v
# OR
z = np.add(u,v)
print("the addition of two vectors [1,0]+[0,1]:", z)
# OR
z = []
for m, n in zip(u,v):
    z.append(m+n)
print("now, the addition of multiple vectors by a for-loop:", z)
print("\n")


# Array Subtraction
u = np.array([1,0])
v = np.array([0,1])
z = u - v
# OR
z = np.subtract(u,v)
print("the subtraction of two vectors [1,0]-[0,1]:", z)
# OR
z = []
for m, n in zip(u,v):
    z.append(m-n)
print("now, the subtraction of multiple vectors by a for-loop:", z)
print("\n")


# Arry Multiplication
# How would you multiply each element in the numpy array by 2?
print("Wrong: Multiplying an array in this form is a str-operation: 2*[1,0]:", 2*[1,0])
print("Right: Multiplying an array u = np.array([1,0]) with 2:", 2*u)
z = np.multiply(u,v)
print("multiplying the arrays u[1,0]*v[0,1]:",z)
# OR
z = []
for n in u:
    z.append(2*n)
print("Right: Now, multiplying the array u by a for-loop", 2*u)
print("\n")

# Array Division
a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
print ("np.divide(a,b):", np.divide(a,b))

# Product of two numpy arrays
u = np.array([1,2])
v = np.array([3,2])
z = u*v
print("the product of u*v:", z)
# OR
z = []
for m, n in zip(u,v):
    z.append(m*n)
print("the product of u*v by a for-loop:", z)
print("\n")

# Dot Product (Skalarprodukt)
u = np.array([1,2])
v = np.array([3,1])
print("Skalarprodukt von [1,2] and [3,2]:", np.dot(u,v))
print("\n")

# Adding constant to an numpy array
u = np.array([1,2,3,-1])
z = u+1
print ("adding constant to an numpy array [1,2,3,-1]:", z)
print("\n")

# Universal Functions

# Get the mean of numpy array
a = np.array([1,-1,1,-1])
print("the mean value for [1,-1,1,-1]:",a.mean())
b = np.array([1,-2,3,4,5])
print("the max value for [1,-2,3,4,5]:",b.max())
print("the min value for [1,-2,3,4,5]:",b.min())
print("Find the sum of maximum and minimum value in the given numpy array:", b.min() + b.max())
print("\n")

# Get the standard deviation of numpy array
standard_deviation_a = a.std()
standard_deviation_b = b.std()
print("standard deviation for np.array([1,-1,1,-1]):", standard_deviation_a)
print("standard deviation for np.array([1,-2,3,4,5]):", standard_deviation_b)
print("\n")

# Creating new array values
print("Creating new array values")
print("np.pi:",np.pi)
x = np.array([0,np.pi/2, np.pi])
print("x:",x)
y = np.sin(x)
print("np.sin(x):",y)
print("\n")

# linspace
# A useful function for plotting mathematical functions is linspace. 
# Linspace returns evenly spaced numbers over a specified interval.
# numpy.linspace(start, stop, num = int value)
# start : start of interval range
# stop : end of interval range
# num : Number of samples to generate.

print("np.linspace(-2,2,num=5):", np.linspace(-2,2,num=5))
print("np.linspace(-2,2,num=9):", np.linspace(-2,2,num=9))
print("np.linspace(-3,3,num=3):", np.linspace(-3,3,num=3))
print("np.linspace(5,4,num=6):", np.linspace(5,4,num=6))
print("\n")

# Plotting Mathematical Functions (works only in Jupyter)
# x = np.linspace(0,2*np.pi,100)
# y = np.sin(x)
# As we are using a Jupiter notebook, we use the command matplotlib inline to display the plot:
#%matplotlib inline (bu gercekten kullanilmak zorunda degil gibi)
# plt.plot(x,y) # Sekli ciziyor
# print("\n")

#import time 
#import sys
#import numpy as np 

'''
import matplotlib.pyplot as plt
%matplotlib inline  

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
'''

# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot the arrays as vectors 
# using the fuction Plotvec2 and find their dot product:
a = np.array([-1,1])
b = np.array([1,1])
#Plotvec2(a,b)  # works only in Jupyter
print("The dot product for [-1,1] and [1,1]:", np.dot(a,b))

a = np.array([1,0])
b = np.array([0,1])
#Plotvec2(a,b)  # works only in Jupyter
print("The dot product for [1,0] and [0,1]:", np.dot(a,b))

a = np.array([0,1])
b = np.array([1,0])
#Plotvec2(a,b)  # works only in Jupyter
print("The dot product for [0,1] and [1,0]:", np.dot(a,b))
a = np.array([2,-1])
b = np.array([3,4])
#Plotvec2(a,b)  # works only in Jupyter
print("The dot product for [2,-1] and [3,4]:", np.dot(a,b))
a = np.array([1,3,-5])
b = np.array([4,-2,-1])
#Plotvec2(a,b)  # works only in Jupyter
print("The dot product for [1,3,-5] and [4,-2,-1]:", np.dot(a,b))
# Using the component formula for the dot product of three-dimensional vectors
# a=(a1,a2,a3), # b=(b1,b2,b3)
# dot(a,b)=a1b1+a2b2+a3b3
# https://mathinsight.org/dot_product_examples
print("\n")

# Now, the following question:
# Why are the results of the dot product for [-1, 1] and [1, 1] 
# and the dot product for [1, 0] and [0, 1] zero, 
# but not zero for the dot product for [1, 1] and [0, 1]?
# Answer: 
# Because the vectors used for the questions 4 and 5 are perpendicular (they have 90° angle)
# The vectors used for question 4 and 5 are perpendicular. As a result, the dot product is zero.


# Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2. 
# Then find the even and odd numbers from arr1 and arr2.

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print("arr1:", arr1)
print("arr2:", arr2)

# starting index!
even_arr1 = arr1[1:5:2] #even numbers
odd_arr1 = arr1[0:5:2] #odd numbers
even_arr2 = arr2[0:5:2] #even numbers
odd_arr2 = arr2[1:5:2] # odd numbers
print("even_arr1:",even_arr1)
print("odd_arr1:",odd_arr1)
print("even_arr2:",even_arr2)
print("odd_arr2:",odd_arr2)


