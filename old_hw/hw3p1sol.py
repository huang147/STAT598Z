def is_sorted(d):
    sorted=True
    for i in range(1, len(d)):
        if d[i - 1] > d[i]:
            sorted=False
    return sorted

def swap(d, i, j):
    tmp=d[i]
    d[i]=d[j]
    d[j]=tmp

def bubble_sort(data):
    swapped=True
    while swapped==True:
        swapped=False
        for i in range(1, len(data)):
            if data[i - 1] > data[i]:
                swap(data, i-1, i)
                swapped=True
                
x=[10, 10, 5, 6, 10, 3, 4, 31, 0, -2, 5]
print is_sorted(x)
bubble_sort(x)
print is_sorted(x)
print x
