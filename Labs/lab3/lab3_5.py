import math
def is_prime(num):
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            return False
        return True

num = int(raw_input("Input any of the number you like:"))
if not is_prime(num):
    print "It is not a prime number"
else:
    print "It is a prime number"
