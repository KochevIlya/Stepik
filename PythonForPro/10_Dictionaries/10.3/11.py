dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
for i in dict1:
    result.setdefault(i, dict1[i])
for i in dict2:
    if i in result:
        result[i] += dict2[i]
    else:
        result.setdefault(i, dict2[i])
    



