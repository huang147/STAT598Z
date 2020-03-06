import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# defined the function
def fx(x):
    return 2*x + 3*x**2 + 3*np.cos(x)

# gradient of the function 
def grad_fx(x):
    return 2 + 6*x - 3*np.sin(x) 

# initialize x and y as two list of numbers
x = np.linspace(-10,10,num = 1000)
y = []

# give an intial value for x
x0 = 1

# do the optimization and print the result
xopt = optimize.fmin_bfgs(fx, x0, fprime=fx)
print "Value of x when f(x) is minimized:", xopt, "Minimum value of f(x):", fx(xopt)

# get the values of y = f(x) by calculation
for i, v in enumerate(x):
    y.append( fx(v) )
 
# make the plot 
plt.plot(x,y)
plt.title(r"$x$ vs $f(x)$")
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.show()





    
