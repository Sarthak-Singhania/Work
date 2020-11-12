a=input("Enter a number you want to reverse:")
b=''
for i in range(len(a)-1,-1,-1):
    b+=a[i]
print(b)