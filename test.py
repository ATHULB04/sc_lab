import numpy as np
A = np.array([[3, 6, 7], [5, -3, 0],[6,5,3]])
B = np.array([[1, 1,5], [2, 1,3], [3,6,-3]])
C=np.array([1,3,6])
#print(A.dot(B))
#print(np.linalg.det(A))
#print(np.linalg.inv(A))
# print(np.linalg.solve(A,C))
# va,ve=np.linalg.eig(A)
# print(va)
# print(ve)
u,s,v=np.linalg.svd(A)
# print(u)
# print(s)
# print(v)
r=np.dot(u,np.dot(np.diag(s),v))
print(r)