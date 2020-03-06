### Scipy can be used for optimizing functions ########
import numpy as np
from scipy import optimize

def fx(x):
    """A simple quadratic function"""
    return 2*x[0]*x[0]+3*x[1]*x[1]*x[1]+x[1]*x[1]+20*x[0]+3

def grad_fx(x):
    return np.array([4*x[0]+20, 6*x[1]*x[1]+2*x[1]])

x0 = np.array([0,0])
xopt = optimize.fmin_bfgs(fx, x0, fprime=grad_fx)
print xopt, fx(xopt)
