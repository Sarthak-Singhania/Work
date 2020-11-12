a=input('Enter:')
b=input('Find:')
for i in range(len(a)):
    flag=0
    for j in range(len(b)):
        if a[i+j]!=b[j]:
            flag=1
            break
    if flag==0:
        break
if flag==0:
    print (b,"found at",i+1)
else:
    print (b,"not found")