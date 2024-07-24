from functools import reduce
with open("file.txt") as file:
    lst = file.readlines()
    lst = [i.strip("\n.") for i in lst]
    words = []
    for i in lst:
        words += i.split()
    letters = 0
    for i in words:
        for c in i:
            if c.isalpha():
                letters += 1
    print(f'''Input file contains:
{letters} letters
{len(words)} words
{len(lst)} lines''')
