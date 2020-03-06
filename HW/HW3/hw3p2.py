import numpy as np

# hw3p2(a)
# create a numpy array x and print it 
x = np.arange(1,16)
print "x:", x

# hw3p2(b)
# reshape x into a 5*3 matrix A and print A
A = x.reshape(5,3)
print "A:", A

# hw3p2(c)
# take row 1,2,4 and column 1,3 and make matrix B; print B 
B = (A[(0,1,3),:])[:,(0,2)]
print "B:", B
# make a vector (3,5)
y = np.array([[3],[5]])
# multiply B by the vector (3,5) and print the result
By = np.dot(B, y)
print "By:", By

# hw3p2(d)
# reshape x into a 5*3 matrix and print 
C = (x.reshape(3,5)).T
print "C:", C
