import numpy as np
import numpy.random as rand
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def D(x,U):    
    d=x.shape[0]
    m=U.shape[1]
    n=U.shape[0]
    assert(d==m)    
    # get the distance array for point x vs list of points in U
    e=np.tile(x,n).reshape(n,d)
    dist=np.sum(np.square(e-U),axis=1)
    uidx=dist.argmin()
    jru=dist[uidx]
    return uidx,jru
      

def kmeans(X,U,k,it,Jru):        
    Xidx=xrange(X.shape[0])
    V=-1*np.ones(X.shape[0])
    J=-1*np.ones(X.shape[0])
    Vnew=-1*np.ones(X.shape[0])
    Unew=np.zeros((k,X.shape[1]))
    Unewnew=np.zeros((k,X.shape[1]))
    for i in Xidx:
        x=X[i,:]
        v,jru=D(x,U)
        V[i]=v
        J[i]=jru
    for j in xrange(k):
        unew=np.matrix(X[V==j,:]).mean(0)
        Unew[j,:]=unew
    for p in Xidx:
        x=X[p,:]
        vnew,jrunew=D(x,Unew)
        Vnew[p]=vnew
    for q in xrange(k):
        unewnew=np.matrix(X[Vnew==q,:]).mean(0)
        Unewnew[q,:]=unewnew
    print "Iteration:",it," J(r,u):", np.sum(J)
    Jru.append([it,np.sum(J)])        
    if not np.alltrue(V==Vnew):
        it=it+1
        kmeans(X,Unewnew,k,it,Jru)
    return Unew,Vnew,np.matrix(Jru)


def purity(Xlab,Vnew,k):
    P=[]
    for i in xrange(k):
        Y=Xlab[Vnew==i]
        n1=len(Y[Y==1])
        n2=len(Y[Y==2])
        n3=len(Y[Y==3])
        p=1.0*max(n1,n2,n3)/(n1+n2+n3)
        P.append(p)
    return P


def InitU(X,s,k):
    rand.seed(s)
    u=rand.randint(0,X.shape[0],size=k)
    while not len(u)==len(set(u)):
        u=rand.randint(0,X.shape[0],size=k)
    U=X[u,:]
    print "\nK:",k,"Seed:",s
    return U


def GenX(mu1,var1,mu2,var2,mu3,var3,n=50):
    rand.seed(12345)

    A1=rand.multivariate_normal(mu1,var1,int(0.7*n))
    L1=np.ones(int(0.7*n),dtype=int).reshape(int(0.7*n),1)
    X1=np.hstack((L1,A1))

    A2=rand.multivariate_normal(mu2,var2,int(0.1*n))
    L2=2*np.ones(int(0.1*n),dtype=int).reshape(int(0.1*n),1)
    X2=np.hstack((L2,A2))

    A3=rand.multivariate_normal(mu3,var3,int(0.2*n))
    L3=3*np.ones(int(0.2*n),dtype=int).reshape(int(0.2*n),1)
    X3=np.hstack((L3,A3))

    L=np.vstack((L1,L2,L3))
    A=np.vstack((A1,A2,A3))
    X=np.vstack((X1,X2,X3))
    return L,A,X


C=['red','green','blue','cyan','magenta','gold','gray','purple','navy','darkkhaki'];M=['s','>','o']


N=20000
print "\nGenerating {0:d} points from 3 Gaussian models\n".format(N)



mu1=[0,0];var1=[[1,0],[0,1]]
mu2=[1,0];var2=[[0.1,0],[0,1]]
mu3=[1,1];var3=[[2,0],[0,2]]
L,A,X=GenX(mu1,var1,mu2,var2,mu3,var3,100)

print "\nDifferent Initial Seeds Given K=2!!"
S=rand.randint(0,100,size=4)
JruPlot=[]
Fig0=plt.figure(0,figsize=(7.1*len(S),7))
for i,s in enumerate(S):
    k=2
    U=InitU(X,s,k)

    Unew,Vnew,Jru=kmeans(X,U,k,it=1,Jru=[])
    JruPlot.append(Jru)

    P=purity(L,Vnew,k)
    print "Purities in", k, "classes:", P

    plt.subplot(1,len(S),i+1)
    for kk in xrange(k):
        B=X[Vnew==kk]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        for b in B:
            plt.scatter(b[1],b[2],c=C[kk],marker=M[int(b[0]-1)],s=30)
            plt.axis('equal')
Fig0.savefig('F0.png')

Fig1=plt.figure(1)
plt.title(s='J(r,u) VS Iteration Number Given K=2 and 4 Different Intial Seeds')
for jp in JruPlot:
    plt.plot(jp[:,0],jp[:,1])
Fig1.savefig('F1.png')

print "\nK=2,3,4,5,6!!"
K=xrange(2,7)
Ktext=['K=2','K=3','K=4','K=5','K=6']
JruPlot=[]
Fig2=plt.figure(2,figsize=(7.1*len(K),7))
for i,k in enumerate(K):
    s=30
    U=InitU(X,s,k)

    Unew,Vnew,Jru=kmeans(X,U,k,it=1,Jru=[])
    JruPlot.append(Jru)

    P=purity(L,Vnew,k)
    print "Purities in", k, "classes:", P

    plt.subplot(1,len(K),i+1)
    plt.title(Ktext[i])
    for kk in xrange(k):
        B=X[Vnew==kk]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        for b in B:
            plt.scatter(b[1],b[2],c=C[kk],marker=M[int(b[0]-1)],s=30)
            plt.axis('equal')
