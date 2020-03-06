import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

def function(x):
    a=[]
    a.append(-np.sqrt(1.0-x*x))
    a.append(np.sqrt(1.0-x*x))
    return a

x=np.arange(-1.0,1.0,0.01)
plt.plot(x,function(x)[0],x,function(x)[1]) #draw the boundary 

#Accept-Reject Sampling - draw from unit cube in R2 and accept samples
# that fall inside the disc. Note that this method of sampling from a
# multivariate density is inefficient for higher dimensions.

def arfunction(n):
    rvx=np.zeros(n)
    rvy=np.zeros(n)
    a=0
    for i in np.arange(n):
        x=rand.uniform(-1.0,1.0,1)
        y=rand.uniform(-1.0,1.0,1)
        if x*x+y*y <= 1:
           rvx[i]=x
           rvy[i]=y
           a+=1
        else:
            continue
    print 'efficiency is ',n/a*1.0
    plt.scatter(rvx,rvy)
    plt.show()
    
n=5000
arfunction(n)

