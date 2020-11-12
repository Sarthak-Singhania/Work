tvcnt=int(input('Enter the number of TV(s):'))
cnt=1
cart=0
clrtv=0
bwtv=0
while cnt<=tvcnt:
    print('TV',cnt)
    tvclr=int(input('Which type of TV do you want?\n1)Color TV\n2)B/W TV\nEnter your option:'))
    tvsize=int(input('We have the following TV sizes: \n(1) 32"\n \n(2) 40"\n \n(3) 42"\nEnter the size:'))
    if tvclr==1:
        if tvsize==1:
            cart+=5000
            print('The TV has been added to your cart. The MRP is Rs.5000')
            clrtv+=1
        elif tvsize==2:
            cart+=6000
            print('The TV has been added to your cart. The MRP is Rs.6000')
            clrtv+=1
        elif tvsize==3:
            cart+=7000
            print('The TV has been added to your cart. The MRP is Rs.7000')
            clrtv+=1
        else:
            print('Sorry, invalid input')
    elif tvclr==2:
        if tvsize==1:
            cart+=3000
            print('The TV has been added to your cart. The MRP is Rs.3000')
            bwtv+=1
        elif tvsize==2:
            cart+=4000
            print('The TV has been added to your cart. The MRP is Rs.4000')
            bwtv+=1
        elif tvsize==3:
            cart+=5000
            print('The TV has been added to your cart. The MRP is Rs.5000')
            bwtv+=1
        else:
            print('Sorry, invalid input')
    else:
        print('Invalid input')
    cnt+=1
dis=0
if tvcnt>1:
    if clrtv>1 or bwtv>1:
        if cart<=11000 and cart>=7000:
            dis=0.1
        elif cart<=15000 and cart>11000:
            dis=0.2
        elif cart>15000:
            dis=0.3
    else:
        print('No discount')
else:
    print('Buy atleast 2 TV get a discount')
print('You have bought',clrtv,'Colour TV')
print('You have bought',bwtv,'B/W TV')
print('You get a discount of',dis*100,'%')
print('The total bill is of Rs.',cart-(cart*dis))