Fig2.savefig('F2.png')

Fig3=plt.figure(3)
plt.title(s='J(r,u) VS Iteration Number Given K=2,3,4,5,6')
LG=[]
for j,jp in enumerate(JruPlot):
    c=C[j]
    l=plt.plot(jp[:,0],jp[:,1],color=c)
    LG.append(l)
plt.legend(LG,Ktext,loc='best')
Fig3.savefig('F3.png')



mu1=[0,0];var1=[[1,0],[0,1]]
mu2=[1,0];var2=[[0.1,0],[0,1]]
mu3=[1,1];var3=[[2,0],[0,2]]
L,A,X=GenX(mu1,var1,mu2,var2,mu3,var3,N)

print "\n10 Different Initial Seeds Given K=3!!"
S=rand.randint(0,100,size=10)
Fig4=plt.figure(4,figsize=(7.1*len(S),7))
JruPlot=[]
for i,s in enumerate(S):
    k=3
    U=InitU(X,s,k)

    Unew,Vnew,Jru=kmeans(X,U,k,it=1,Jru=[])
    JruPlot.append(np.matrix(Jru))

    P=purity(L,Vnew,k)
    print "Purities in", k, "classes:", P

    plt.subplot(1,len(S),i+1)
    for kk in xrange(k):
        B=X[Vnew==kk]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        plt.scatter(B[:,1],B[:,2],c=C[kk],s=30)
        plt.axis('equal')
Fig4.savefig('F4.png')

Fig5=plt.figure(5)
plt.title(s='J(r,u) VS Iteration Number Given K=3 and 10 Different Intial Seeds')
for jp in JruPlot:
    plt.plot(jp[:,0],jp[:,1])
Fig5.savefig('F5.png')


print "\n4 Different Mean Values Given K=3!!"
JruPlot=[]
MU=[[[0,0],[1,0],[0,1]],[[-1,0],[1,0],[0,1]],[[0,0],[0,0.5],[0,1]]]
MUtext=['Original Means','Spread-out Means','Close-up Means']
Fig6=plt.figure(6,figsize=(7.1*len(MU),7))
for i,mu in enumerate(MU):
    mu1,mu2,mu3=mu
    var1=[[1,0],[0,1]];var2=[[0.1,0],[0,1]];var3=[[2,0],[0,2]]
    L,A,X=GenX(mu1,var1,mu2,var2,mu3,var3,N)
    print "\nMean1:",mu1,"Mean2:",mu2,"Mean3:",mu3

    k=3;s=30
    U=InitU(X,s,k)

    Unew,Vnew,Jru=kmeans(X,U,k,it=1,Jru=[])
    JruPlot.append(np.matrix(Jru))

    P=purity(L,Vnew,k)
    print "Purities in", k, "classes:", P

    plt.subplot(1,len(MU),i+1)
    plt.title(MUtext[i])
    for kk in xrange(k):
        B=X[Vnew==kk]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        plt.scatter(B[:,1],B[:,2],c=C[kk],s=30)
        plt.axis('equal')
Fig6.savefig('F6.png')

Fig7=plt.figure(7)
plt.title(s='J(r,u) VS Iteration Number Given K=3 and 4 Different Means')
LG=[]
for j,jp in enumerate(JruPlot):
    c=C[j]
    l=plt.plot(jp[:,0],jp[:,1],color=c)
    LG.append(l)
plt.legend(LG,MUtext,loc='best')
Fig7.savefig('F7.png')


print "\n3 Different Variances Given K=3!!"
JruPlot=[]
VAR=[[[[1,0],[0,1]],[[0.1,0],[0,1]],[[2,0],[0,2]]],[[[0.1,0],[0,0.1]],[[0.01,0],[0,0.1]],[[0.2,0],[0,0.2]]],[[[3,0],[0,3]],[[0.3,0],[0,3]],[[6,0],[0,6]]]]
VARtext=['Original Variance','Small Variance','Large Variance']
Fig8=plt.figure(8,figsize=(7.1*len(VAR),7))
for i,var in enumerate(VAR):
    mu1,mu2,mu3=[[0,0],[1,0],[0,1]]
    var1,var2,var3=var
    L,A,X=GenX(mu1,var1,mu2,var2,mu3,var3,N)
    print "\nVar1:",var1,"Var2:",var2,"Var3:",var3

    k=3;s=30
    U=InitU(X,s,k)

    Unew,Vnew,Jru=kmeans(X,U,k,it=1,Jru=[])
    JruPlot.append(np.matrix(Jru))

    P=purity(L,Vnew,k)
    print "Purities in", k, "classes:", P

    plt.subplot(1,len(VAR),i+1)
    plt.title(VARtext[i])
    for kk in xrange(k):
        B=X[Vnew==kk]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        plt.scatter(B[:,1],B[:,2],c=C[kk],s=30)
        plt.axis('equal')
Fig8.savefig('F8.png')


Fig9=plt.figure(9)
plt.title(s='J(r,u) VS Iteration Number Given K=3 and 3 Different Variance')
LG=[]
for j,jp in enumerate(JruPlot):
    c=C[j]
    l=plt.plot(jp[:,0],jp[:,1],color=c)
    LG.append(l)
plt.legend(LG,VARtext,loc='best')
Fig9.savefig('F9.png')


