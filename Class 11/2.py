cnt=1
even=0
odd=0
d=0
c=0
print("You need to enter 10 numbers.")
while cnt<=10:
    a=int(input("Enter a number:"))
    cnt+=1
    b=a%2
    if b==0:
        d+=1
        even+=a
    else:
        c+=1
        odd+=a
print("You have entered",d, "even numbers.")
print("You have entered",c, "odd numbers.")
print("Sum of even numbers is: ", even)
print("Sum of odd numbers is:", odd)