from operator import *
def arithmetic_operation(symbol):
    dic = {"+": add, "-": sub, "*": mul, "/" : truediv}
    return dic[symbol]