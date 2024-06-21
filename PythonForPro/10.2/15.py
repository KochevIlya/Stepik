d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

str = input().upper()
for c in str:
    for i in d: 
        counter = 1
        for s in d[i]:
            if c == s:
                print(i * counter, end = "")
                break 
            counter += 1
