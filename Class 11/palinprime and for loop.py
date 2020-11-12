for i in range(20,201):    
    d=i
    c=0
    while d!=0:
        b=d%10
        c=c*10+b
        d=d//10
    if i==c:
        print(i,"is a palindrome")