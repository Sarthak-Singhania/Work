#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Student
#
# Created:     11/05/2018
# Copyright:   (c) Student 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from os import system
system("cls")
b=0
ch='y'

while ch=='y':
    system("cls")
    b+=1
    a=raw_input("Enter an operation(+,-,*,/):")
    if a=='+':
            system("cls")
            num1=input("Enter 1st number:")
            num2=input("Enter 2nd number:")
            print "The answer is: ", num1+num2
    elif a=='-':
            system("cls")
            num1=input("Enter 1st number:")
            num2=input("Enter 2nd number:")
            print "The answer is: ", num1-num2
    elif a=='*':
            system("cls")
            num1=input("Enter 1st number:")
            num2=input("Enter 2nd number:")
            print "The answer is: ", num1*num2
    elif a=='/':
            system("cls")
            num1=input("Enter 1st number:")
            num2=input("Enter 2nd number:")
            if num2==0:
                print "You have entered 0, the answer is not defined."
            else:
                print "The answer is: ", num1/num2
    else:
            print "Invalid input!!"
    if b==3:
        break

    ch=raw_input("Do you want to continue(y/n):")
print "You have used the calculator",b,"times."