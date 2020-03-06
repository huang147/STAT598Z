import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
y=x**2
z=np.exp(x)
w=np.exp(-x)
plt.plot(x,y,'r')
plt.plot(x,z,'g')
plt.plot(x,w,'b')
plt.legend((r'$x^2$',r'$exp(x)$',r'$exp(-x)$'),'lower center',shadow=True, fancybox=True)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.ylim([-10,10])
plt.title('Function plot using python')
plt.show()
