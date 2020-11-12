number=int(input())
sum1=0
a=int(input())
def sum():
    global number
    global sum1
    if number==a:
        return sum1
    else:
        sum1+=number
        number+=1
        return sum()
print(sum())