# script to find a POSITION OF A NUMBER in a sorted array
# returns -1 if not found

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