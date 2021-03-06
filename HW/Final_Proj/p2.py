import numpy as np
import numpy.random as rand
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def GenX(mu1,var1,mu2,var2,n=2000):
    rand.seed(12345)

    A1=rand.multivariate_normal(mu1,var1,int(0.5*n))
    L1=np.ones(int(0.5*n),dtype=int).reshape(int(0.5*n),1)
    X1=np.hstack((L1,A1))

    A2=rand.multivariate_normal(mu2,var2,int(0.5*n))
    L2=-1*np.ones(int(0.5*n),dtype=int).reshape(int(0.5*n),1)
    X2=np.hstack((L2,A2))

    L=np.vstack((L1,L2))
    A=np.vstack((A1,A2))
    X=np.vstack((X1,X2))
    return L,A,X


def J(w,X,Y,lamb=0.001):
    J=0.5*lamb*np.dot(w.T,w)+np.dot((np.dot(X,w)-Y).T,(np.dot(X,w)-Y))
    return J[0][0]


def gJ(w,X,Y,lamb=0.001):
    return lamb*w+2*np.dot(X.T,(np.dot(X,w)-Y))

def GetJw(ww1,ww2,X,Y,lamb=0.001):
    jw=np.zeros_like(ww1)
    for i in xrange(ww1.shape[0]):
        for j in xrange(ww1.shape[1]):
            w=np.array((ww1[i,j],ww2[i,j])).reshape(2,1)
            jw[i,j]=J(w,X,Y,lamb)
    return jw

def grad_desc(X,Y,w0,e=0.00001,h=0.00000001,maxiter=1000,lamb=0.001):
    w=[np.array(w0)];zw=[J(w0,X,Y,lamb)]
    for t in xrange(maxiter):
        gradient=gJ(w[t],X,Y,lamb)
        #print t,w[t],gradient
        if np.sqrt(gradient[0]**2+gradient[1]**2)<=e:
            print "\nConverged in ",t,"iterations"
            break
        w.append(w[t]-h*gradient);zw.append(J(w[t],X,Y,lamb))
    w=np.array(w);zw=np.array(zw)
    #print "\nThe values of Wt:\n",w
    return w,zw

def plot(w,zw,e=0.01,h=0.00001,name="JW.png",lamb=0.001):
    fig = plt.figure()
    ax = Axes3D(fig)
    w1=np.arange(-2,7,1)
    w2=np.arange(-2,7,1)
    ww1,ww2=np.meshgrid(w1,w2)
    jw=GetJw(ww1,ww2,X,Y,lamb)
    ax.plot_surface(ww1,ww2,jw,rstride=1,cstride=1, cmap=cm.cool,linewidth=0,antialiased=False)
    ax.plot(w[:,0],w[:,1],zw,marker='o',color='r')
    ax.set_xlabel('w1')
    ax.set_ylabel('w2')
    print 'from',w[0],'to',w[-1]
    N='J(w) min='+str(zw[-1])+'at'+str(w[-1])+ ' e='+str(e)+' h='+str(h)+'lamb='+str(lamb)
    print N
    ax.set_zlabel('J(w)')
    ax.text(w[0,0],w[0,1],zw[0],'start')
    ax.text(w[-1,0],w[-1,1],zw[-1],'end')
    ax.text3D(-2,7,np.max(jw),N)
    fig.savefig(name)    



mu1=[0,0];var1=np.eye(2)
mu2=[5,5];var2=np.eye(2)
Y,X,T=GenX(mu1,var1,mu2,var2,n=2000)

w0=np.array((1,1)).reshape(2,1)

w1,zw1=grad_desc(X,Y,w0,e=0.01,h=0.00001,maxiter=1000,lamb=0.001)
plot(w1,zw1,e=0.01,h=0.00001,name="JW1.png",lamb=0.001)

w2,zw2=grad_desc(X,Y,w0,e=0.01,h=0.00001,maxiter=1000,lamb=1.0)
plot(w2,zw2,e=0.01,h=0.00001,name="JW2.png",lamb=1.0)

w3,zw3=grad_desc(X,Y,w0,e=0.01,h=0.00001,maxiter=1000,lamb=1000.0)
plot(w3,zw3,e=0.01,h=0.00001,name="JW3.png",lamb=1000.0)

w4,zw4=grad_desc(X,Y,w0,e=0.01,h=0.00001,maxiter=1000,lamb=100000.0)
plot(w4,zw4,e=0.01,h=0.00001,name="JW4.png",lamb=100000.0)

w5,zw5=grad_desc(X,Y,w0,e=0.01,h=0.00001,maxiter=1000,lamb=0.0001)
plot(w5,zw5,e=0.01,h=0.00001,name="JW5.png",lamb=0.0001)

w6,zw6=grad_desc(X,Y,w0,e=0.01,h=0.00001,maxiter=1000,lamb=0.0)
plot(w6,zw6,e=0.01,h=0.00001,name="JW6.png",lamb=0.0)







