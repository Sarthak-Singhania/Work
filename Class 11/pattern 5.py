s=7
'''for a in range(s,0,-1):
    d=ord('A')
    for b in range(1,s+1):
        if b>=a:
            print (b,end='')
            d+=1
        else:
            print ('',end='')
    print()'''
for a in range(s,0,-1):
    for b in range(1,s+1):
        if b>=a:
            print (b,end='')
        else:
            print (' ',end='')
    for b in range(s-1,0,-1):
         if b>=a:
            print (b,end='')
    print()
