def countSquares(n):
    return (((n+1) * (n + 2) / 2) * (2 * (n+1) + 1) / 3)
n = 8
print("Count of squares is ",countSquares(n))