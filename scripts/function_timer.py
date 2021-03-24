from time import time


def time_measure(func):
    def measure(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print("--- %s seconds ---" % (time() - start_time))

        return res

    return measure
