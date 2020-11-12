def sorting(l1,l2):
    l=l1+l2
    return sorted(l)
def commonsum(l1,l2):
    sum=0
    for i in l1:
        for x in l2:
            if i==x:
                sum+=i
    return sum
def circular(l1,l2):
    l3=l1*2
    for x in range(len(l1)): 
        z=0
        for y in range(x, x + len(l1)): 
            if l2[z]==l3[y]: 
                z+=1
            else: 
                break
        if z == len(l1): 
            return True 
    return False
cont='y'
while True:
    option=(int(input('\n\t\t1)Sort and merge\n\t\t2)Sum of common numbers\n\t\t3)Circular Identity\n\n\t\tEnter the option number:')))
    if option==1:
        print(sorting(list(map(int,input('List number 1\nEnter a set of numbers(separated by spaces):').split(sep=' '))),list(map(int,input('List number 2\nEnter a set of numbers(separated by spaces):').split(sep=' ')))))
    elif option==2:
        print(commonsum(list(map(int,input('List number 1\nEnter a set of numbers(separated by spaces):').split(sep=' '))),list(map(int,input('List number 2\nEnter a set of numbers(separated by spaces):').split(sep=' ')))))
    elif option==3:
        print(circular(list(map(int,input('List number 1\nEnter a set of numbers(separated by spaces):').split(sep=' '))),list(map(int,input('List number 2\nEnter a set of numbers(separated by spaces):').split(sep=' ')))))
    if input('Do you want to continue(y/n)?')=='n':
        break
