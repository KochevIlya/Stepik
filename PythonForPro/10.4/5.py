n = int(input())
result = {}
for i in range(n):
    strg = input().split()
    for j in range(1, len(strg)):
        result[strg[j]] = strg[0]
m = int(input())
for i in range(m):
    print(result[input()])
