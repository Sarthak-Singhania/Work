print("Enter 3 numbers.")
a=int(input("1st number:"))
b=int(input("2nd number:"))
c=int(input("3rd number:"))
if a<b and a<c:
    if b<c:
        min,mid,max=a,b,c
    else:
        min,mid,max=a,c,b
elif b<a and b<c:
    if a<c:
        min,mid,max=b,a,c
    else:
        min,mid,max=b,c,a
else:
    if a<b:
        min,mid,max=c,a,b
    else:
        min.mid,max=c,b,a
print(min,"<",mid,"<",max)