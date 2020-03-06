import numpy as np
import numpy.random as rand

rand.seed(12398)
a = rand.uniform(low = 0, high = 1, size = 10)
print "a:", a

rand.seed(None)
b = rand.rand(10)
print "b:", b

