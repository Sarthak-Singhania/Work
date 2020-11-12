def binary(n):
    if n>1:
        binary(n//2)
    print(n%2,end='')
def octahedral(n,cnt):
    if n>7 or cnt==0:
        if cnt==0:
            return int((n%8)+octahedral(n//8,cnt+1))
        else:
            return int((n%8)*(10**cnt)+octahedral(n//8,cnt+1))
    elif n<=7 and n>0:
        return n*(10**cnt)
def hexadecimal(n):
    l=[]
    x=n//16
    if x<10:
        l.append(x)
    elif x==10:
        l.append('a')
    elif x==11:
        l.append('b')
    elif x==12:
        l.append('c')
    elif x==13:
        l.append('d')
    elif x==14:
        l.append('e')
    elif x==15:
        l.append('f')
    y=n%16
    if y<10:
        l.append(y)
    elif y>=10:
        z=y
        hexadecimal(z)
    return ''.join(map(str,l))
cont='y'
while cont!='n':
    number=int(input('Enter a number:'))
    option=(input('Desired type:'))
    if option=='B' or option=='b':
        print(binary(number))
    elif option=='O' or option=='o':
        print(octahedral(number,0))
    elif option=='H' or option=='h':
        print(hexadecimal(number))
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'
