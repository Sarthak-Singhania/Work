def sequence(length):
    if length<=1:
        return length
    else:
        res=(sequence(length-1)+sequence(length-2))
        return res
length=int(input())
for i in range(length):
    print(sequence(i))