n = int(input())
m = int(input())
resultSet = {input() for _ in range(m)}

for _ in range(1, n):
    m = int(input())
    tempSet = {input() for _ in range(m)}
    resultSet -= resultSet - tempSet
print(*sorted(resultSet), sep = "\n")