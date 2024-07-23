def read_csv():
    with open("data.csv") as file:
        keys = file.readline().rstrip("\n").split(",")
        result = []
        line = file.readline()
        while line != "":
            values = line.rstrip("\n").split(",")
            result.append(dict(zip(keys, values)))
            line = file.readline()
        return result
