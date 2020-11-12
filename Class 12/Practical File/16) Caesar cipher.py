key={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',   'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ':' '}
def change():
    l1=list(key.keys())
    l2=list(key.values())
    d={}
    for x in range(len(l1)):
        d[l2[x]]=l1[x]
    return d
key1=change()
def cipher(a):
    b=list(a)
    d={}
    for x in range(len(b)):
        d[b[x]]=key[b[x]]
    return d
def decipher(a):
    b=list(a)
    d={}
    for x in range(len(b)):
        d[b[x]]=key1[b[x]]
    return d
cont='y'
while cont!='n':
    option=(int(input('\n\t\t1)Cipher\n\t\t2)Decipher\n\n\t\tEnter the option number:')))
    if option==1:
        a=input('Enter the file name with extenstion:')
        f=open(a,'r')
        b=f.read()
        f1=open('ciphered.txt','a')
        c=list(cipher(b).values())
        f1.write(str(''.join(c)))
    elif option==2:
        a=input('Enter the file name with extenstion:')
        f=open(a,'r')
        b=f.read()
        f1=open('deciphered.txt','a')
        c=list(decipher(b).values())
        f1.write(str(''.join(c)))
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'
f1.close()
