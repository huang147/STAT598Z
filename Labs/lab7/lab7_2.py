print "Lab 7 Question 2"

import matplotlib.pyplot as plt
X = [1,2,3,4,5]
fX = [5,10,15,20,25]
gX = [1,4,9,16,25]
plt.plot(X, fX,'r')   
plt.plot(X, gX,'g')
plt.legend(('f(X)','g(X)'),'upper center',shadow=True, fancybox=True)
plt.ylim([1,25])
plt.grid(False)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('A Simple Plot')
plt.show()


