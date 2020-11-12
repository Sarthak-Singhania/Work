def fact(n):
    if n==1:
        return 1
    else:
        num=n*fact(n-1)
        stack.append(num)
        print(stack)
        return num
num=0
stack=[]
print(fact(10))