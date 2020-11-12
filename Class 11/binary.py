a=100
b=''
c=''
while a!=0:
    b+=str(a%2)
    a//=2
for i in range(len(b)-1,-1,-1):
    c+=b[i]
print(c)
