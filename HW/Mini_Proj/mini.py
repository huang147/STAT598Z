import numpy as np
import numpy.random as rand
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D



# read data from raw data files
def read(fname):
    label=[]
    col=[]
    m=0
    f=open(fname,'r')
    for line in f:
        m=m+1
        line = line.strip()
        a=np.zeros
        a=line.split()
        label.append(int(a[0])) # label 
        for v in a[1:]:
            (b1,b2)= v.split(':')
            if not int(b1) in col:
                col.append(int(b1))
    col.sort()
    d=col[-1]+1
    return label,col,d,m
    
# insert values into the initialized data matrix
def insertvalue(fname,d,m):
    data=np.zeros((m,d))    
    row=0
    f=open(fname,'r')
    for line in f:
        line = line.strip()
        a=np.zeros
        a=line.split()
        for v in a[1:]:
            (idx,val)= v.split(':')
            idx=int(idx);val=float(val)
            column=idx
            data[row,column]=val
        row=row+1
    return data[:,1:]


def gJ(w,X,Y,lamb=0.001):
    gJ1=lamb*w
    gJ2=-2*np.dot(X.T,Y)+2*np.dot(X.T,(Y*(np.dot(X,w))*Y))
    gJ2[gJ2<0]=0
    gJ=gJ1+gJ2
    return gJ

def J(w,X,Y,lamb=0.001):
    J1=0.5*lamb*np.dot(w.T,w)
    a=np.ones_like(Y)-Y*np.dot(X,w)
    J2=np.dot(a.T,a)
    J=J1+J2
    return J[0][0]

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
            #print "Optimized w: \n",(w[t]-h*gradient).T
            break
        elif t==maxiter-1:
            print "\nCan not converge in",maxiter,"iterations"
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
    #ax.text3D(-2,7,np.max(jw),N)
    fig.savefig(name)    

def accuracy(X1,Y1,X2,Y2,lamb=0.001):
    w0=X1[0].reshape(X1.shape[1],1)
    w,zw=grad_desc(X1,Y1,w0,e=0.01,h=0.00001,maxiter=1000,lamb=lamb)
    w1=w[-1]
    L=Y2-np.sign(np.dot(X2,w1))
    Accuracy=1.0*len(L[L==0])/len(L)
    print "Lambda:",lamb," Accuracy:",Accuracy,"\n"
    return L

a1a="a1a"; a1at="a1a.t"
alabel,acol,ad,am=read(a1a)
tlabel,tcol,td,tm=read(a1at)
if ad <= td:
    d=td
else:
    d=ad
# data matrices of training and test sets
X1=insertvalue(a1a,d,m=am) # train data
X2=insertvalue(a1at,d,m=tm) # test data

Y1=np.array(alabel).reshape(am,1) # train label
Y2=np.array(tlabel).reshape(tm,1) # test label


accuracy(X1,Y1,X2,Y2,lamb=0.001)
accuracy(X1,Y1,X2,Y2,lamb=0.0001)
accuracy(X1,Y1,X2,Y2,lamb=0.0)
accuracy(X1,Y1,X2,Y2,lamb=0.01)
accuracy(X1,Y1,X2,Y2,lamb=0.1)
accuracy(X1,Y1,X2,Y2,lamb=1.0)
accuracy(X1,Y1,X2,Y2,lamb=100.0)
accuracy(X1,Y1,X2,Y2,lamb=1000.0)
accuracy(X1,Y1,X2,Y2,lamb=10000.0)
accuracy(X1,Y1,X2,Y2,lamb=100000.0)





