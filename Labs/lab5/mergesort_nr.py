import numpy as np
import numpy.random as rand

# Merge sort without recursion 
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

# Logic:
# Merge blocks of size 1. This will ensure that every adjacent
# pair of elements in the array is sorted.
# Then merge all blocks of size 2. This will ensure that every adjacent
# set of 4 elements in the array is sorted and so on
# Finish when entire array is sorted.

# To check what is happening uncomment the print and verify that the
# logic is being implemented. 

# m indicate the size of the blocks being merged

def merge_sort_nr(a):
    n=len(a)
    m=1
    while m <= n:
        i=0
        while i<(n-m):
            low=i
            mid=i+m
            high=min(i+2*m,n)
            a[low:high]=merge(a[low:mid], a[mid:high])
            i+=2*m
        # print a 
        m*=2
    return a

rand.seed(123)
a=rand.randint(low=0,high=100,size=10)
print "before sort:", a
a=merge_sort_nr(a)
print "after sort:", a
