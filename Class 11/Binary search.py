L=[5,6,8,3,1,2]
A=sorted(L)
x=10
f=0
l=len(A)-1
found=0
while f<=l:
    m=(f+l)//2
    if A[m]==x:
        found=1
        break
    elif A[m]<x:
       f=m+1
    else:
        l=m-1
if found!=0:
    print('Found',x,'at',m+1)
else:
    print('Not found')