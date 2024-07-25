from functools import reduce
with open("ledger.txt") as file:
    lst = []
    for i in file:
        lst.append(i.rstrip("\n").strip("$"))
    print(f"${reduce(lambda x, y: x + int(y), lst, 0)}")
