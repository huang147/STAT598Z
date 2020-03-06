

list = [10, 4, 5, 1, 3, 4, 5]
#print list[1]

#smallest = list[0]

#for i in range(0, len(list) -1 ):
#    if list[i] < smallest:
#        smallest = list[i]

#print smallest



def findmin(a):
    #less = []
    n = len(a)
    print a

    if n == 1:
        min = a[0]
        return min
    else:
        pindex = n/2
        pivot = a[pindex]
        for i in range(n-1):
            if a[i]> pivot:
	    	x = a[i]
            	a.remove(x)
	findmin(a)



listmin = findmin(list)
print listmin
