from fractions import Fraction as F

str1 = input()
str2 = input()

fr1 = F(str1)
fr2 = F(str2)

print(str1, "+", str2, "=", fr1 + fr2)
print(str1, "-", str2, "=", fr1 - fr2)
print(str1, "*", str2, "=", fr1 * fr2)
print(str1, "/", str2, "=", fr1 / fr2)
