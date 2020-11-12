passlist=[]
password=input('Enter your password:')
listpass=list(password)
criteria=[chr(x) for x in range(97,123)]+[chr(i) for i in range(65,91)]+[chr(y) for y in range(48,58)]+['$','#','@']
for x in listpass:
    if x not in criteria:
        pass
    else:
        passlist.append(password)
print(passlist)
