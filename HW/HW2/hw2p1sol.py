"""
Problem 1: Write a Python program which does the following in sequence:
* Creates a list x which contains the numbers [9, 10, 11, 12, 13, 14, 15, 16].
* Prints the last three elements of x.
* Prints out all the even numbers in x.
* Deletes all the even numbers from x and prints the resulting list.
* Bonus (no points): Create a tuple y from x. What happens when
you try to insert or delete elements from y?
"""

# Creates a list x which contains the numbers [9, 10, 11, 12, 13, 14, 15, 16]
x = [9, 10, 11, 12, 13, 14, 15, 16]

# Prints the last three elements of x
print x[-3:]

# Prints out all the even numbers in x.
for num in x:
	if num%2 == 0:
		print num,

# Deletes all the even numbers from x and prints the resulting list.
for idx, num in enumerate(x):
	if num%2 == 0:
		x.pop(idx)

# Bonus (no points): Create a tuple y from x. What happens when
# you try to insert or delete elements from y?	

y = tuple(x)

# Removing individual tuple elements is not possible, because
# tuples are immutable in Python 
