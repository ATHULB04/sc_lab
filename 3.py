import matplotlib.pyplot as p
import scipy as s
import numpy as np
t=np.arange(0,4*np.pi,0.1)
y1=np.cos(t)
fig,a=p.subplots(1,2)
a[0].hist(y1,bins=10,ec="red")
a[1].plot([1,2,3,4,5],ls="-.",marker="*",lw=2)
p.show()
fig1.savefig("output figure-1.jpg")