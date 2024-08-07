import math
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def function(item):
    item *= 1000
    if item % 10 >= 5:
        item += 10
    item = int(item)
    item = item // 10
    item = item / 100
    return item

def another(item):
    return round(item, 2)



numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
print(*map(function, numbers))
print(*map(another, numbers))