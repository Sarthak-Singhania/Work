l=[]
def push():
    l.append(input('Enter:'))
def pop1():
    l.pop(-1)
def pop2():
    l1=[]
    b=int(input('Enter:'))
    a=l.index(b)
    for i in range(-1,a+1):
        l1.append(l.pop(-1))
    l1.pop(-1)
    for j in range(len(l1),0,-1):
        l.append(l1.pop(-1))
def peek():
    print(l[-1])
def display():
    print(l)
cont='y'
while cont!='n':
    option=(int(input('\n\t\t1)Push\n\t\t2)Pop\n\t\t3)Peek\n\t\t4)Display\n\t\tEnter the option number:')))
    if option==1:
        push()
    elif option==2:
        if len(l)!=0:
            op=int(input('\n\t\t1)Pop top elementn\n\t\t2)Pop any other element\n\t\tEnter the option number:'))
            if op==1:
                pop1()
            elif op==2:
                pop2()
        else:
            print('Stack is underflow')
    elif option==3:
        if len(l)!=0:
            peek()
        else:
            print('Stack is underflow')
    elif option==4:
        if len(l)!=0:
            display()
        else:
            print('Stack is underflow')
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'