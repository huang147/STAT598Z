import numpy as np
import numpy.random as rand

# generate random numbers from standard normal distribution
# standard normal = Gaussian with mean = 0 and std = 1
# first seed the random number generator 
rand.seed(201314)
size = 4 * 3 * 8 * 6 
a = np.array(rand.standard_normal(size))
# resize a so it has shape (4,3,8,6)
a.resize(4,3,8,6)

# find the mean, std, var, min, max for a 
print "mean(a):", np.mean(a)
print "std(a):", np.std(a)
print "var(a):", np.var(a)
print "min(a):", np.min(a)
print "max(a):", np.max(a)



