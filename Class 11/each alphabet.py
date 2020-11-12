a=input('Enter a sentence:')
l=[0 for x in range(26)]
b=ord('a')
for i in range(len(a)):
    if a[i]!=' ':
        l[ord(a[i])-ord('a')]+=1
for j in range(26):
    if l[j]!=0:
        print(chr(b),'-',l[j])
    b+=1