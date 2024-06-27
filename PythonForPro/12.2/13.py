from random import randrange as r
import random
def generate_password(length):
    lst = []
    for i in range(length):
        lst.append(
            (
                r(97, 108),  # нижние буквы
                r(109, 111),
                r(112, 123),
                r(65, 73),  # верхние буквы
                r(74, 79),
                r(80, 91),
                r(50, 58),  # Число
            )[random.randint(0, 6)]
        )
    return lst


def generate_passwords(count, length):
    lst = []
    for i in range(count):
        generated = []
        alpha = False
        digit = False
        bigAlpha = False
        while alpha != True or digit != True or bigAlpha != True:
            generated = generate_password(length)
            alpha = False
            digit = False
            bigAlpha = False
            for i in generated:
                if 97 <= i <= 122:
                    alpha = True
                elif 65 <= i <= 90:
                    bigAlpha = True
                elif 50 <= i <= 58:
                    digit = True

        result = ""
        for i in generated:
            result += chr(i)
        lst.append(result)
    return lst


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep="\n")
