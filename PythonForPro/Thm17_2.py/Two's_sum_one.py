file = open("numbers.txt")
lst = [int(i) for i in file.readlines()]
print(sum(lst))
file.close()