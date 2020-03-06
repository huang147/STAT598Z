"""
Problem 2 : Write a Python program which takes as input an integer n
and computes \sum_i^n (1/2)^i in three ways: using a for loop, using a while
loop, and without using a loop (e.g., by using an analytic formula). Print
out all three results. What happens when n is very large? Do you have
any suggestions on how to make your program more robust to errors when
n is large?
"""

# Note, we assumed i will start from 1.
n = int(raw_input("Enter a value for n: "))

# using a for loop
def for_sum(n):
	result = 0
	for i in range(1, n+1):
		result+= (.5)**i
	return result

print "Calculating for n = {0} with for loop, result = {1}".format(n, for_sum(n)) 

# using a while loop 
def while_sum(n):
	result = 0
	i = 1
	while(i <= n):
		result+= (.5)**i
		i+= 1
	return result

print "Calculating for n = {0} with while loop, result = {1}".format(n, while_sum(n)) 

# using an analytic formula
def analytic_sum(n):
	return 1-2**(-n)

print "Calculating for n = {0} with analytic formula, result = {1}".format(n, analytic_sum(n))

# When n is very large, the result gets too large to fit into a float variable 
# in Python, therefore Python interpreter rounds the result to 1. 
# Read more about limitations of Floating Point Arithmetic: 
# http://docs.python.org/2/tutorial/floatingpoint.html#tut-fp-issues 
# http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
