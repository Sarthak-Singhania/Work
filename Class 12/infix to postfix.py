infix='(a+b)*(c+('
l=[x for x in infix]
precedence={'**':3,'*':2,'/':2,'%':2,'+':1,'-':1}
brackets=['(',')']
operation=[]
postfix=''
for i in l:
    if i in precedence or i in brackets:
        if len(operation)==0:
            operation.append(i)
            print(operation)
        elif i=='(':
            operation.append(i)
            print(operation)
        elif precedence[i]>precedence[operation[-1]] or operation[-1]=='(':
            operation.append(i)
            print(operation)
        elif precedence[i]<=precedence[operation[-1]]:
            postfix+=operation.pop()
            operation.append(i)
            print(operation)
        elif i==')':
            if operation[-1]!='(':
                postfix+=operation.pop()
    else:
        postfix+=i
for _ in range(len(operation)):
    postfix+=operation.pop()
print(postfix)
