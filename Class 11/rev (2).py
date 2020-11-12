a=rev=int(input("Enter the number you want to to check for pallandrom number:"))
c=0
while a!=0:
    b=a%10
    c=c*10+b
    a//=10
if c==rev:
    print('It is a pallindrome.')
else:
    print('It is not a pallidrome.')