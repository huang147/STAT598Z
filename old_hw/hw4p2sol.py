import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

rand.seed(3456)

num_sample=3000
gamma=5.0
beta=5.0
unifs=np.sqrt(rand.uniform(low=0, high=1, size=num_sample))
samples=np.power(1-np.power(1.0-unifs, 1.0/beta), 1.0/gamma)

plt.hist(samples)

plt.show()
