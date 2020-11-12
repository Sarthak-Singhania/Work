decimal = int(input("Enter a decimal integer greater than 0: "))

print("Quotient Remainder Octal") 
bstring = " "
while decimal > 0:
    remainder = decimal % 8 
    decimal = decimal // 8 
    bstring = str(remainder) + bstring
print(bstring)
n=1000
a=''
while n>0:
    remainder=n%8 
    n//=8 
    a=str(remainder)+a
print(a)
