#transient state
import numpy as np
import matplotlib.pyplot as p
from scipy import integrate
rc=3
r=3
v=3
def di_dt(i,t):
    return -((i/rc)+(5*np.exp(-t))/r)
i=v/r
t=np.linspace(0,20,100)
y=integrate.odeint(di_dt,i,t)
p.plot(t,y)
p.show()

