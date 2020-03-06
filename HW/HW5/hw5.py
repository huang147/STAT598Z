import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

rand.seed(12345)


def binormal(n,u1,u2,std1,std2,lab):
    x=rand.normal(u1,std1,size=n)
    y=rand.normal(u2,std2,size=n)
    label=np.ones(n)*lab
    xy=np.vstack((label,x,y)).T
    return xy


# read data from raw data files
def read(fname):
    label=[]
    col=[]
    m=0
    f=open(fname,'r')
    for line in f:
        m=m+1
        line = line.strip()
        a=np.zeros
        a=line.split()
        label.append(int(a[0])) # label 
        for v in a[1:]:
            (b1,b2)= v.split(':')
            if not int(b1) in col:
                col.append(int(b1))
    col.sort()
    d=col[-1]+1
    return label,col,d,m
    
# insert values into the initialized data matrix
def insertvalue(fname,d,m):
    data=np.zeros((m,d))    
    row=0
    f=open(fname,'r')
    for line in f:
        line = line.strip()
        a=np.zeros
        a=line.split()
        for v in a[1:]:
            (idx,val)= v.split(':')
            idx=int(idx);val=float(val)
            column=idx
            data[row,column]=val
        row=row+1
    return data[:,1:]



# given a point x in test data and a list of points y in training data, 
# get the distance matrix and find the k nearest neighbors, 
# then predict the class x belongs to, 
# and determine the correctness of prediction
def D(x,xlab,y,ylab,k):
    d=x.shape[0]
    m=y.shape[1]
    n=y.shape[0]
    assert(d==m) 
    
    # get the distance array for point x vs list of points y
    e=np.tile(x,n).reshape(n,d)
    dist=np.sqrt(np.sum(np.square(e-y),axis=1))
    
    if k==1:
        predict=ylab[dist.argmin()]
    else:
        nb=zip(ylab,dist)
        dtype=[('index',int),('distance',float)]
        nb=np.sort(np.array(nb,dtype=dtype),order='distance')[:k]
        nb=np.array(zip(*nb)[0])
        pre={}
        for lab in ylab:
            p=len(nb[nb==lab])
            pre[lab]=p

        #print xlab,pre
        # randomly pick a predicted class "predict" to be 1,2,or 3
        # look at the counts of other classes
        # if counts of other classes larger than count of "predict"
        # set "predict" as that other class
        predict=rand.randint(1,4);count=pre[predict]
        for i in pre.keys():
            if pre[i]>count:
                predict=i
    # return 1 if prediction is correct; 0 otherwise    
    if predict==xlab:
        return 1
    else:
        return 0


# calculate the correct rate of knn classifier 
# given different k and different test data sets
def knn(train,test,k,num):
    f=train[:,1:];flab=train[:,0]
    c=0.0;ic=0.0 # initialize correct & incorrect counts
    for i in xrange(test.shape[0]):
        g=test[i,1:];glab=test[i,0]
        if (D(g,glab,f,flab,k)):
            c=c+1
        else:
            ic=ic+1
    correct_rate=c/(c+ic)
    print "test group={0:d},k={1:d},correct rate={2:.2f}".format(num,k,correct_rate)



# training data group1:
n1=7000;u11=0;u21=0;std11=1;std21=1;lab1=1
train1=binormal(n1,u11,u21,std11,std21,lab1)
# training data group2:
n2=1000;u12=1;u22=0;std12=np.sqrt(0.1);std22=1;lab2=2
train2=binormal(n2,u12,u22,std12,std22,lab2)
# training data group3:
n3=2000;u13=1;u23=1;std13=np.sqrt(2);std23=np.sqrt(2);lab3=3
train3=binormal(n3,u13,u23,std13,std23,lab3)
# training data combined together:
train=np.vstack((train1,train2,train3))

# plot training data:
plt.figure()
plt.scatter(train1[:,1],train1[:,2],color='b')
plt.scatter(train2[:,1],train2[:,2],color='r')
plt.scatter(train3[:,1],train3[:,2],color='g')
plt.show()


# test data group1:
nn1=100;uu11=0;uu21=0;stdd11=1;stdd21=1;labb1=1
test1=binormal(nn1,uu11,uu21,stdd11,stdd21,labb1)
# test data group2:
nn2=100;uu12=1;uu22=0;stdd12=np.sqrt(0.1);stdd22=1;labb2=2
test2=binormal(nn2,uu12,uu22,stdd12,stdd22,labb2)
# test data group3:
nn3=100;uu13=1;uu23=1;stdd13=np.sqrt(2);stdd23=np.sqrt(2);labb3=3
test3=binormal(nn3,uu13,uu23,stdd13,stdd23,labb3)
# test data combined together
test=np.vstack((test1,test2,test3))

print "test data generated from normal distributions "
print "test group 0 = all test data"
print "test group 1 = normal w/ u=(0,0) & sigma=(1,0,0,1)2x2"
print "test group 2 = normal w/ u=(1,0) & sigma=(0.1,0,0,1)2x2"
print "test group 3 = normal w/ u=(1,1) & sigma=(2,0,0,2)2x2"

for k in xrange(1,6):
    print " "
    knn(train,test,k,0)
    knn(train,test1,k,1)
    knn(train,test2,k,2)
    knn(train,test3,k,3)
    


dna="dna.scale"; dnat="dna.scale.t"
alabel,acol,ad,am=read(dna)
tlabel,tcol,td,tm=read(dnat)
if ad <= td:
    d=td
else:
    d=ad
# data matrices of training and test sets
a=insertvalue(dna,d,m=am)
t=insertvalue(dnat,d,m=tm)
# label arrays of training and test sets
alabel=np.array(alabel).reshape(am,1)
tlabel=np.array(tlabel).reshape(tm,1)
# combine label and data part for easy process in knn calculation step
dnatrain=np.hstack((alabel,a))
dnatest=np.hstack((tlabel,t))



print "test data from LibSVM"
print "test group 0 = all test data"

for k in xrange(1,6):
    print " "
    knn(dnatrain,dnatest,k,0)




