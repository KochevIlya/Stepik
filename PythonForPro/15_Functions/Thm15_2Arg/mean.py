def mean(*args):

    a = [i for i in args if type(i) in {float, int}]
    return 0 if len(a) == 0 else sum(a) / len(a)

