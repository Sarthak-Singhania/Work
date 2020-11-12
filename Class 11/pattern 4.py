k = 0
for i in range(1,6,2):
    for j in range(1,5-i+1):
        print(" ",end="")
    while (k != (2 * i)):
        if (k == 0 or k == 2 * i - 2) :
            print(1,end="")
        else :
            print(" ",end="")
        k+=1
    k = 0
    print("")
for i in range(6,1,-2):
    for j in range(1,5-i+1):
        print(" ",end="")
    while (k != (2 * i)):
        if (k == 0 or k == 2 * i - 2) :
            print(1,end="")
        else :
            print(" ",end="")
        k+=1
    k = 0
    print("")