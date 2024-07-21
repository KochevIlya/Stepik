def pretty_print(data, side="-", delimiter="|"):
    result = ""
    for i in data:
        result += f"{delimiter} {i} "
    result += f"{delimiter}"
    border = " " + side * (len(result) - 2)
    print(border, result, border, sep = "\n")
    
