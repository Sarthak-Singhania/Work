f=open('myfile.txt','w')
f.write(input('Enter a sentence:'))
f.close()
f=open('myfile.txt','r')
a=f.read()
l=a.split()
d={}                            #histogram
for i in l:
    d[i]=0
for x in l:
    d[x]+=1
v=list(d.values())
k=list(d.keys())
print('Total number of words are',sum(v))           #part 1
print('Number of different words are',len(k))
print('The most common word is',k[v.index(max(v))])
d={}
d[len(l[0])]=[l[0]]
for i in range(1,len(l)):
    if len(l[i]) in d:
        d[len(l[i])].append(l[i])
    else:
        d[len(l[i])]=[l[i]]
print(d)
def find_longest_word():
    print('The longest words are:',d[max(d)])
find_longest_word()
def filter_long_words(n):
    for i in d:
        if i>n:
            return ' '.join(map(str,d[i]))
f1=open('newfile.txt','w')
f1.write(filter_long_words(int(input('Enter the number:'))))
find_longest_word()
f.close()
f1.close()
