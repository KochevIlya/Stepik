import random
def generate_ip():
    strg = ""
    for i in range(4):
        strg += str(random.randint(0, 255)) + "."
    strg = strg[:-1]
    return strg