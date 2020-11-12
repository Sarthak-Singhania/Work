num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))
op=input("Enter operator(+,-,*,/,%):")
result=0
if op=='+':
    result=num1+num2
    print(num1,op,num2,"=",result)
elif op=='-':
    result=num1-num2
    print(num1,op,num2,"=",result)
elif op=='*':
    result=num1*num2
    print(num1,op,num2,"=",result)
elif op=='/':
    if num2==0:
        print("The 2 nd number can not be 0")
    else:
        result=num1/num2
        print(num1,op,num2,"=",result)
elif op=='%':
    if num2==0:
        print("The 2 nd number can not be 0")
    else:
        result=num1%num2
        print(num1,op,num2,"=",result)
else:
    print("Invalid Operator")