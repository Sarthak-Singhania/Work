f=open('14) Student.txt','r')

a=f.read()
l=a.split()
cs=0
mm=0
bi=0
for x in l:
    if x=='CSEE':
        cs+=1
    elif x=='Biology':
        bi+=1
    elif x=='MME':
        mm+=1
print('CSEE:',cs,'\nMME:',mm,'\nBiology:',bi)
