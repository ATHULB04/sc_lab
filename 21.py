#to save a csv file
import numpy as np 
import matplotlib.pyplot as p
t=np.arange(0,0.002, 0.00002)
f=1000
y=2+5*np.sin(2*np.pi*f*t)
np.savetxt("waveform.csv",y,delimiter=",")
p.plot(t,y)
p.show()