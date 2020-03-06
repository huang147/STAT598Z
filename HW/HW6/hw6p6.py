import numpy as np
import numpy.random as rand
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


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


def gmm(X,n,d,k,max_iter,tol):
    #initialize pi,mu,sigma, and gamma
    gamma=np.zeros((n,k))
    sigma=[]
    for i in np.arange(k):
        sigma.append(np.eye(d))
    mu=rand.uniform(size=(k,d))
    pi=1.0*np.ones(k)/k

    for iter in np.arange(max_iter):
        prev_gamma=gamma
        gamma=calc_gamma(X,n,d,k,mu,sigma,pi)
        diff=1.0*np.sum(np.abs(prev_gamma-gamma))/n
        if diff<tol:
            print "converged in",iter,"iterations"
            plot(X,gamma,n,d,k)
            return mu,sigma,pi
        else:
            print "diff",diff
        
        mu=calc_mu(X,gamma,d,k)
        sigma=calc_sigma(X,gamma,mu,n,d,k)
        pi=1.0*np.sum(gamma,axis=0)/np.sum(gamma)
    print "can not converge in", max_iter,"iterations"
    plot(X,gamma,n,d,k)
    return mu,sigma,pi


def plot(X,gamma,n,d,k):
    C=['red','green','blue','cyan','magenta','gold','gray','purple','navy','darkkhaki']
    cluster=np.argmax(gamma,axis=1)
    Fig10=plt.figure(10)
    plt.title("Gaussian Mixture Model 2-D")
    for j in np.arange(k):
        cluster_j=X[cluster==j]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        x=cluster_j[:,0];y=cluster_j[:,1]
        #plt.scatter(cluster_j[:,0],cluster_j[:,1],c=C[j],s=30)
        plt.scatter(x,y,c=C[j],s=30)
        plt.axis('equal')
    Fig10.savefig('GMM.png')
    
    Fig11=plt.figure(11,figsize=(10,5))
    plt.subplot(121)
    plt.title("Gaussian Mixture Model X Histogram")
    for j in np.arange(k):
        cluster_j=X[cluster==j]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        x=cluster_j[:,0]
        #plt.hist(cluster_j[:,0],color=C[j])
        plt.hist(x,color=C[j])
    plt.subplot(122)
    plt.title("Gaussian Mixture Model Y Histogram")
    for j in np.arange(k):
        cluster_j=X[cluster==j]
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        y=cluster_j[:,1]
        plt.hist(y,color=C[j])
        #plt.hist(cluster_j[:,1],color=C[j])
    Fig11.savefig('GMMhist.png')



def calc_sigma(X,gamma,mu,n,d,k):
    sigma=[]
    m=np.sum(gamma,axis=0)

    for j in np.arange(k):
        sigma_j=np.zeros((d,d))
        mu_j=mu[j,:]
        for i in np.arange(n):
            sigma_j=sigma_j+gamma[i,j]*np.outer((X[i,:]-mu_j),(X[i,:]-mu_j))
        sigma.append(sigma_j/m[j])
    return sigma


def calc_mu(X,gamma,d,k):
    mu=np.zeros((k,d))
    for j in np.arange(k):
        mu[j,:]=np.sum(np.tile(gamma[:,j],d).reshape(gamma.shape[0],d)*X,axis=0)/np.sum(gamma[:,j])
    return mu


def calc_gamma(X,n,d,k,mu,sigma,pi):
    gamma_numer=np.zeros((n,k))
    for j in np.arange(k):
        mu_j=np.outer(np.ones(n),mu[j,:])

        tmp1=np.dot(np.linalg.inv(sigma[j]),(X-mu_j).T)
        tmp2=-0.5*np.diag(np.dot((X-mu_j),tmp1))
        
        denom_j=2*np.pi*np.sqrt(np.linalg.det(sigma[j]))
        gamma_numer[:,j]=pi[j]*np.exp(tmp2)/denom_j

    gamma_sum=np.sum(gamma_numer,axis=1)
    gamma=gamma_numer/np.outer(gamma_sum,np.ones(k))
    return gamma



N=150


mu1=[0,0];var1=[[1,0],[0,1]]
mu2=[10,0];var2=[[0.1,0],[0,1]]
mu3=[5,5];var3=[[2,0],[0,2]]
L,X,T=GenX(mu1,var1,mu2,var2,mu3,var3,N)


d=2
k=3
max_iter=10000
tol=0.01

mu,sigma,pi=gmm(X,N,d,k,max_iter,tol)


