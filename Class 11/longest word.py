a=input('Enter a sentence:')
b=''
lenght=0
cnt=0
for i in range(len(a)):
    if a[i]!=' ':
        b+=a[i]
    else:
        if len(b)>lenght:
            lenght=len(b)
        else:
            break
        b=''
print(b)