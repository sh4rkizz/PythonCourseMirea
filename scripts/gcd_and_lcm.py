def gcd(a, b):
    """Finds the greatest common divisor possible"""
    if a < b:
        a, b = b, a
    while b:
        a %= b
        a, b = b, a

    return a


def lcm(a, b):
    """Finds the lowest common multiple"""
    if a < b:
        a, b = b, a

    return int(a / gcd(a, b) * b)
