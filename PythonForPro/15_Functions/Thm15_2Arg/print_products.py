def print_products(*args):
    counter = 1
    for i in args:
        if type(i) == str and i.strip() != "":
            print(f"{counter}) {i}")
            counter += 1
    if counter == 1:
        print("Нет продуктов")

