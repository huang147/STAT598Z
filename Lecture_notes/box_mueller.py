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

def exponential_rvgen(lamb,n=1):
    # Recall the signature for uniform(low=0.0, high=1.0, size=1)
    
    U=rand.uniform(size=n)
    X=-np.log(U)/lamb
    return X

# We will use the above function to generate samples from the normal
# distribution 

def box_mueller(n=1):
    lamb=0.5
    if (n%2) ==0:
        theta=rand.uniform(low=0,high=2*np.pi,size=n/2)
        x=exponential_rvgen(lamb, n/2)
        x1=np.sqrt(x)*np.cos(theta)
        x2=np.sqrt(x)*np.sin(theta)
        return np.hstack((x1,x2))
    else:
        theta=rand.uniform(low=0,high=2*np.pi,size=n)
        x=exponential_rvgen(lamb, n)
        x1=np.sqrt(x)*np.cos(theta)
        return x1
    
n=10000
x=box_mueller(n)
plt.hist(g,bins=100,normed=True)

# Now let us plot the true density and verify that the generated
# histogram does match the true density
y=np.arange(start=-5,stop=5,step=0.1)
fy=np.exp(-0.5*y*y)/np.sqrt(2.0*np.pi)

plt.plot(y,fy,"r",linewidth=2)

# Visually verify that we indeed obtained an Gaussian random variable 
plt.show()
