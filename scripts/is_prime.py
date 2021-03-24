from math import sqrt


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
