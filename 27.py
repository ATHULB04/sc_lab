#rlc circuit
import numpy as np
import matplotlib.pyplot as p
from scipy import integrate
v=5
r=1
l=0.001
c=0.000001
i=v/r
def du_dx(i,t):
    return l*i[1],-r*i[1]-1/c*i[0]
x0=[i,0]
ts=np.linspace(0,15,100)
Is=integrate.odeint(du_dx,x0,ts)
xs=Is[:,0]
p.plot(ts,xs)
p.show()