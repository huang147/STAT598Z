import numpy as np
import numpy.random as rand

# Given a list of unsorted numbers, this program first sorted it, then find the median

# define a quicksort function to sort a list 
def sort(a):
    n = len(a)
    if n <= 1: 
        return a    
    else:
        pivotIndex = int(n/2)
        pivot = a[pivotIndex]
        large = []
        small = []
        a.remove(pivot)
        for i in range(n-1):
            if a[i] <= pivot:
                small.append(a[i])
            else:
                large.append(a[i])
        a = sort(small) + [pivot] + sort(large) 
        return a


# define a function to find median from a sorted list
def medianFromSorted(a):
    n = len(a)
    if n == 0:
        print "array can not be empty!"    
    elif n == 1:
        median = a[0]        
    else:
        if n%2:
            median=a[n/2]
        else:
            median = float(a[n/2]+a[n/2-1])/2
    return median


# get median from a list (no matter sorted or not)
def median(a):
    a = sort(a)
    median = medianFromSorted(a)
    return median


# Test on several different lists to ensure correctness

b = [1,2,3,4,4,5]        
print "before sort:", b
b = sort(b)
print "after sort:", b 
print "median:", median(b)

b = [1,7,12,4,3,2,5]
print "before sort:",b
b = sort(b)
print "after sort:",b
print "median:", median(b)

# generate list b of random numbers
b = []
for i in xrange(10):
    v = rand.randint(100) 
    b.append(v)
print "before sort:", b
b = sort(b)
print "after sort:", b
print "median:", median(b)



