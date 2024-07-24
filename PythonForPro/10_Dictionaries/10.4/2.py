strg1 = input()
strg2 = input()
result = {}
for i in strg1:
    result[i] = result.get(i, 0) + 1

for i in strg2:
    result[i] = result.get(i, 0) - 1
    if result[i] == -1:
        print("NO")
        quit()
for i in result:
    if result[i] != 0:
        print("NO")
        quit()
print()