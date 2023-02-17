import numpy as np
import matplotlib.pyplot as p
from scipy import integrate
def du_dx(u,t):
    return u[1],-4*u[1]-2*u[0]+(np.exp(-t)*np.cos(t))
x0=[0,0]
ts=np.linspace(0,10,100)
us=integrate.odeint(du_dx,x0,ts)
xs=us[:,0]
p.plot(ts,xs)
p.show()