import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-10,10,200)
Y=np.sin(X)
plt.plot(X,Y)
#to add spines in the middle
#ax = plt.gca()
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))

plt.show()
