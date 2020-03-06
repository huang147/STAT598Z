import numpy as np
import numpy.random as rand

def insertion_sort(a):
    n=len(a)
    for j in range(n):
        key=a[j]
        i=j-1
        while (i>=0) and (a[i]>key):
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    return a

array1=[1, 4, 7, 9, 2, 4, 6, 11, 12]
print "before sort: ",array1
b=insertion_sort(array1)
print "after sort: ",b

rand.seed(123)
a=rand.randint(low=0,high=100,size=10)
print "before sort:", a
a=insertion_sort(a)
print "after sort:", a
