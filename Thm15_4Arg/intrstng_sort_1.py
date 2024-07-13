
def cmprtr(nmbr):
    sum = 0
    while nmbr > 0:
        sum += nmbr % 10
        nmbr //= 10
    return sum
numbers = [int(i) for i in input().split()]
numbers = sorted(numbers)
print(*sorted(numbers, key=cmprtr))

