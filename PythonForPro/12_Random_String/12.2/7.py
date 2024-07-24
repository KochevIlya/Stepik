from random import randrange as r
import random
def generate_index():
    argsS, argsE = ord("A"), ord("Z") + 1
    result = f'{chr(r(argsS, argsE))}{chr(r(argsS, argsE))}{random.randint(0, 99)}_{random.randint(0, 99)}{chr(r(argsS, argsE))}{chr(r(argsS, argsE))}'
    return result
print(generate_index())