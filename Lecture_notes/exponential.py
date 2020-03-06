# Import the modules we will need. All of these should be familiar to
# you by now 
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# Always remember to initialize the random number generator
rand.seed(345687)

# Let us write a function which will generate samples from the
# exponential distribution 

# When invoked without any arguments we will return one sample 
# lambda is a reserved keyword in Python. So we use lamb 

def exp_rvgen(lamb,n=1):
    # Recall the signature for uniform(low=0.0, high=1.0, size=1)
    u=rand.uniform(size=n)
    x=-np.log(u)/lamb
    return x

# Let us generate 10000 random variables from the exponential
# distribution
lamb=0.1
n=10000
x=exp_rvgen(lamb, n)
plt.hist(x,bins=100,normed=True)

# Now let us plot the true density and verify that the generated
# histogram does match the true density
y=np.arange(start=0,stop=100,step=0.1)
fy=lamb*np.exp(-lamb*y)
plt.plot(y,fy,"r",linewidth=2)

# Visually verify that we indeed obtained a exponential random variable 
plt.show()

