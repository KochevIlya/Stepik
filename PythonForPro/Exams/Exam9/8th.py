m = int(input())
n = int(input())
math = {input() for i in range(m)}
inf = {input() for i in range(n)}

print(m + n - 2 * len(math.intersection(inf))) if m + n - 2 * len(math.intersection(inf)) != 0 else print("NO")