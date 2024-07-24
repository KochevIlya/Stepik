from functools import reduce
def decimal(string):
    lst = string.split(".")
    powers = [3, 2, 1, 0]
    sum = 0
    for i, j in zip(lst, powers):
        sum += int(i) * 256 ** j
    return sum

n = int(input())
lst = [input() for i in range(n)]
print(*sorted(lst, key=lambda x: decimal(x)), sep="\n")  