def search(l,n,x): 
    for i in range (n): 
        if l[i]==x: 
            return i
    return -1
a=[2,3,10,40,4]
l=sorted(a)
x=10
n=len(l); 
result=search(l,n,x) 
if result==-1: 
    print('Not found')
else: 
    print('Found',x,'at',result+1)