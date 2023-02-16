import matplotlib.pyplot as p
import scipy as s
import numpy as np
y=[]
t=np.arange(-10,10,.01)
for i in t:
    if -5<i<5:
        y.append(4*i*i)
    else:
        y.append(100)
p.boxplot(t,y)
p.show()
print(np.mean(y))


