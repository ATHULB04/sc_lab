import matplotlib.pyplot as p
import scipy as s
import numpy 
v1=numpy.array([ 1, 3, 5, 7])
v2=numpy.array([2, 4, 6, 8])
# Classic comuting
v3 = numpy.zeros(5)
for i in range(len(v2)):
    v3[i] = v1[i]+v2[i]
print(v3)

# Vectorized computing
v4=v1+v2
print(v4)