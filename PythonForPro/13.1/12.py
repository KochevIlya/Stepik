from decimal import *

num = Decimal(input())
num = str(num)
index = num.find(".")
tens = num[:index]
if tens[0] == "-":
    tens = tens[1:]
ost = num[index + 1:]
tens = list(tens)
ost  = list(ost)
tens.extend(ost)
tens = [int(i) for i in tens]
temp = max(tens) + min(tens)
print(temp)

