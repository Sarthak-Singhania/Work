f=open('file1.txt','r')
a=f.read()
l=a.split()
vowel='aeiouAEIOU'
for x in l:
    if x[0] not in vowel:
        f1=open('file2.txt','a')
        f1.write(x+' ')
f.close()
print(f.read())
f1.close()
