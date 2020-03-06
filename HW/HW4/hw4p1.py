import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

rand.seed(12345)

# method1: accept-reject sampling
def ar_gen1(n):
    rvx=np.zeros(n);rvy=np.zeros(n)
    total=0.0
    for i in np.arange(n):
        while True:
            total=total+1
            x=rand.uniform(-1,1,size=1)
            y=rand.uniform(-1,1,size=1)
            # accept sample only when both x and y are in the limits
            if x >= 0 and x <= 1:
                if y <= 1-x and y >=x-1:
                    rvx[i]=x;rvy[i]=y
                    break
            elif x < 0 and x >= -1:
                if y <=x+1 and y >= -x-1:
                    rvx[i]=x;rvy[i]=y
                    break
    efficiency=n/total
    return rvx,rvy,efficiency

# method2: simple coordinate rotation
def ar_gen2(n):
    rvx = np.zeros(n);rvy=np.zeros(n)
    total=0.0
    for i in np.arange(n):
        total=total+1
        # draw sample from x~uniform(-sqrt(2)/2,sqrt(2)/2)
        # and y~uniform(-sqrt(2)/2,sqrt(2)/2)
        x=rand.uniform(-0.707,0.707,size=1)
        y=rand.uniform(-0.707,0.707,size=1)
        # rotate by 45 degrees (counter clockwise)
        rvx[i]=0.707*x+0.707*y
        rvy[i]=-0.707*x+0.707*y
    efficiency=n/total
    return rvx,rvy,efficiency
        

# plot the result, comparing method1 and method2
n=3000
plt.figure(1,figsize=(10,5))

plt.subplot(121)
x,y,eff=ar_gen1(n) 
plt.legend()
plt.title(("Accept-Reject: Efficiency",eff))
plt.scatter(x,y)
xx=np.linspace(-1,1,n)
yy1=np.ones(n);yy2=-1.0*np.ones(n)
xxx1=np.ones(n);xxx2=-1*np.ones(n)
yyy=np.linspace(-1,1,n)
plt.plot(xx,yy1,'r',xx,yy2,'r',xxx1,yyy,'r',xxx2,yyy,'r')

plt.subplot(122)
x,y,eff=ar_gen2(n) 
plt.legend()
plt.title(("Coordinate Rotate: Efficiency",eff))
plt.scatter(x,y)
xx=np.linspace(-1,1,n)
yy1=np.ones(n);yy2=-1.0*np.ones(n)
xxx1=np.ones(n);xxx2=-1*np.ones(n)
yyy=np.linspace(-1,1,n)
plt.plot(xx,yy1,'r',xx,yy2,'r',xxx1,yyy,'r',xxx2,yyy,'r')

plt.show()


