def bubblesort(l):
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
def binary(L):
    A=sorted(L)
    x=1
    f=0
    l=len(A)-1
    found=0
    while f<=l:
        m=(f+l)//2
        if L[m]==x:
            found=1
            break
        elif L[m]<x:
           f=m+1
        else:
            l=m-1
    if found==0:
        return False
    else:
        return True
def linear():
    def search(l,n,x):
        for i in range (n): 
            if l[i]==x: 
                return i
        return -1
    a=list(map(int,input('Enter the numbers:').split()))
    l=sorted(a)
    x=int(input('Enter a number:')
    n=len(l); 
    result=search(l,n,x) 
    if result==-1: 
        return False
    else: 
        return True

