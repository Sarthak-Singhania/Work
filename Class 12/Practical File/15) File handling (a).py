f=open('myfile.txt','r')
a=f.read()
l=a.split()
d={}
for x in l:
    d[x]=0
for x in l:
    d[x]+=1
def maxword():
    global d
    d1={}
    w=d.values()
    b=d.keys()
    for x in range(len(d)):
        d1[w[x]]=b[x]
    return tuple(d1[max(w)])
print('Total number of words:',sum(d.values()))
print('Number of different words:',len(d))
print('The most common words:',maxword())
