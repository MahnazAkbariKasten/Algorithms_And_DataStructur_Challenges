__author__ = 'pretymoon'

import math

def largest_palindrom(n):
    if n < 1 or n > 8:
        return -1

    smallest_number = 10 ** (n - 1)

    largest_number = 0
    for i in range(n):
        largest_number += 9 * 10 ** i

    bottom = largest_number + 1
    for i in range(largest_number, smallest_number - 1, -1):
        # print(i)
        k = i
        for j in range(i, bottom):
            if is_palindrom(j * k):
                return (j * k) % 1337
            k -= 1

        if i <= math.ceil((largest_number) / 2):
            bottom = bottom - 1

        k = i - 1
        for j in range(i, bottom):
            if is_palindrom(j * k):
                return (j * k) % 1337
            k -= 1

        if i <= math.ceil((largest_number) / 2):
            bottom = bottom - 1

    return -1


def is_palindrom(number):
    string_ver = str(number)
    l = len(string_ver)

    for i in range(l // 2):
        if string_ver[i] != string_ver[l - i - 1]:
            return False

    return True

print(largest_palindrom(1))
# print(is_palindrom(9))