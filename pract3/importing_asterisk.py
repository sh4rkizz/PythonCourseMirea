from module_to_import import *

try:
    print(binary_serach(2512, [1, 2, 3, 4, 5, 6, 7, 2511, 2512]))
except NameError:
    print('This function was not imported by asterisk\n')
    try:
        print(f'{gcd.__doc__} for a = 25215, b = 15657 is {gcd(25215, 15657)}')
        print(f'Sorted array: {counting_sort(range(15, 1, -1))}')
    except NameError:
        'We won`t get here'
