#!/opt/epd/bin/python

from random import randint

print "I have a card in mind. Let's see if you are smart."

# randomly generate the sign (an integer in 1-4) and number (an integer in 1-13)
sign = randint(1, 4)
number = randint(1, 13)

# first guess the sign
while 1: # make sure the guessing goes on until get to the right answer
	a = raw_input("Enter your guess for the sign(integer, 1-4):") 
	a = int(a)
	if a < 1 or a > 4:
		print "Your guess should be an integer between 1 and 4!"
	elif a == sign:
		print "Bingo!"
		break # jump out of the 1st while loop and finish guessing sigh
	elif a > sign:
		print "Sorry your guess is too high"		
	else: 
		print "Sorry your guess is too low"

print "Now guess the number."

# next guess the number 
while 1: # make sure the guessing goes on until get to the right answer
	b = raw_input("Enter your guess for the number(integer, 1-13):")
	b = int(b)
	if b < 1 or b > 13:
		print "Your guess should be an integer between 1 and 13!"
	elif b == number:
		print "Bingo!"
		break
	elif b > number: 
		print "Sorry your guess is too high"
	else: 
		print "Sorry your guess is too low"











