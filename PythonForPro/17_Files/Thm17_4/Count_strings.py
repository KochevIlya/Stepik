with open("input.txt") as input, open("output.txt", "w") as output:
    line = input.readline()
    counter = 1
    while line != "":
        output.write(f"{str(counter)}) {line}")
        counter += 1 
        line = input.readline()