a, b = int(input()), int(input())

result = []
for i in range(a, b+1):
    num = []
    temp = i
    flag = False
    while temp > 0:
        if temp % 10 == 0:
            flag = True
            break
        num.append(temp % 10)
        temp //= 10
    
    result.append(i) if flag == False and all(map(lambda x: i % x == 0, num))  else 0

print(*result, sep=" ")