file_name = input()
with open(file_name) as file, open("forbidden_words.txt") as frbddn_file:
    words = frbddn_file.read().rstrip("\n").split()
    s = file.read()
    s_lower = s.lower()

    for i in words:
        s_lower = s_lower.replace(i, "*" * len(i))
    
    for i in range(len(s_lower)):
        if s_lower[i] == "*":
            print("*", end="")
        else:
            print(s[i], end="")


