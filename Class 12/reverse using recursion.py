def rev(num):
    global reverse
    if num>0:
        reminder=num%10
        reverse=(reverse*10)+reminder
        rev(num//10)
    return reverse
reverse=0
print(rev(17))