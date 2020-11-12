def pascal(col,row):
    if(col == 0) or (col == row):
        return 1
    else:
        return pascal(col-1,row-1) + pascal(col,row-1)
def PascalTriangle(num):
    for r in range(num):
        for c in range(r+1):
            print(str(pascal(c,r)),end=' ')
        print('\n')
PascalTriangle(10)
