def greet(name, *args):
    result = "Hello, " + name
    for i in args:
        result += " and " + i
    result += "!" 
    return result
