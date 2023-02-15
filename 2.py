import matplotlib.pyplot as p
import scipy as s
import numpy as np
t=np.arange(0,4*np.pi,0.0001)
y1=np.cos(t)
y2=np.cos(t)*np.cos(5*t)+np.cos(5*t)
fig,a=p.subplots(2)
a[0].plot(t,y1)
a[1].plot(t,y2)
p.show()