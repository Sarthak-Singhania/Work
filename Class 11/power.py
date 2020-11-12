a=int(input("Enter a number:"))
b=int(input("Enter the power:"))
cnt=0
power=1
while cnt<b:
    power*=a
    cnt+=1
print("The product is:",power)