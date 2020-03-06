import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# Problem 4

def compute_gamma(data,mu,sigma,pii,n,d,k):
    gamma=np.zeros((n,k))
    for j in np.arange(k):
        mu_j=np.outer(np.ones(n), mu[j,:])
        denom_j=np.sqrt(np.linalg.det(sigma[j]))
        tmp=np.dot(np.linalg.inv(sigma[j]),(data-mu_j).T)
        tmp=np.diag(np.dot((data-mu_j),tmp))
        gamma[:,j]=pii[j]*np.exp(-0.5*tmp)/denom_j
    # Normalize
    gamma_sum=np.sum(gamma,axis=1)
    return gamma/np.outer(gamma_sum,np.ones(k))
    
def compute_mu(data,gamma,d,k):
    mu=np.zeros((k,d))
    m=np.sum(gamma,axis=0)
    m=np.outer(m,np.ones(d))
    mu=np.dot(gamma.T,data)/m
    return mu

def compute_sigma(data,gamma,mu,n,d,k):
    sigma=[]
    m=np.sum(gamma,axis=0)
    
    for j in np.arange(k):
        sigma_j=np.zeros((d,d))
        mu_j=mu[j,:]
        for i in np.arange(n):
            sigma_j+=gamma[i,j]*np.outer((data[i,:]-mu_j),(data[i,:]-mu_j))
        sigma.append(sigma_j/m[j])
    return sigma

# This code is specialized for two dimensions
def display(data,gamma,n,d,k):
    tmp=np.argmax(gamma,axis=1)
    c=['r','g','b','m']
    for i in np.arange(k):
        class_i=data[tmp==i,:]
        plt.scatter(class_i[:,0], class_i[:,1],s=20,c=c[i],marker='o')
    plt.show()

def gmm(data,n,d,k,max_iter,tol):

    # Initialize sigma, mu, pi, and gamma
    sigma = []
    for i in np.arange(k):
        sigma.append(np.eye(d))
    mu=rand.uniform(size=(k,d))
    pii=np.ones(k)*1.0/k
    gamma=np.zeros((n,k))

    for iter in np.arange(max_iter):
        prev_gamma=gamma
        gamma=compute_gamma(data,mu,sigma,pii,n,d,k)
        diff=np.sum(np.abs(prev_gamma-gamma))*1.0/n
        if diff<tol:
            print "converged in", iter, "iterations"
            print 'pi=', pii
            print 'mu=', mu
            print 'sigma=', sigma
            display(data,gamma,n,d,k)
            return mu,sigma,pii
        else:
            print "diff:", diff

        mu=compute_mu(data,gamma,d,k)
        sigma=compute_sigma(data,gamma,mu,n,d,k)
        pii=np.sum(gamma,axis=0)*1.0/n

    print "did not converge!"
    print 'pi=', pii
    print 'mu=', mu
    print 'sigma=', sigma
    display(data,gamma,n,d,k)
    return mu,sigma,pii


# n1 and n2 are number of points to draw from the two Gaussians
n1=300
n2=700
n=n1+n2

# The mean and variance values given in the problem 
mu1=np.array([0,0])
sigma1=np.array([[2,2],[1,2]])
mu2=np.array([6,6])
sigma2=np.array([[1,0],[0,1]])

rand.seed(90876)

data1=rand.multivariate_normal(mu1, sigma1, n1)
data2=rand.multivariate_normal(mu2, sigma2, n2)
data=np.vstack([data1,data2])

# dimension
d=2

# Number of clusters
k=2

# Maximum number of iterations 
max_iter=1000

# Iteration tolerance 
tol=0.001

mu,sigma,pii=gmm(data, n, d, k, max_iter, tol)
