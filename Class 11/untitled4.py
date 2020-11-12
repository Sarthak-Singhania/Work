a=input()
c=list(map(int,a.split()))
cnt=0
new_list = []
while c:
    minimum = c[0] 
    for x in c: 
        if x < minimum:
            minimum = x
            cnt+=1
    new_list.append(minimum)
    c.remove(minimum)