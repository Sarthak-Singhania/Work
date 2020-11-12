a=rev=input("Enter the number for which you want to check that if it is a pallandrom number or not: ")
c=0
while a!=0:
    b=a%10
    c=c*10+b
    a=a/10
if rev==c:
    print("It is a pallandrom number.")
else:
    print("It is not a pallandrom number.")
