#n = input("Please put in an integer:")
#m = int(n/2)
#print "n/2", m

def quicksort(a):
    n = len(a)
    
    if n ==1:
        return a
    else:
        