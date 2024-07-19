def evaluate(coefficients, x):
    sublist = [i for i in range(len(coefficients) - 1, -1, -1)]
    return list(map(lambda a, deg: a * x ** (deg), coefficients, sublist))

counter = 0
coef = [int(i) for i in input().split()]
num = int(input())

print(sum(evaluate(coef, num)))