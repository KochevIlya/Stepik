import random
result = set()
while len(result) != 100:
    result.add(random.randint(1000000, 9999999))
print(*result, sep = "\n")

