from os import system
system('cls')
a=input("Enter an operation(+,-,*,/,%):")

if a=='+':
    system('cls')
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))
    print("The answer is:",num1+num2)
if a=='-':
    system('cls')
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))
    print("The answer is:",num1-num2)
if a=='*':
    system('cls')
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))
    print("The answer is: ",num1*num2
if a=='/':
    system('cls')
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))
    if num2==0:
        print("You have entered 2nd number as 0 which is not defined.")
    else:
        print("The answer is:",num1/num2)
if a=='%':
    system('cls')
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))
    if num2==0:
        print("You have entered 2nd number as 0 which is not defined.")
    else:
        print("The answer is: ",num1%num2)
else:
    print(" INVALID INPUT!!!")
