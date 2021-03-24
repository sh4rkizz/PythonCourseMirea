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
