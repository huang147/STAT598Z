import numpy as np
import matplotlib.pyplot as plt

radii=np.arange(1,7,1)
circum=2*np.pi*radii
plt.plot(radii,circum,'r')
plt.xlabel('radii')
plt.ylabel('circumference')
plt.title('Radius vs Circumference Plot')
plt.show()
