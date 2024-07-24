def merge(value):
    result = {}
    for i in value:
        for key, val in i.items():
            temp = result.get(key,set())
            temp.add(val)
            result[key] = temp
    return result