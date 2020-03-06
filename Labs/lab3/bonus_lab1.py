
def isdivisor(a,b):
    a = int(a)
    b = int(b)
    if a%b ==0:
        print "{0} is divisble by {1}".format(a,b)
    else:
        print "{0} is not divisble by {1}".format(a,b)

print "Enter the first number as q to exit"
a = raw_input("Please enter the first number ")
b = raw_input("Please enter the second number ")
while a !="q":
    isdivisor(a,b)
    a = raw_input("Please enter the first number ")
    b = raw_input("Please enter the second number ")

print('Bye Bye\n')
