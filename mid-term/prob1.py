s = raw_input("Enter the word to be checked: ")
b = True
for i in range(len(s)/2):
  if s[i]!=s[-i-1]:
    b = False
    
if b == True:
     print"Yes, it’s a palindrome (using for loop) "
else:
     print "This is not a Palindrome (using for loop) "


while i<=(len(s)/2):
  if s[i]!=s[-i-1]:
    b = False
  i+=1
    
if b == True:
     print"Yes, it’s a palindrome (using while loop) "
else:
     print "This is not a Palindrome (using while loop) "
     
