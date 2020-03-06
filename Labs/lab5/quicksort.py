
def quick_sort(a):
    n=len(a)
    #print "length",n
    if n<=1:
        return a
    else:
        pivotIndex=n/2
        pivotValue=a[pivotIndex]
        a.remove(pivotValue)
        #remove pivotValue from list
        less=[];greater=[]
        for x in a:
            if x<=pivotValue:
                less.append(x)
                #append x to less
            else:
                greater.append(x)
                #append x to greater
        a= quick_sort(less)+[pivotValue]+quick_sort(greater)
        #recursively sort less and greater
        return a


array1=[1.3, 4.5, 7, 9, 2, 4, 6, 11, 12]
print "before sort: ",array1
b=quick_sort(array1)
print "after sort: ",b

array2=[8, 7, 6, 5, 4, 3, 2, 1]
print "before sort",array2
b=quick_sort(array2)
print "after sort: ",b

