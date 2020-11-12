a=input("Enter elements separated by space: ").split()
b=input("Enter elements separated by space: ").split()

#Merge List
L=a+b
print(L)

sum=0
for x in a:
    if x in b:
       sum+=int(x)
    else:
        pass
print (sum)

c=a*2
for x in range(len(a)):
    z=0
    for y in range(x, x + len(a)):
        if b[z]==c[y]:
            z+=1
        else:
            break
    if z == len(a):
        print ('Yes')
        break
else:
    print ('No')
