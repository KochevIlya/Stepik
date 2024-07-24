def isAnogram(strg1, strg2):
    result = {}
    for i in strg1:
        result[i] = result.get(i, 0) + 1

    for i in strg2:
        result[i] = result.get(i, 0) - 1
        if result[i] == -1:
            return False
    for i in result:
        if result[i] != 0:
            return False
            
    return True


strg1 = [i.strip(".,:;/!?") for i in input().lower().split()]
strg2 = [i.strip(".,:;/!?") for i in input().lower().split()]
result = {}
str1 = ""
for i in strg1:
    str1 += i
str2 = ""
for i in strg2:
    str2 += i

print("YES" if isAnogram(str1, str2) else "NO")