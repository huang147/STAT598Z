# Solution HW 1, Problem 2

import string

# problem 2(1)
def m2k(a):
    a=float(a)
    if a<0:
        print "Error: Input distance has to be non-negative"
    else:
        b=a*1.609334
        print "{0} miles is {1} kilometers".format(a,b)

def k2m(a):
    a=float(a)
    if a<0:
        print "Error: Input distance has to be non-negative"
    else:
        b=a/1.609334
        print "{0} kilometers is {1} miles".format(a,b)

# problem 2(2)
def m2k_table():
    for a in range(100):
        m2k(a)

# m2k_table()     
arg=raw_input("Please input m2k or k2m: ")
# print arg
if arg=="m2k":
    print "Converting from miles to kilometers"
    
    a=raw_input("Please enter distance in miles: ")
    while (a != "q"):    
        m2k(a)
        a=raw_input("Please enter distance in miles: ")

if arg=="k2m":
    print "Converting from kilometers to miles"
    
    a=raw_input("Please enter distance in kilometers: ")
    while a !="q":
        k2m(a)
        a=raw_input("Please enter distance in kilometers: ")

print('Bye Bye\n')

