# Solution HW 1, Problem 2

import string
GALLON=3.78541178

# problem 2(1)
def gtol(a):
    a=float(a)
    if a<0:
        print "Error: Input has to be non-negative"
    else:
        b=a*GALLON
        print "{0} gallons is {1} liters".format(a,b)

def ltog(a):
    a=float(a)
    if a<0:
        print "Error: Input has to be non-negative"
    else:
        b=a/GALLON
        print "{0} liters is {1} gallons".format(a,b)

# problem 2(2)
def gtol_table():
    for a in range(100):
        gtol(a)

# gtol_table()     
arg=raw_input("Please input gallons to liters (gtol) or liters to gallons (ltog): ")
if arg=="gtol":
    print "Converting from gallons to liters"
    
    a=raw_input("Please enter volume in gallons: ")
    while (a != "q"):    
        gtol(a)
        a=raw_input("Please enter volume in gallons: ")

if arg=="ltog":
    print "Converting from liters to gallons"
    
    a=raw_input("Please enter volume in liters: ")
    while a !="q":
        ltog(a)
        a=raw_input("Please enter volume in liters: ")

print "Bye Bye"
