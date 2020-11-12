l=[1,2,3,4,5,6,7,8,9,0]
b=len(l)-1
a=int(input('Enter a number:'))
loc=int(input('Enter the location:'))
loc-=1
while loc<b:
    l[b]=l[b-1]
    b-=1
l[b]=a
print(l)