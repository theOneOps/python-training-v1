def add(*args):
    n = 0
    for i in args:
        n += i
    return n


print(add(range(6)))
