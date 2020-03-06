import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

rand.seed(123456)

# B stands for beta, G stands for gamma, n is the total sample number
def fy_gen(G,B,n):
    u=rand.uniform(0,1,n)
    fy=(1-(1-u)**(1.0/B))**(1.0/G)
    return fy

def fy(G,B,n,y):
    return G*B*(y**(G-1))*((1-y**G)**(B-1))


n=3000;G=3;B=2
y=np.linspace(0,1,n)
fy=fy(G,B,n,y)
yy=fy_gen(G,B,n)

# plot fy vs y, and histogram of random sampling
plt.figure(1)
plt.hist(yy,bins=100,normed=True)
plt.plot(y,fy,'red')
plt.show()
