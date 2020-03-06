import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
rand.seed(123456)

def Finv(u):
    x = B/((1-u)**(1/a))
    return x

B = 2.0
a = 5.0
n = 10000
u = rand.uniform(0,1,n)
x = Finv(u)
y = np.arange(B, 20, 0.1)
fy = a*(B**a)/(y**(a+1))
plt.plot(y,fy,"r",linewidth = 2)
plt.hist(x,100,normed= True)
plt.legend(('density','histogram'),'upper center',shadow=True, fancybox=True)
print "Samples:", x
plt.show()

