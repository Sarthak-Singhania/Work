l=[]
def enqueue():
    global l
    l.append(int(input('Enter:')))
def diqueue():
    global l
    l.pop(0)
def peek():
    global l
    print(l[0])
def display():
    global l
    print(l)
while True:
    option=(int(input('\n\t\t1)Enqueue\n\t\t2)Diqueue\n\t\t3)Peek\n\t\t4)Display\n\n\t\tEnter the option number:')))
    if option==1:
        enqueue()
    elif option==2:
        diqueue()
        if len(l)==0:
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
        break