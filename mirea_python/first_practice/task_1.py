from math import log, fabs, exp


def f11(x, y):
    try:
        first_argument = (y ** 3 - 93 * y ** 7) / (67 * x ** 4 + exp(x)) \
                               - (y ** 6 - x ** 5) / (y + x ** 3)
        second_argument = fabs(y) + log(x) - 39
        return float(first_argument - second_argument)
    except ValueError or ZeroDivisionError:
        return f'x = {x}, y = {y} is not supported by this function'


print('%.2e' % f11(22, 66))
print('%.2e' % f11(45, -81))
