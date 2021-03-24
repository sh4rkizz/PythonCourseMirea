# script to find a POSITION OF A NUMBER in a sorted array
# returns -1 if not found
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


# ONLY FOR POSITIVE INTs

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


# If input is int
def digits_counter(number_to_cnt_digs, cnt=0):
    if number_to_cnt_digs == 0:
        return cnt
    else:
        return digits_counter(number_to_cnt_digs // 10, cnt + 1)


# Also use
# return len(str(number_to_cnt_digs))


def time_measure(func):
    def measure(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print("--- %s seconds ---" % (time() - start_time))

        return res

    return measure


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


# Optimized finding of primes
def is_prime(ch):
    if ch % 2 == 0:
        return False
    else:
        sq = int(sqrt(ch))
        for q in range(3, sq, 2):
            if ch % q == 0:
                return False
        return True


def unique(inp):
    t = dict()
    for i, j in inp:
        if i and j:
            t.update({i: j})
    inp = [[i, j] for i, j in t.items()]
    return inp


__import__('*')
