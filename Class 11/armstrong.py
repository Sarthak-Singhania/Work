for i in range(20,201):
    a=i
    c=0
    d=a
    while a!=0:
        b=a%10
        c+=b*b*b
        a//=10
    if c==d:
        print(i,"is an armstrong number.")