import math

n = int(input())
if n % 2 != 0:
    chisl = int(n / 2)
    znam = int(n / 2) + 1
else:
    chisl = int(n / 2) - 1
    znam = int(n / 2) + 1
while math.gcd(chisl, znam) != 1:
    znam += 1
    chisl -= 1
print(str(chisl) + "/" + str(znam))
