file_name = input()
with open(file_name) as file:
    lst = file.readlines()
    print(len(lst))