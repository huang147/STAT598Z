import random as rand
import string

def feedback(a,t):
    if a==t:
        print "Bingo!"
        return 0
    else:
        feed_t=rand.randint(1,3)
        if feed_t<3:
            if a<t:
                print "Sorry your guess is too low"
            else:
                print "Sorry your guess is too high"
        else:
            if a>t:
                print "Sorry your guess is too low"
            else:
                print "Sorry your guess is too high"
        return -1


dict={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

ti=rand.randint(1,26)
tv=dict[ti]
print "I am ready to play. I have a letter between \"a\" and \"z\" in mind"
a=raw_input("Enter your guess: ")
f=feedback(a,tv)
while f!=0:
    a=raw_input("Enter your guess:")
    f=feedback(a,tv)
    
