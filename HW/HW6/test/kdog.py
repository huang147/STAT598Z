from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def plot_xyz_histogram(data,xe,ye,ax, barcolor):
    for duration, occurrence in zip(xe, data):
        current = ye
        #current = range(len(occurrence))
        print duration,current,occurrence
        #print "current",current
        #print "ye",ye
        
        barband = range(-45, 45, 5)
        for modifier in barband:
            #print current,occurrence,duration+(float(modifier)/100)
            ax.bar(current, occurrence, zs=duration+(float(modifier)/100), zdir='y', color=barcolor,alpha=0.6)
    ax.set_xlabel('Current')
    ax.set_ylabel('Duration')
    ax.set_zlabel('Occurrances')
    #plt.show()

x,y = np.random.randn(2,100)
data,xedges,yedges = np.histogram2d(x, y, bins = (4,4))

x2=np.arange(-10,10);y2=2*np.arange(-10,10)
data2,xe2,ye2=np.histogram2d(x2,y2,bins=(4,4))
plt.hist(data2)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)


#plot_xyz_histogram(data,xe,ye,ax,barcolor='b')

plot_xyz_histogram(data2,xe2,ye2,ax,barcolor='r')
plt.show()

