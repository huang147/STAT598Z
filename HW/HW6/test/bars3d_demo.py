from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax =Axes3D(fig)
for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
    xs = np.arange(20)
    ys = np.arange(20)
    print "ys",ys

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

fig=plt.figure()
ax=Axes3D(fig)
xs = np.arange(20)
ys = np.arange(20)
zs=10
ax.bar(xs, ys)
plt.show()


#x,y = np.random.randn(2,10)
#print np.histogram2d(x,y)

x=np.arange(10)
y=2*np.arange(10)

H,xedges,yedges = np.histogram2d(x, y, bins = (2, 2))
print H,xedges,yedges

#print H.shape, xedges.shape, yedges.shape


fig = plt.figure()
ax =Axes3D(fig)
for z in yedges:
    xs = xedges
    ys = np.arange(20)
    print "ys",ys

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


