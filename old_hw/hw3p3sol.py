import numpy as np
import numpy.random as rand

# Always remember to initialize the random number generator
rand.seed(3456)

mu=5.0
sigma=2.0

x=rand.normal(mu, sigma, 4*3*8*6)
print x

A=x.reshape(4,3,8,6)
print A

m=np.mean(A)
print m

s=np.std(A)
print s

v=np.var(A)
print v

mx=np.max(A)
print mx

mn=np.min(A)
print mn
