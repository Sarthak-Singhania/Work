l=[]
cnt=int(input('Enter how many number you want to input:'))
min=0
mid=0
max=0
for i in range(cnt):
    a=input('Enter a number:')
    l.append(a)
for j in range(len(l)):
    if max<l[j]:
        max=l[j]
for a in range(len(l)):
        if mid<l[a]:
            mid=l[a]
            if mid>=max:
                mid=l[a-1]
for b in range(len(l)):
        if min<l[b]:
            min=l[b]
            if min>=mid:
                min=l[b-1]
print(min,'<',mid,'<',max)