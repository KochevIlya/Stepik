import random

length = int(input())    
password = ""
for i in range(length):
    isLower = True if random.randint(0, 1) == 1 else False
    password += chr(random.randint(97, 122)) if isLower else chr(random.randint(65, 90))
print(password)


