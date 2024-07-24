n = int(input())
result = {}
for i in range(n):
    strg = input().split()
    result.setdefault(strg[0], strg[1])
    result.setdefault(strg[1], strg[0])
print(result[input()])


