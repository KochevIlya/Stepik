def matrix(n=1, m=None, num=0):
    if m == None:
        m = n
    lst = [[num for i in range(m)] for j in range(n)]
    return lst

matr = matrix(3, 4, 5)
for i in range(3):
    print(*matr[i])