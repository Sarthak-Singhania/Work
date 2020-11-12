a=input('Enter:')
b=input('Find:')
cnt=0
for i in range(len(a)):
    flag=0
    for j in range(len(b)):
        if a[i+j]!=b[j]:
            flag=1
            break
    if flag==0:
        cnt+=1
        print(b,'has been found at',i+1)
if len(b)>1:
    print('The word',b,'has occured',cnt,'times')
else:
    print('The letter',b,'has occured',cnt,'times')