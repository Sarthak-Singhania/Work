a=input()
b=input()
c=len(b)
for i in range(len(a)):
    d=''
    d+=a[i:i+c]
    if d==b:
        print('yes at',i+1)
        break