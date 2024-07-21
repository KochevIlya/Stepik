def concat(*args, sep=" "):
    result = ""
    for i in args:
        result += str(i) + sep
    result = result[:-len(sep)]
    return result
