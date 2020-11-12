f=open('12) text handling 1.txt','r')
a=f.read()
l=a.split()
d={}
for x in l:
    d[x[0]]=0
for x in l:
    d[x[0]]+=1
for i in d:
    print('Words beginning with',i,':',d[i])
