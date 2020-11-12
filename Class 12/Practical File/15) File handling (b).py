f=open('myfile.txt','r')
a=f.read()
l=a.split()
d={}
for i in l:
    num=[]
    for j in l:
        if len(i)==len(j):
            num.append(j)
    d[len(i)]=num
print('Dictionary:',d)
def find_longest_word():
    return d[max(d)]
print('List of longest words:',find_longest_word())
def filter_long_words(n):
    l=[]
    for x in d:
        if x>n:
            l.append(x)
    return l
print(filter_long_words(int(input('Enter the number for words longer:'))))
f1=open('newfile.txt','a')
for x in filter_long_words(8):
    f1.write(x)
f.close()
f1.close()
