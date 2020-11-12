def stack(s):
    if s!=[]:
        res=s.pop()
        stk2.append(res)
        stack(s)
stk=[1,2,3,4,5]
stk2=[]
stack(stk)
print(stk2)