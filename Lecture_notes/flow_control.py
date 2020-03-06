## If and Else statements:
a=0

if a > 1:
    print "a > 1"
else:
    print "a <= 1"

if a> 1:
    print "do something"


x=37
if x>10:
    y=35
    z=24
else:
    y=12
    z=45
print y


## For loop 
x=36
for x in range(10):
    print x

for x in range(10):
    x = 3.9 * x * (1 - x)
    print x
    
# While loop

a=0
while a < 10:
    a=a+1
    print a

x=1
z=12
y=31
if y==21:
    print y

while ((x<10) or (z>6)) and y<15:
    print x
    x=x+12

for x in range(10):
    if x<2:
        print x
    else:
        print x+3
        
# More information about Python's built-in functions such as range can
# be found at http://docs.python.org/library/functions.html
