sum = 0
with open("nums.txt") as file:
    line = file.readline()
    while line != '':
        line = line.strip()
        line = line.split()
        for i in line:
            number = ""
            for c in i:
                if c.isdigit():
                    number += c
                elif number != "":
                    sum += int(number)
                    number = ""
            if number != "":
                sum += int(number)
                    
        line = file.readline()
print(sum)