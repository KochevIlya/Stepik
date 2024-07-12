def print_products(*args):
    counter = 1
    for i in args:
        if type(i) == str and i != "":
            print(f"{counter}) {i}")
            counter += 1

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


