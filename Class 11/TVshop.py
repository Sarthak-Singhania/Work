from time import sleep
from os import system
system("color 1e")
system("title TV Sales Billing")
print("Welcome to TV shop")
sleep(2)
system("cls")
tvcnt=int(input("How many TV(s) do you want \n(1) Single TV \n(2) Multiple TV(s) (Get a discount) \nEnter your option:"))
if tvcnt==1:
    system("cls")
    tvclr=int(input("What type of TV do you want \n(1) Colour TV \n(2) B/W TV \nEnter your option:"))
    if tvclr==1:
        system("cls")
        size=int(input('We have the following TV sizes: \n(1) 32"\n \n(2) 40"\n \n(3) 42"\n \nEnter the size:'))
        if size==1 or 32:
            system("cls")
            print("Your total bill is of Rs. 5000")
            sleep(5)
        elif size==2 or 40:
            system("cls")
            print("Your total bill is of Rs. 6000")
            sleep(5)
        elif size==3 or 42:
            system("cls")
            print("Your total bill is of Rs. 7000")
            sleep(5)
        else:
            system("cls")
            print("This is a invalid input.")
    if tvclr==2:
        system("cls")
        size=int(input('We have the following TV sizes: \n(1) 32"\n \n(2) 40"\n \n(3) 42"\n \nEnter the size:'))
        if size==1 or 32:
            system("cls")
            print("Your total bill is of Rs. 3000")
            sleep(5)
        elif size==2 or 40:
            system("cls")
            print("Your total bill is of Rs. 4000")
            sleep(5)
        elif size==3 or 42:
            system("cls")
            print("Your total bill is of Rs. 5000")
            sleep(5)
        else:
            system("cls")
            print("This is a invalid input.")
    else:
        system("cls")
        print("This is an invalid input.")
if tvcnt==2:
    system("cls")
    clrtv=int(input("How many Colour TV(s) do you want? \nEnter the number of TV(s): "))
    bwtv=int(input("How many B/W TV(s) do you want? \nEnter the number of TV(s): "))
    system("cls")
    if clrtv>0:
        size1=int(input('We have the following TV sizes for Colour TV: \n(1) 32"\n \n(2) 40"\n \n(3) 42"\n \nEnter the size:'))
        if size1==1 or 32:
            cost1=5000
        elif size1==2 or 40:
            cost1=6000
        elif size1==3 or 42:
            cost1=7000
        else:
            system("cls")
            print("This is a invalid input.")
        if clrtv==1:
            dis1=0.15
        else:
            dis1=0.2
        clrcostraw=clrtv*cost1
        clrcost=clrcostraw-(clrcostraw*dis1)
        dist=dis1
        bwcost=0
    else:
        system("cls")
        print("This is a invalid input.")
    if bwtv>0:
        size2=int(input('\nWe have the following TV sizes for B/W TV: \n(1) 32"\n \n(2) 40"\n \n(3) 42"\n \nEnter the size:'))
        if size2==1 or 32:
            cost2=3000
        elif size2==2 or 40:
            cost2=4000
        elif size2==3 or 42:
            cost2=5000
        else:
            system("cls")
            print("This is a invalid input.")
        if bwtv==1:
            dis2=0.10
        else:
            dis2=0.15
        bwcostraw=bwtv*cost2
        bwcost=bwcostraw-(bwcostraw*dis2)
        dist=dis1+dis2

    system("cls")
    print("Total discount given to you is ",(dist)*100,"%")
    print("The cost for Colour TVs  after discount is Rs. ",clrcost)
    print("The cost for B/W TVs after discount is Rs. ",bwcost)
    print("Your total bill is of Rs. ",clrcost+bwcost)
    sleep(10)

else:
    system("cls")
    print("This is a invalid input.")
system("cls")
print("Thank you for using the billing software made by Sarthak Singhania.")
sleep(3)