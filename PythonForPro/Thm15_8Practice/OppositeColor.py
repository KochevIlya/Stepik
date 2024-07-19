rgb = [int(i) for i in input().split()]
print(*list(map(lambda x: 255 - x, rgb)), sep = " ")