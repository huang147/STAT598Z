import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

num_sample = 3000

# sample radius using inverse transform
radiuses = np.sqrt(rand.uniform(low=0, high=1, size=num_sample))

# sample angles
angles = rand.uniform(low=0, high=2 * np.pi, size=num_sample)

xpos = radiuses * np.cos(angles)
ypos = radiuses * np.sin(angles)

plt.scatter(xpos, ypos)

plt.show()


# due to heavy-tailedness of Cauchy distribution,
# histogram does not look pretty if outlying points
# are included, so specific range was used.
plt.hist(xpos/ypos, bins=100, normed=True, range=(-5,5))

plt.show()
