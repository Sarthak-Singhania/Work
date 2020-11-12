a=input("Enter a number:")
b=int(len(a))
c=0
if b%2==0:
    a1=a[1:-1]
    a2=a[0]
    a3=a[-1]
    num=int(a1)
    while num!=0:
        d=num%10
        c=c*10+d
        num//=10
    a4=str(c)
    print(''.join(a2+a4+a3))
else:
    a1=a[1:-1]
    a2=a[0]
    a3=a[-1]
    num=int(a1)
    while num!=0:
        d=num%10
        c=c*10+d
        num//=10
    a4=str(c)
    print(''.join(a2+a4+a3))