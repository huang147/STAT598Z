f_old=open('hamlet.txt',"r")
f_new=open('newhamlet.txt',"w")
line_number=1
for line in f_old:
    f_new.write("{0:d},{1:s}".format(line_number, line))
                
    line_number=line_number+1

f_test=open('newhamlet.txt',"r")

for line in f_test:
        print line,

f_test.close()
