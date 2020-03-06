import numpy as np
import numpy.random as rand
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D



def J1(x,y):
    return x**2+y**2+x+y

def gJ1(x,y):
    gx=np.zeros_like(x);gy=np.zeros_like(y)
    gx=2*x+1;gy=2*y+1
    return np.array([gx,gy])

def J2(x,y):
    return x**2+2*y**2+x+y

def gJ2(x,y):
    gx=np.zeros_like(x);gy=np.zeros_like(y)
    gx=2*x+1;gy=4*y+1
    return np.array([gx,gy])

def J3(x,y):
    return x**2+10*y**2+x+y

def gJ3(x,y):
    gx=np.zeros_like(x);gy=np.zeros_like(y)
    gx=2*x+1;gy=20*y+1
    return np.array([gx,gy])

def grad_desc(xy0,f=J1,gJ=gJ1,e=0.01,h=0.01):
    w=[np.array((xy0[0],xy0[1]))];t=0
    gx,gy=gJ(xy0[0],xy0[1])
    while np.sqrt(gx**2+gy**2)>=e:
        w.append(w[t]-h*gJ(w[t][0],w[t][1]))
        gx,gy=gJ(w[t+1][0],w[t+1][1])
        t=t+1
    w=np.array(w)
    #print "\nThe values of Wt:\n",w
    print "Converged in",t,"iterations"
    return w

def plot(w,f=J1,e=0.01,h=0.01,name="J1.png"):
    fig = plt.figure()
    ax = Axes3D(fig)
    x=np.arange(-10, 10, 0.5)
    y=np.arange(-10, 10, 0.5)
    xx,yy=np.meshgrid(x,y)
    z=f(xx,yy)
    ax.plot_surface(xx,yy,z,rstride=1,cstride=1, cmap=cm.cool,linewidth=0,antialiased=False)
    zw=f(w[:,0],w[:,1])
    ax.plot(w[:,0],w[:,1],zw,marker='o',color='r')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('J(x)')
    print 'from',w[0],'to',w[-1]
    N='J(x) min='+str(zw[-1])+'at'+str(w[-1])+ '\n'+' e='+str(e)+' h='+str(h)
    print N
    ax.text(w[0,0],w[0,1],zw[0],'start')
    ax.text(w[-1,0],w[-1,1],zw[-1],'end')
    ax.text3D(-5,-5,np.max(z),N)
    fig.savefig(name)

w1=grad_desc([5,5],f=J1,gJ=gJ1,e=0.01,h=0.1);plot(w1,f=J1,e=0.01,h=0.1,name="J1_1.png")
w1=grad_desc([5,5],f=J1,gJ=gJ1,e=0.01,h=0.01);plot(w1,f=J1,e=0.01,h=0.01,name="J1_2.png")
w1=grad_desc([5,5],f=J1,gJ=gJ1,e=0.1,h=0.1);plot(w1,f=J1,e=0.1,h=0.1,name="J1_3.png")
w1=grad_desc([5,5],f=J1,gJ=gJ1,e=0.1,h=0.01);plot(w1,f=J1,e=0.1,h=0.01,name="J1_4.png")


w2=grad_desc([5,5],f=J2,gJ=gJ2,e=0.01,h=0.1);plot(w2,f=J2,e=0.01,h=0.1,name="J2_1.png")
w2=grad_desc([5,5],f=J2,gJ=gJ2,e=0.01,h=0.01);plot(w2,f=J2,e=0.01,h=0.01,name="J2_2.png")
w2=grad_desc([5,5],f=J2,gJ=gJ2,e=0.1,h=0.1);plot(w2,f=J2,e=0.1,h=0.1,name="J2_3.png")
w2=grad_desc([5,5],f=J2,gJ=gJ2,e=0.1,h=0.01);plot(w2,f=J2,e=0.1,h=0.01,name="J2_4.png")


w3=grad_desc([5,5],f=J3,gJ=gJ3,e=0.01,h=0.01);plot(w3,f=J3,e=0.01,h=0.01,name="J3_1.png")
w3=grad_desc([5,5],f=J3,gJ=gJ3,e=0.01,h=0.001);plot(w3,f=J3,e=0.01,h=0.001,name="J3_2.png")
w3=grad_desc([5,5],f=J3,gJ=gJ3,e=0.1,h=0.01);plot(w3,f=J3,e=0.1,h=0.01,name="J3_3.png")
w3=grad_desc([5,5],f=J3,gJ=gJ3,e=0.1,h=0.001);plot(w3,f=J3,e=0.1,h=0.001,name="J3_4.png")









