choice = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
strg = input()
lst = [choice[i] for i in strg]
print(*lst, sep = "")