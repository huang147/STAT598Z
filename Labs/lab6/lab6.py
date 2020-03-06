print " ** Lab 6 question 1 ** "
from numpy import *
a = arange(10)
print a

a_rs=linspace(1,9,9).reshape(3,3)
print 'Matrix A ='
print a_rs

b=array([3,7,9])
print 'vector b =', b
ab=a_rs*b
print 'Product A*b ='
print ab

print " ** Lab 6 Question 2 - dot product ** "

a=linspace(1,11,6)
b=linspace(2,12,6)

print "Dot product of ",a," and ", b," is ", dot(a,b)
print "Rank-1 matrix", outer(a,b)

print " ** Lab 6 Question 3 - mean and median ** "

a=linspace(1,9,9)
print a
print "Mean :", mean(a)
print "Median :",median(a)
print "Average :",average(a)

print " ** Lab 6 Question 4  - vector cross product ** "

a=array([10,20,30])
b=array([5,6,8])
cross_ab=cross(a,b)
print "Vector cross Product of ",a, " and ",b," is ", cross_ab

print " ** Lab 6 Question 5 - Transpose ** "

## Method 1
A=array([(1,2,3),(4,5,6),(7,8,9)])
print "Matrix A : "
print A
print "Transpose of A: "
print A.transpose()

# Method 2
A=matrix('3 5 6;2 4 1;7 8 3')
print "Matrix A : "
print A
print "Transpose of A: "
print A.T

print " ** Lab 6 Question 6 - Increment** "

A=linspace(1,10,10)
print "before increment"
print A
A+=1
print "after increment"
print A

print " ** Lab 6 Question 7 - Matrix indexing and slicing ** "

A=zeros((5,2))
B=ones((5,2))
print "7.a";A;"7.b";B

A[1,0]=1
B*=10
B[3,1]=0
print "7.c";A;"7.d";B

A=zeros((5,2))
A[[0,1],:]=eye(2)
print "7.e";A

A=zeros((5,2))
A[[0,1],:]=diag([1,2])
print "7.f";A


print " ** Lab 6 Question 8  ** "
A=random.randint(0,100,10)
b=(A%2==0)
print "Array :",A; "The even elements are: " ,A[b]

print "Reverse Order",A[::-1]

A[::2]=-1*ones(5)
print "Even digits replaced by -1"
print A

A[::2]=zeros(5)
print "Even digits deleted "
print A





