d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
strg = input()
counter = 0
for i in strg:
    for j, k in d.items():
        if i in k:
            counter += j
print(counter) 