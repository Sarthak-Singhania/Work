f=open('file handling reversing words.txt','w+')
f.write(input('Enter a sentence: '))
f.seek(0)
words=f.read()
f.close()
words+=' '
b=''
c=''
d=''
for i in range(len(words)):
    if words[i]!=' ':
        b+=words[i]
    else:
        for y in range(len(b)-1,-1,-1):
            c+=b[y]
        d+=c
        d+=' '
        c=''
        b=''
f=open('file handling reversed words.txt','w+')
f.write(d)
f.seek(0)
print(f.read())