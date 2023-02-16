import matplotlib.pyplot as plt
import scipy as s
import numpy as np
import math 
a= np.array([[3, 6], [5, -3]])
b= np.array([[1, 1], [2, 1]])
print(a+b)
print(a.dot(b))
print(np.transpose(a))
print("first coloumn=",a[:,0])
print("first row=",a[0,:])