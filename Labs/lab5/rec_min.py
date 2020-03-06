# Two different ways of recursively finding the minimum element in a
# list 

# Compare the last element and the minimum of the remaining elements
def rec_min1(x):
    if len(x) == 1:
        return x[0]
    else:
        return min(x[-1], rec_min1(x[:-1]))

print rec_min1((10,4,5,1,3,4,5))

# Split the array into two and compare the minimum of the two halves
def rec_min2(x):
    n=len(x)
    if n == 1:
        return x[0]
    else:
        return min(rec_min2(x[:n/2]), rec_min2(x[n/2:]))
        
print rec_min2((10,4,5,1,3,4,5))
