n = int(input())
result = {}
for i in range(n):
    strg = input().split(": ")
    result.setdefault(strg[0].lower(), strg[1])

m = int(input())
for i in range(m):
    print(result.get(input().lower(), "Не найдено"))