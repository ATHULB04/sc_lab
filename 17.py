import numpy as np
import matplotlib.pyplot as p
t=np.arange(0,40,0.01)
T=20
fig,a=p.subplots(5)
# f=4/np.pi
# n=1
# y=((-1)**(n))*(1/(2*n+1))*(np.cos(2*np.pi*(2*n+1)*t/T))
# a[0].plot(t,y)
# n=2
# y1=((-1)**(n))*(1/(2*n+1))*(np.cos(2*np.pi*(2*n+1)*t/T))   
# a[1].plot(t,y1)
# n=3
# y2=((-1)**(n))*(1/(2*n+1))*(np.cos(2*np.pi*(2*n+1)*t/T))
# a[2].plot(t,y2)
# y3=4/np.pi*(1+y+y1+y2)
# a[3].plot(t,y3)
s=1
i=0
for j in [4,10,100]:
    for n in range(1,j+1):
        y=((-1)**(n))*(1/(2*n+1))*(np.cos(2*np.pi*(2*n+1)*t/T))
        s+=y
    f=4/np.pi*s
    a[i].plot(t,f)
    i+=1
p.show()