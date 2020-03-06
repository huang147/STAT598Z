import numpy as np
import numpy.random as rand

def merge(a, b):
    n=len(a)
    m=len(b)
    c=np.zeros(n+m,dtype=np.int32)
    i=0
    j=0
    k=0
    while i<n and j<m:
        if a[i]<b[j]:
            c[k]=a[i]
            i=i+1
        else:
            c[k]=b[j]
            j=j+1
        k=k+1
    while i<n:
        c[k]=a[i]
        k=k+1
        i=i+1
    while j<m:
        c[k]=b[j]
        k=k+1
        j=j+1
    return c

def threewaymerge(a,b,c):
    d=merge(a,b);
    return merge(d,c)

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]

print threewaymerge(a,b,c)
