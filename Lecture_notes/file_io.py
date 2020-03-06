# Python can also be used to open files and read in the contents 
fname="test.txt"

# Using "r" indicates that we want to read this file 
# If you want to write into a file then use "w" 
f=open(fname, "r")

for l in f:
    # Remove any extra whitespace 
    l=l.strip()
    print l
