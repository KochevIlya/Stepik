file = open("prices.txt")
lst = [i[:-1] for i in file]
cost = 0
for i in lst:
    str = i.split("\t")
    cost += int(str[1]) * int(str[2])
    
print(cost)
file.close()