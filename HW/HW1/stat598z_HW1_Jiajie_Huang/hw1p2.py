#!/opt/epd/bin/python 

# gtol and ltog initialized as 0 and will change due to user input
gtol = 0
ltog = 0

def g2l(v1):
	v2 = v1 * 3.78541178 # convert gallons to liters
	print v1, "gallons is", v2, "liters"
	return v1, v2

def l2g(w1):
	w2 = w1 * 0.264172 # convert liters to gallons
	print w1, "gallons is", w2, "liters"
	return w1, w2


while 1: # make sure the input goes on until gets the valid input 
	# first indicate the type of convertion: gtol, ltog, or q as exit
	convert=raw_input("Please input gallons to liters (gtol) or liters to gallons (ltog)(press q to exit): ")

	if convert == "q":
		print "Bye!"
		break # jump out of while loop, end the program
	elif convert == "gtol":
		gtol = 1
		break # jump out of while loop, change gtol to 1 for the convertion step
	elif convert == "ltog":
		ltog = 1
		break # jump out of while loop, change ltog to 1 for the convertion step
	else: 
		print "Invalid input! (gtol: gallons to liters; ltog: liters to gallons; q: exit)"

# then consider the gallons to liters convertion if indicated by user
if gtol == 1:
	print "Converting gallons to liters"
	while 1: # make sure the program runs until getting the valid input
		v1 = raw_input("Please input volume in gallons (non-negative numbers or q as exit):")
		if v1 == "q":
			print "Bye!!"
			break # jump out, end the program
		v1 = float(v1)
		if v1 >= 0:
			#v2 = v1 * 3.78541178 # convert gallons to liters
			#print v1, "gallons is", v2, "liters"
			g2l(v1)
			break
		else: # restate the valid input type and start over
			print "Invalid input! (input must be non-negative numbers)"


# or consider the liters to gallons convertion if indicated by user		
if ltog == 1:
	print "Converting liters to gallons"

	while 1: # make sure the program runs until getting the valid input
		w1 = raw_input("Please input volume in liters (non-negative numbers or q as exit):")
		if w1 == "q":
			print "Bye!!"
			break # jump out, end the program
		w1 = float(w1)
		if w1 >= 0:
			#w2 = w1 * 0.264172 # convert liters to gallons
			#print w1, "gallons is", w2, "liters"
			l2g(w1)
			break
		else: # restate the valid input type and start over
			print "Invalid input! (input must be non-negative numbers)"



