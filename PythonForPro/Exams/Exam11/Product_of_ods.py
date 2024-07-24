from functools import reduce
def product_of_odds(data):   # data - список целых чисел
    return reduce(lambda x, y: (x * y) if y % 2 == 1 else x, data, 1)

