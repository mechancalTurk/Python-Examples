####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### NumPy in Python (2-dim) #######
####### B. Ege ########################

import numpy as np
import matplotlib.pyplot as plt

################################ 2-Dimensional NumPy #####################################


a = [[11,12,13],[21,22,23],[31,32,33]]
A = np.array(a)
print("A:",A)
print("A.ndim", A.ndim)
print("A.shape", A.shape)
print("A.size", A.size)
print("A[0][0:2]:", A[0][0:2])
print("A[0:2,2]:", A[0:2,2])
print("Access the element on the first row and first and second columns:", A[0,0:2])
print("\n")

B = np.array([[0,1,1],[1,0,1]])
C = np.array([[1,1],[1,1],[-1,1]])
print("B:", B)
print("C:", C)
z = np.dot(B,C)
print("np.dot(A,B):", z)
a = np.array([[1,0],[0,1]])
b = np.array([[2,1],[1,2]]) 
print("The dot product for [[1,0],[0,1]] and [[2,1],[1,2]]:\n", np.dot(a,b))
print("\n")
print("np.sin(z):", np.sin(z))
print("\n")

# We use the numpy attribute T to calculate the transposed matrix
# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
print("the matrix C:\n",C)
# Get the transposed of C
print("the transposed of C:\n",C.T)

# Perform matrix multiplication with the numpy arrays A and B.
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
# --> because operands could not be broadcast together with shapes (3,4) (4,2)
# we have to use the dot product
print("A:",A)
print("B:",B)
print("np.dot(A,B):",np.dot(A,B))
print("\n")

# Q: What is the Python library used for scientific computing and is a basis for Pandas?
# A: NumPy










