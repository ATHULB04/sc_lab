import numpy as np
import matplotlib.pyplot as p
t=np.linspace(0,2*np.pi,180)
y=np.sin(t)
print(y)
# y1=np.gradient(y,2*np.pi/180)
y1=np.deri
p.plot(t,y)
p.plot(t,y1)
p.show()
