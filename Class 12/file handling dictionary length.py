f=open('file handling dictionary length.txt','w')
f.write(input('Enter a sentence: '))
f.close()
f=open('file handling dictionary length.txt','r')
words=f.read()
l=words.split()
d={}
d[len(l[0])]=[l[0]]
for i in range(1,len(l)):
    if len(l[i]) in d:
        d[len(l[i])].append(l[i])
    else:
        d[len(l[i])]=[l[i]]
print(d)