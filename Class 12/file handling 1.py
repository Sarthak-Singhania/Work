f=open('file handling 1.txt','w')
f.write(input('Enter a sentence: '))
f.seek(0)
words=f.read()
l=words.split()
print(len(l))
f.close()
f=open('1.txt','a')
f.write(input())
f.close()