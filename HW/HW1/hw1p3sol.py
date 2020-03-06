import random as rand

rand.seed(1245)
# Generate a random card
# First the sign
sign=rand.randint(1,4)
# Then the number
num=rand.randint(1,26)

print "I have a card in mind. Let us see if you can guess it."

# Let the user guess the sign first
flag_sign=False
while flag_sign==False:
    a=raw_input("Enter your guess for the sign:")
    if int(a) < sign:
        print "Sorry your guess is too low"
    elif int(a) > sign:
        print "Sorry your guess is too high"
    elif int(a) == sign:
        print "Bingo"
        flag_sign=True

# Let the user guess the number next 
flag_num=False
while flag_num==False:
    a=raw_input("Enter your guess for the number:")
    if int(a) < num:
        print "Sorry your guess is too low"
    elif int(a) > num:
        print "Sorry your guess is too high"
    elif int(a) == num:
        print "Bingo"
        flag_num=True


    
