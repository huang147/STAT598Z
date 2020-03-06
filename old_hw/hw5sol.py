import numpy as np

# Solution to HW 5

# Given a file handle of a LibSVM file, find the total number of points
# in the dataset and the maximum index 
def find_stats(fp):
    # Total number of points in the dataset
    num_pts=0

    # Maximum index of a data point
    max_idx=0

    # Collect information about the dataset 
    for l in fp:
        num_pts=num_pts+1
        # Remove any extra whitespace 
        l=l.strip()
        iv_pairs=l.split(" ")
        # The first token is the label 
        label=iv_pairs[0]
        for iv in iv_pairs[1:]:
            iandv=iv.split(":")
            idx=int(iandv[0])
            val=float(iandv[1])
            if idx > max_idx:
                max_idx=idx
    return num_pts, max_idx

# Read the data from the file given total number of points and maximum
# index 
def read_data(fp,num_pts,max_idx):

    # Allocate space
    data=np.zeros((num_pts,max_idx+1))
    labels=np.zeros(num_pts)
    
    i=0

    # Read the data file again 
    for l in fp:
        # Remove any extra whitespace 
        l=l.strip()
        iv_pairs=l.split(" ")
        # The first token is the label 
        labels[i]=iv_pairs[0]
        for iv in iv_pairs[1:]:
            iandv=iv.split(":")
            idx=iandv[0]
            val=iandv[1]
            data[i,idx]=val
        i=i+1
    return data,labels 

def dist_sq(x,y,ysq):
    return np.dot(x,x)+ysq-np.dot(y,x)

fname="a9a.txt"
f=open(fname, "r")
num_pts,max_idx=find_stats(f)
f.seek(0)

tfname="a9a.t.txt"
tf=open(tfname, "r")
num_test,tmp=find_stats(tf)
tf.seek(0)

if tmp>max_idx:
    max_idx=tmp

data,labels=read_data(f,num_pts,max_idx)
tdata,tlabels=read_data(tf,num_test,max_idx)

ysq=np.zeros(num_pts)
for i in np.arange(num_pts):
    ysq[i]=np.dot(data[i],data[i])

# Set this to k=1 for problem 2 and any other positive integer > 1 for
# problem 3
for k in (1,2,3,4,5):

    predicted=np.zeros(num_test)
    for i in np.arange(num_test):
        dsq=dist_sq(tdata[i],data,ysq)
        idx=np.argsort(dsq)
        idx=idx[0:k]
        if np.sum(labels[idx])>0:
            predicted[i]=+1
        else:
            predicted[i]=-1

    errors=np.sum(np.abs(predicted-tlabels))/2
    print "k: %d" % k
    print errors, "errors out of", num_test, "points" 

