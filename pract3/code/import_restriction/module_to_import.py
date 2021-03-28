__all__ = ['gcd', 'lcm', 'counting_sort']

from math import sqrt
from time import time


def binary_search(num_to_find, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if num_to_find == array[mid]:
            return mid
        elif num_to_find < array[mid]:
            high = mid - 1
        else:
            low = mid + 1


def counting_sort(array_to_sort, reverse=False):
    lst = [0] * (max(array_to_sort) + 1)

    for i in array_to_sort:
        lst[i] += 1

    srt = []
    for i in range(len(lst)):
        srt.extend([i] * lst[i])

    if reverse:
        return reversed(srt)
    return srt


def time_measure(func):
    def measure(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print("--- %s seconds ---" % (time() - start_time))

        return res

    return measure


def gcd(a, b):
    """The greatest common divisor possible"""
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


def is_prime(ch):
    if ch % 2 == 0:
        return False
    else:
        sq = int(sqrt(ch))
        for q in range(3, sq, 2):
            if ch % q == 0:
                return False
        return True
