chipher = input()
dict_chipher = {}
for i in chipher:
    dict_chipher[i] = dict_chipher.get(i, 0) + 1
info = {}
n = int(input())
for i in range(n):
    key, value = input().split(": ")
    info.setdefault(int(value), key)
result = {}
for k, v in dict_chipher.items():
    result[k] = info.get(v)
res_str = ""
for i in chipher:
    res_str += result[i]
print(res_str)

