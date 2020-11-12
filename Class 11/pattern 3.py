k=0
for a in range(1,6,2):
    for b in range(1,5-a+1):
        print(" ",end="")
    while k!=2*a-1:
        if k==0 or k==2*a-2 :
            print('*',end="")
        else :
            print(" ",end="")
        k+=1
    k=0
    print("")
for a in range(4,0,-2):
    for b in range(1,5-a+1):
        print(" ",end="")
    while k!=2*a-1:
        if k==0 or k==2*a-2 :
            print('*',end="")
        else :
            print(" ",end="")
        k+=1
    k=0
    print("")