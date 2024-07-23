import random
names = []
surnames = []
with open("first_names.txt") as names_file, open("last_names.txt") as surnames_file:
    names = names_file.readlines()
    surnames = surnames_file.readlines()
surnames = [i.strip() for i in surnames]
names = [i.strip() for i in names]
for i in range(3):
    print(names[random.randint(0, len(names))], surnames[random.randint(0, len(surnames))])