from math import fabs, tan


def f14(n):
    if n < 0:
        return None
    if n == 0:
        return 10
    else:
        return fabs(f14(n - 1)) + tan(f14(n - 1))


print('%.2e' % f14(6))
print('%.2e' % f14(14))
