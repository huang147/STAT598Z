import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print x
A=x.reshape(4,3)
print A
B=A[ix_([0,1,3],[0,1])]
print B
y=np.array( [6,8] )
print y
C=np.dot(B,y)
print C
