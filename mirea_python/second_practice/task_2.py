def f22(code):
    h = (code & (2 ** 32 - 1) & ~(2 ** 29 - 1)) >> 10
    g = (code & (2 ** 29 - 1) & ~(2 ** 25 - 1)) >> 3
    f = (code & (2 ** 25 - 1) & ~(2 ** 24 - 1)) >> 8
    e = (code & (2 ** 24 - 1) & ~(2 ** 21 - 1)) >> 8
    d = (code & (2 ** 21 - 1) & ~(2 ** 19 - 1)) >> 2
    c = (code & (2 ** 19 - 1) & ~(2 ** 11 - 1)) >> 6
    b = (code & (2 ** 11 - 1) & ~(2 ** 5 - 1)) << 21
    a = code & (2 ** 5 - 1)
    return a | b | c | d | e | f | g | h
