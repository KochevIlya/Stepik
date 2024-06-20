list1 = set(int(i) for i in input().split())
list2 = set(int(i) for i in input().split())
result = list1.intersection(list2)

print(*sorted(result, reverse=True)) if len(result) > 0 else print("BAD DAY")

