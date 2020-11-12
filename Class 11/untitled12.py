l=['hello','lol','rofl','sms','moody']
d={}
for i in l:
    num=0
    for j in l:
        if len(i)==len(j):
            num+=1
    d[len(i)]=num
print(d)