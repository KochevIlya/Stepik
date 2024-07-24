    

def compose(f, g):
    def arg(x):
        return f(g(x))
    return arg