import numpy as np
import matplotlib.pyplot as plt

str=raw_input('Enter a string: ')
width=0.2
acount=str.count('a')
ecount=str.count('e')
icount=str.count('i')
ocount=str.count('o')
ucount=str.count('u')

count=[acount,ecount,icount,ocount,ucount]
index=np.arange(5)
plt.bar(index,count,width,color='r')
plt.xticks(index+width/2., ('A', 'E', 'I', 'O', 'U') )
plt.xlabel('Vowels')
plt.ylabel('Distribution')
plt.title('frequency of occurrence of vowels in string '+str)
plt.show()

            
