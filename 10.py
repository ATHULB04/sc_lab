#program to find adjoint
import numpy as np
m=np.array([[0,1,2],[1,2,3],[3,1,1]])
print(np.linalg.det(m))
print(np.linalg.inv(m))
m1=(np.linalg.det(m)*np.linalg.inv(m))
print(m1)

