str1='hello'
str2='hello'
flag=0
if len(str1)==len(str2):
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            flag=1
    if flag!=1:
        print('The strings are equal')
    else:
        print('Strings are not equal')
else:
    print('Strings are not equal')