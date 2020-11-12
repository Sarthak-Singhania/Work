a=input("Enter a number you want to check:")
b=''
for i in range(len(a)-1,-1,-1):
    b+=a[i]
if b==a:
    print('It is a pallindrome.')
else:
    print('It is not a pallindrome.')