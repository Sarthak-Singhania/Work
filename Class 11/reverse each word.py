a=input()
a+=' '
b=''
c=''
d=''
for i in range(len(a)):
    if a[i]!=' ':
        b+=a[i]
    else:
        for y in range(len(b)-1,-1,-1):
            c+=b[y]
        d+=c
        d+=' '
        c=''
        b=''
print(d)