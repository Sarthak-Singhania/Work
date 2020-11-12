a=d=int(input("Enter a number for which you want to reverse the middle digits:"))
c=0
cnt=0
while a!=0:
    b=a%10
    a/=10
    cnt+=1
if cnt%2==0:
    while a!=0:
        e=d%10
        d/=0