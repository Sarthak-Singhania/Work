a=rev=num=int(input("Enter a number to check for pallinprime number:"))
c=0
if a==2 or a==3 or a==5 or a==7:
    print("It is a prime number. It is a single digit number.")
else:
    for i in range(2,a):
        if (a % i) == 0:
            print(a,"is not a prime number")
            break
    else:
        while num!=0:
            b=num%10
            c=c*10+b
            num//=10
        if c==rev:
            print("It is not a pallinprime number.")
        else:
            print("It is a pallinprime number.")