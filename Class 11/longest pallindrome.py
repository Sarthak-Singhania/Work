a=input('Enter a sentence:')
b=''
c=''
lenght=0
for i in range(len(a)):
    if a[i]!=' ':
        b+=a[i]
        if len(b)>lenght:
            lenght=len(b)
    else:
        b=''
for j in range(len(b)-1,-1,-1):
    c+=b[j]
if c==b:
    print('It is a pallindrome.')
    print(lenght)
    print(b)
else:
    print('It is not a pallindrome.')