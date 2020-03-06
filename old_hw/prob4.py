import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

np.random.seed(17)
u=rand.uniform(0,1,10000)
x=np.sqrt(u)
np.all(x>=0) #are all the samples greater than 0?
np.all(x<=1) # are all the samples less than 1?
count,bins,ignored = plt.hist(x,100,normed=1,color='red')
plt.title('Histogram for U(0,1)-Scheme 1')
plt.ylim([0,2])
plt.show()

np.random.seed(123)
u=rand.uniform(0,1,[2,10000])
v=u.max(axis=0)
np.all(v>=0) #are all the samples greater than 0?
np.all(v<=1) # are all the samples less than 1?
count,bins,ignored = plt.hist(v,100,normed=1,color='blue')
plt.title('Histogram for U(0,1)- Scheme 2')
plt.ylim([0,2])
plt.show()
