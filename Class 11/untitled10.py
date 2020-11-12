a='rotor'
flag=0
for i in range(len(a)):
    j=len(a)-1-i
    if a[i]!=a[j]:
        flag=1
if flag!=1:
    print('Palindrome')
else:
    print('Not a palindrome')