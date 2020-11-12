def count(a):
    cnt=0
    while a!=0:
        a//=10
        cnt+=1
    return cnt
def reverse(n):
    return int(n[::-1])
def hasdigit(n):
    num=input('Enter the number you want to check:')
    return num in n
def show(n):
    a=count(n)
    b=list(n)
    sum=0
    for x in b:
        a-=1
        sum+=int(x)*(10**a)
        if a==0:
            sum+=int(x)
    return sum
cont='y'
while cont!='n':
    option=(int(input('\n\t\t1)Count\n\t\t2)Reverse\n\t\t3)HasDigit\n\t\t4)Show\n\n\t\tEnter the option number:')))
    if option==1:
        print(count(int(input('Enter the number:'))))
    elif option==2:
        print(reverse(input('Enter the number:')))
    elif option==3:
        print(hasdigit(input('Enter the number:')))
    elif option==4:
        print(show(input('Enter the number:')))
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'
