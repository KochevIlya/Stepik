def matrix(n=1, m=None, num=0):
    if m == None:
        m = n
    lst = [[num for i in range(m)] for j in range(n)]
    return lst
