import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(x):
    return 2*x**2+8*sin(x)
	
retval= optimize.fmin_bfgs(f, 4.7)
print retval, f(retval)
x = arange(-10,10,0.1)
plt.plot(x, f(x))
plt.plot(retval, f(retval), "o", markersize=8)
plt.savefig("foo.pdf")
plt.show()
