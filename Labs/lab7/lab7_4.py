import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,100)
y=np.sign(x)
plt.plot(x,y)
plt.xlim(x.min()*1.1, x.max()*1.1)
plt.ylim(y.min()*1.1, y.max()*1.1)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
