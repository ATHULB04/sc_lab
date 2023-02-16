import numpy as np
m = np.array([[4,2],[1,1]])
print("Original matrix:")
print(m)
result = np.linalg.det(m)
print("Determinant of the given matrix:")
print(result)
if result==0:
    print ("this matrix has no inverse")
else :
    result = np.linalg.inv(m)
    print("Inverse of the said matrix:")
    print(result)