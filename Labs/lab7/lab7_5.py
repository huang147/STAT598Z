import numpy as np	
import matplotlib.pyplot as plt
np.random.seed(17)
r_num = np.random.uniform(0,1,1000)
np.all(r_num>=0) #are all the samples greater than 0?
np.all(r_num<=1) # are all the samples less than 1?
count,bins,ignored = plt.hist(r_num,15,normed=1,color='red')
plt.title('Histogram for U(0,1)')
plt.show()
