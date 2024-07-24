lst = input().split()
result = {}
rlst = []
for i in lst:
    result[i] = result.get(i, 0) + 1
    if result[i] == 1:
        strg = i
    else:
        strg = i + "_" + str(result[i] - 1)
    rlst.append(strg)
print(*rlst)