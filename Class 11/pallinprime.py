a=input()
b=list(map(int,a.split()))
c=b[0]
d=b[1]
for j in range(c,d):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j)