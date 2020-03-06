s = raw_input("Enter the word to be checked: ")
b = True
for i in range(len(s)/2):
  if s[i]!=s[-i-1]:
    b = False
    break
    
if b == True:
     print"Yes, it’s a palindrome"
else:
     print "This is not a Palindrome"
        
