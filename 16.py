# import scipy
# from numpy import exp
# import numpy as np
# # def f(x):
#     # return 4*x**2+3
# f=lambda x:np.exp(x)
# i = scipy.integrate.quad(f,0,np.inf)
# print (i)
import numpy as np
from scipy.integrate import quad
invexp = lambda x: np.exp(-x)
y=quad(invexp, 0, np.inf)
print(y)