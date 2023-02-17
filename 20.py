import time
import numpy
a = numpy.arange(1,100,0.1)
print(a)
b = numpy.arange(100,200,0.1)
# classic implementation
tic = time.process_time()
outer_product =numpy.zeros((len(a), len(b)))
for i in range(len(a)):
    for j in range(len(b)):
        outer_product[i][j]= a[i]*b[j]
toc = time.process_time()
print("outer_product = ",outer_product);
print("Computation time "+str(1000*(toc - tic ))+"ms")
#vectorized computing
n_tic = time.process_time()
outer_product = numpy.outer(a,b)
n_toc = time.process_time()
print("outer_product = "+str(outer_product));
print("\nComputation time = "+str(1000*(n_toc - n_tic ))+"ms")