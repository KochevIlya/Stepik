from math import sin

d = {'квадрат': lambda x: x ** 2,
     'куб': lambda x: x ** 3,
     'корень': lambda x: x ** 0.5,
     'модуль': lambda x: abs(x),
     'синус': lambda x: sin(x)}

a = int(input())
print(d[input()](a))


