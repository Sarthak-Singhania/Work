def isprimeno(n):
    for i in range(2,a):
        if n%i==0:
            return False
        else:
            return True
def factors(n):
    l=[]
    for i in range(2,n):
        if n%i==0:
            l.append(i)
def perfect(n):
    l=[]
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return True
    else:
        return False
cont='y'
while cont!='n':
    option=(int(input('\n\t\t1)Prime Check\n\t\t2)Factors\n\t\t3)Perfect Number\n\n\t\tEnter the option number:')))
    if option==1:
        print(isprimeno(int(input('Enter a number:'))))
    elif option==2:
        print(factor(int(input('Enter a number:'))))
    elif option==3:
        print(perfect(int(input('Enter a number:'))))
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'
