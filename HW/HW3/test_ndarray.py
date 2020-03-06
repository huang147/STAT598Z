import numpy as np


x = np.array([12,44,1,2,3,34,4,45,5,5,56,34])

print "x:", x
print "xshape:", x.shape

#x.resize(1,3,2,2)
y=x.reshape(1,3,2,2)


print "xshape:", x.shape

print "new x:", x
print "y:",y



