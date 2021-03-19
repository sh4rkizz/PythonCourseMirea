from math import tan, exp


def f12(x=0):
    try:
        if x < 69:
            return 77 * x ** 2 - 75 * x ** 5
        elif 69 <= x < 113:
            return (30 * x ** 6 + 91 * x ** 4) ** 3 - 28 * x ** 5
        elif 113 <= x < 177:
            return tan(67 * x + exp(x)) + x ** 6
        elif 177 <= x < 189:
            return tan(x ** 6 + 39 * x ** 7) + x ** 5 - 64
        else:
            return x ** 4 + 43 * x ** 3
    except ValueError:
        return f'x = {x} is not supported ny this function'


print('%.2e' % f12(29))
print('%.2e' % f12(152))
