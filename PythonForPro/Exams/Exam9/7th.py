m = int(input())
n = int(input())
math = {input() for i in range(m)}
inf = {input() for i in range(n)}

print(len(math - inf))