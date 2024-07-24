def dividers(num):
    lst = []
    for i in range(1, int(num / 2 + 1)):
        if num % i == 0:
            lst.append(i)
    lst.append(num)
    return lst


numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {i: dividers(i) for i in numbers}
print(result)



