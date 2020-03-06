import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def rosen(x):
    """rosenbrock function"""
    return (100.0*(x[1]-x[0]**2.0)**2.0 + (1-x[0])**2.0)

def rosen_der(x):
    der = np.zeros_like(x)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[1] = 200*(x[1]-x[0]**2)
    return der

#2-D plot
z = np.linspace(-3,3,100)
x = np.ones((2,100))
x[0] = z
y=rosen(x)
xx = np.ones((2,100))
xx[1] = z
yy = rosen(xx)

plt.figure()
plt.subplot(121)
plt.plot(z,y,color="blue", linewidth=2.5, linestyle="-", label="Rosenbrock(x)")
plt.xlabel(r'$x$')
plt.ylabel(r'$Rosenbrock(x,1)$')
plt.subplot(122)
plt.plot(z,yy,color="red", linewidth=2.5, linestyle="-", label="Rosenbrock(y)")
plt.xlabel(r'$y$')
plt.ylabel(r'$Rosenbrock(1,y)$')
plt.show()

## Optimization using fmin_bfgs
x0 = [1.3, 0.7]
xopt = opt.fmin_bfgs(rosen, x0, fprime=rosen_der)
print xopt

# 3-D plot

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y)
z = (100.0*(yy-xx**2.0)**2.0 + (1-xx)**2.0)
##d = xx.shape
##z = np.zeros(d)
##for i in range(100):
##    r = np.ones((2,100))
##    r[0] = xx[i,:]
##    r[1] = yy[i,:]
##    z[i,:] = rosen(r)
    
ax.plot_surface(xx,yy,z,rstride=1,cstride=1, cmap=cm.coolwarm,linewidth=0,antialiased=False)
ax.contourf(xx,yy,z,zdir='z',offset=-2, cmap=cm.hot)

##ax.zaxis.set_major_locator(LinearLocator(10))
##ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
##fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


