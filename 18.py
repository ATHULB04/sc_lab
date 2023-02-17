import matplotlib.pyplot as p
import scipy as s
import numpy as np
m=1
for n in range(1,10):
    y=((-1)**n)*(1/(2*n+1))
    m+=y
    print(4*(m))
