def func_apply(function, items):
    for i in range(len(items)):
        items[i] = function(items[i])
    return items