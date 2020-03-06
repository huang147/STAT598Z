# Import the modules we will need. All of these should be familiar to
# you by now 
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# This is needed for the beta function
import scipy.special as spl

# Always remember to initialize the random number generator
rand.seed(3456)


# This function performs accept reject sampling
# dist = the distribution function
# minsup = minimum value of support
# maxsup = maximum value of support
# maxdist = maximum value of the distribution
# n = number of desired samples
def arsampler(dist, minsup, maxsup, maxdist, n):
    rv=np.zeros(n)
    for i in np.arange(n):
        while True:
            x=rand.uniform(low=minsup,high=maxsup,size=1)
            u=rand.uniform(low=0.0,high=maxdist,size=1)
            if u < dist(x):
                rv[i]=x
                break
    return rv

def beta(x, a=3, b=5):
    return np.power(x, a-1.0)*np.power(1.0-x,b-1.0)/spl.beta(a, b)

# Let us generate samples from the beta distribution
a=3
b=5

## Verify for yourself that the maximum of the Beta distribution is
## attained at x = (a-1/a+b-2) provided a > 1

maxx=(a-1.0)/(a+b-2.0)
maxdist=beta(maxx)
n=10000
x=arsampler(beta, 0, 1.0, maxdist,n)
plt.hist(x,bins=100,normed=True)

# Now let us plot the true density and verify that the generated
# histogram does match the true density
y=np.arange(start=0,stop=1.0,step=0.1)
fy=beta(y)
plt.plot(y,fy,"r",linewidth=2)

# Visually verify that we indeed obtained an exponential random variable 
plt.show()
