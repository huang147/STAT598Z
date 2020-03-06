print "lab 4 question 5"

n=1
max=0
min=0
count=0
sum=0
values=[]
print("Enter zero when you want to exit")

while (n!=0):
        n=input("Enter an integer")
        if isinstance(n,int)!= 1:
                print "not an integer"
                break
                        
        if n!=0:
            count =count+1
            sum=sum+n
            values.append(n)
            if n>max:
                max=n
            if count==1:
                min=n
            elif n<min:
                 min=n

print "The values entered are: " , values
print "The maximum is:", max
print "The minimum is:", min
print "The mean is: ", float(sum/count)
values.sort()
print "The sorted values are: " , values
if count%2==1:
        print "The median is: ",values[(count-1)/2]
else:
        print "The median is: ", 0.5*(values[count/2]+values[count/2-1])
        
