import sympy as sym
import numpy as np
t=sym.Symbol("t")
s=3*t**4-40*t**3+126*t**2-9
v=s.diff(t)
deriv= sym.Derivative(v, t)
y=deriv.doit()
for i in range(0,10,2):
    print(v.subs(t,i))
    print(y.subs(t,i))
