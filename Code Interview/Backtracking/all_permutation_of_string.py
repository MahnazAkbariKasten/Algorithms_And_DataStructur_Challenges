__author__ = 'pretty moon'


def all_permutation(arr_of_str, perm):
    # arr_of_str = list(string)
    for i in range(len(arr_of_str)):
        perm += [arr_of_str[i]]

    print(arr_of_str)

def all_permutation_driver(string):
    arr_of_str = list(string)

    all_permutation()

all_permutation("mahnaz")