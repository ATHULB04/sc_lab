#half wave rectifier
import matplotlib.pyplot as plt
import scipy as s
import numpy as np
import math 

x = np.arange(0,4*np.pi,0.01)
z = s.signal.sawtooth(x-np.pi)
y=np.abs(z)
k=(z+y)/2
plt.plot(x,k)
plt.show()