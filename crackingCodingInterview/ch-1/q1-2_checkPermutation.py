__author__ = 'pretymoon'


def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return "Not Permutation!"

    for i in range(1, len(s2)):
        if s2[i:] + s2[:i] == s1:
            return "Permutation!"
    return "Not Permutation!"

print(checkPermutation("abc", "bac"))
print(checkPermutation("abc", "bca"))