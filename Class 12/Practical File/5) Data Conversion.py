def binary(n):
    return bin(n)[2:]
def octahedral(n):
    return oct(n)[2:]
def hexadecimal(n):
    return hex(n)[2:]
cont='y'
while cont!='n':
    number=int(input('Enter a number:'))
    option=(input('Desired type:'))
    if option=='B' or option=='b':
        print(binary(number))
    elif option=='O' or option=='o':
        print(octahedral(number))
    elif option=='H' or option=='h':
        print(hexadecimal(number))
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'
