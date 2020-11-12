f=open('file handling histogram.txt','w')
f.write(input('Enter a word: '))
f.close()
f=open('file handling histogram.txt','r')
words=f.read()
d={}
for i in words:
    d[i]=0
for i in words:
    d[i]+=1
print(d)