#to read csv file
import numpy as np
import matplotlib.pyplot as p
y=np.genfromtxt("waveform.csv",delimiter=",")
t=np.arange(0,0.002, 0.00002)
print(np.mean(y))
print(np.std(y))
fig,a=p.subplots(3)
a[0].plot(y)
a[1].boxplot(y)
a[2].hist(y,ec="red")
p.show()