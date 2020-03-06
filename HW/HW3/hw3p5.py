import numpy as np
import matplotlib.pyplot as plt
from matplotlib import spines
from scipy import optimize

def fx(x):
    return np.sin(x)

def gx(x):
    return np.cos(x)

def px(x):
    return np.tan(x)

x = np.linspace(-10,10,num = 100)
yf = []
yg = []
yp = []

for v in x:
    yf.append(fx(v))
    yg.append(gx(v))
    yp.append(px(v))



#print yf,yg,yp


fig = plt.figure(1)
pyf = plt.add_subplot(1,3,1)

#pyf.ylim(-1,1)
#plt.title(r"$sin wave$")
#pyf.xlabel(r"$x$")
#pyf.ylabel(r"$sin(x)$")
box = pyf.get_position()
#plt.set_position([box.x0, box.y0, box.width*0.8, box.height])

#box = pyf.get_position()
#pyf.set_position([box.x0, box.y0, box.width*0.8, box.height])




#plt.plot(x,yf)



#leg = ax.legend(['abc'], loc = 'center left', bbox_to_anchor = (1.0, 0.5))



plt.subplot(1,3,2)
plt.plot(x,yg)
plt.ylim(-1,1)
plt.title(r"$cos wave$")
plt.xlabel(r"$x$")
plt.ylabel(r"$cos(x)$")


plt.subplot(1,3,3)
plt.plot(x,yp)
plt.ylim(-1,1)
plt.title(r"$tan wave$")
plt.xlabel(r"$x$")
plt.ylabel(r"$tan(x)$")


plt.show()



