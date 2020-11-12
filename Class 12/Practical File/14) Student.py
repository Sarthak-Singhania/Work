f=open('14) Student.txt','r')
l=f.readlines()
l1=[]
for x in l:
    l1.append(tuple(x,))
print(l1)
