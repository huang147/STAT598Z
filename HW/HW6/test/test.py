
#def plothist2d(X,gamma,n,d,k):
#    C=['red','green','blue','cyan','magenta','gold','gray','purple','navy','darkkhaki']
#    cluster=np.argmax(gamma,axis=1)
 #   Fig=plt.figure(10)
 #   ax=Axes3D(Fig)
 #   plt.title("Gaussian Mixture Model")
  #  for j in np.arange(k):
   #     cluster_j=X[cluster==j]
    #    H,x,y=np.histogram2d(cluster_j[:,0],cluster_j[:,1],bins=(5,5))
     #   plot_xyz_histogram(H,ax,barcolor=C[j])
    #plt.show()
    #Fig.savefig('GMM.png')


def plot_xyz_histogram(data, ax, barcolor):
    for duration, occurrence in zip(range(len(data)), data):
        current = range(len(occurrence))
        barband = range(-45, 45, 5)
        for modifier in barband:
            ax.bar(current, occurrence, zs=duration+(float(modifier)/100), zdir='y', color=barcolor,alpha=0.6)
            #ax.bar(current, occurrence, zs=duration+(float(modifier)/100))

    ax.set_xlabel('Current')
    ax.set_ylabel('Duration')
    ax.set_zlabel('Occurrances')
    #plt.show()
