#odinary differential equation
import numpy as np
import matplotlib.pyplot as p
from scipy import integrate
def fun(x,t):
    return -2*x
x0=1
t=np.linspace(0,10,1000)
y=integrate.odeint(fun,x0,t)
p.plot(t,y)
p.show()