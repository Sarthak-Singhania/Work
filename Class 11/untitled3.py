'''a=int(input())
l=[0 for x in range(a)]
b=input()
c=list(map(int,b.split()))
if len(c)<a:
    for i in range(len(c)):
        l[i]+=c[i]'''
data_list = [5,-5,6,5,6,4,8]
new_list = []
while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)