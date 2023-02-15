#arange&linspace
import matplotlib.pyplot as p
import scipy as s
import numpy as np
m=np.arange(0,10,0.1)#increment 0 by 0.1
fig, axs = p.subplots(3)
print(m)
x=np.sin(m)
axs[0].plot(m,x)
n=np.linspace(0,10,100)#divide 0-10 into 100 points
print(n)
y=np.cos(n)
axs[1].scatter(n,y)
axs[2].bar(n,2*n+3)
p.show()