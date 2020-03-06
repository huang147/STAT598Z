import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# This code is specialized for two dimensions
def display(data, closest_mu, n, d, k):
    c=['r','g','b','m','c']
    for i in np.arange(k):
        class_i=data[closest_mu==i,:]
        plt.scatter(class_i[:,0], class_i[:,1], s=20, c=c[i], marker='o')

def one_iter(data, xsq, n, d, means, k):
    # Compute the distance
    msq=np.zeros(k)
    for i in np.arange(k):
        mu_i=means[i,:]
        msq[i]=np.dot(mu_i, mu_i)

    e1=np.ones(k)
    e2=np.ones(n)
    dist=np.outer(xsq, e1)+np.outer(e2, msq)-2*np.dot(data, means.T)
    closest_mu=np.argmin(dist, axis=1)
    new_means=np.zeros((k, d))
    for i in np.arange(k):
        new_means[i]=np.sum(data[closest_mu==i,:], axis=0)/(1.0*np.sum(closest_mu==i))
    
    J=0.0;
    for j in range(n):
        J=J+np.dot(data[j,:]-new_means[closest_mu[j],:],data[j,:]-new_means[closest_mu[j],:])

    return J,closest_mu,new_means

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
data=np.vstack([data1, data2])

# dimension
d=2

# Maximum number of iterations 
max_iter=1000

# Iteration tolerance 
tol=0.001

# Pre-compute x_i^2
xsq=np.zeros(n)
for i in np.arange(n):
    x_i=data[i,:]
    xsq[i]=np.dot(x_i, x_i)

### Problem 1

rand.seed(12897)

# Number of clusters
k=2

# Select initial clusters 
seeds=rand.random_integers(low=0, high=n-1, size=k)

# Store the selected seed points 
means=data[seeds,:]

J=[];
tot_iter=0;
for i in np.arange(max_iter):
    J_new,closest_mu,new_means=one_iter(data, xsq, n, d, means, k)
    J.append(J_new)
    diff=np.abs(np.sum(new_means-means))
    means=new_means.copy()
    tot_iter=tot_iter+1;
    if diff<tol:
        break

print "Itr:", tot_iter, "J:", J[i]
print "means", means
#display(data,closest_mu,n,d,k)
#plt.plot(range(tot_iter),J)
#plt.show()

### Problem 2
rand.seed(896)

for k in (3,5):
    # Select initial clusters 
    seeds=rand.random_integers(low=0, high=n-1, size=k)

    # Store the selected seed points 
    means=data[seeds,:]

    J=[];
    tot_iter=0;
    for i in np.arange(max_iter):
        J_new,closest_mu,new_means=one_iter(data, xsq, n, d, means, k)
        J.append(J_new)
        diff=np.abs(np.sum(new_means-means))
        means=new_means.copy()
        tot_iter=tot_iter+1;
        if diff<tol:
            break

    print "K:", k, "Itr:", tot_iter, "J:", J[i]
    print "means", means

    display(data,closest_mu,n,d,k)
    #plt.plot(range(tot_iter),J)
    
plt.show()


### Problem 3

for init in range(10):

    rand.seed(init)
    k=3

    # Select initial clusters 
    seeds=rand.random_integers(low=0, high=n-1, size=k)

    # Store the selected seed points 
    means=data[seeds,:]

    J=[];
    tot_iter=0;
    for i in np.arange(max_iter):
        J_new,closest_mu,new_means=one_iter(data, xsq, n, d, means, k)
        J.append(J_new)
        diff=np.abs(np.sum(new_means-means))
        means=new_means.copy()
        tot_iter=tot_iter+1;
        if diff<tol:
            break

    print "init:", init, "Itr:", tot_iter, "J:", J[i]
    print "means", means
