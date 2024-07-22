file_name = input()
file = open(file_name)
print(file.readlines()[-2])
file.close()