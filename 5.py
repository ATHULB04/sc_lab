import matplotlib.pyplot as plt
import scipy as s
import numpy as np
import math 
a=np.arange(0,10,1)
b=np.array(3*a)
plt.scatter(a,[0,1,2,3,4,5,6,7,8,9],color="green",lw=2)
plt.plot(b,ls="--",lw=3)
plt.legend(["x","3*x"])
plt.xlabel("random")
plt.ylabel("values")
plt.show()
