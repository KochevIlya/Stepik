from functools import reduce
n = int(input())
words = []
for i in range(n):
    words.append(input())
print(*sorted(words, key=lambda x: (reduce(lambda z, y: z + ord(y.upper()) - ord("A"), x, 0), x)), sep = "\n")