a=input('Enter a sentence:')
cnt=0
l=[]
b=''
for i in range(len(a)):
    if a[i]!=' ':
        b+=a[i]
    else:
        l.append(len(b))
        print(b,'-',l[cnt])
        cnt+=1
        b=''
l.append(len(b))
print(b,'-',l[cnt])