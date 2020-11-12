from random import randint
l=[]
def new_order():
    global l
    l.append(randint(100,999))
def diqueue():
    global l
    return l.pop()
def display():
    global l
    print(l)
while True:
    option=(int(input('\n1)Order a meal\n2)Order is ready\n3)Waiting Queue\n4)Exit\nEnter the option number:')))
    if option==1:
        new_order()
    elif option==2:
        print(diqueue())
        if len(l)==0:
            print('Stack is underflow')
    elif option==3:
        if len(l)!=0:
            display()
        else:
            print('Stack is underflow')
    elif option==4:
        break