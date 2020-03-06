import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

U=rand.uniform(0,1,5000)
theta=rand.uniform(0,2*np.pi,5000)
x1=U*np.cos(theta)
x2=U*np.sin(theta)


plt.scatter(x1,x2)


x=np.arange(-1,1,0.01)
y1=-np.sqrt(1.0-x*x)
y2=np.sqrt(1.0-x*x)
plt.plot(x,y1,x,y2)
plt.show()
