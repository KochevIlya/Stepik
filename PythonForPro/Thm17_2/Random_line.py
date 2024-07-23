from random import randint
file = open("lines.txt")
lst = file.readlines()
print(lst[randint(1, len(lst))])