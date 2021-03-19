from math import fabs


def f13(n, m):
    try:
        n = int(n)
        m = int(m)
    except ValueError:
        return None

    first = 0
    second = 0

    for i in range(1, n + 1):
        first += 50 * i ** 2 + 34 * i ** 3 - 80
        second += fabs(i) * 2

    return float(first * m + 94 * second)


print('%.2e' % f13(75, 12))
print('%.2e' % f13(69, 22))
