dct = {}
strg = input().split()
for i in strg:
    dct[i] = dct.get(i, 0) + 1
    print(dct[i], end=" ")

