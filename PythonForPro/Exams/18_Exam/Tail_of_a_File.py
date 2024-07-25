file_name = input()
with open(file_name) as file:
    lines = []
    for line in file:
        lines.append(line.rstrip("\n"))
    for i in lines[-10:]:
        print(i)