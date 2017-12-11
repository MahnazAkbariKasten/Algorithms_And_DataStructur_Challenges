__author__ = 'prettymoon'

import unittest

class TestPalindromePermutation(unittest.TestCase):
    def test_1(self):
        self.assertEqual("mynamecb", False)

    def test_2(self):
        self.assertEqual("amammmeee", True)

    def test_3(self):
        self.assertEqual("", False)

def isPalindromePermutation(s):
    ## make a dictionary of letters in the string with count of letters as the values.
    ## O(n) time & space

    d = dict()

    for letter in s:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    count_odd_occuranc = 0

    ## Maximum one letter can have odd number of occurrence,
    ## ow can't make a palindrome permutation with those letters.
    for cnt in d.values():
        if cnt % 2 != 0:
            count_odd_occuranc += 1

    if count_odd_occuranc > 1:
        return False
    else:
        return True


def isPalindromePermutation2(s):

    ## if the string is an array, we can sort the array and reduce the running time.
    ## O(n) space and O(n log(n)) time

    if len(s) == 0:
        return True

    s = sorted(list(s))

    odd_occur_cnt = 0
    cur_cnt = 1
    cur_letter = s[0]
    for i in range(1, len(s)):
        if s[i] == cur_letter:
            cur_cnt += 1
            i += 1
        else:
            if cur_cnt % 2 != 0:
                odd_occur_cnt += 1
            cur_letter = s[i]
            cur_cnt = 1
            i += 1

    if odd_occur_cnt > 1:
        return False
    else:
        return True



print(isPalindromePermutation("mynamecb"))
print(isPalindromePermutation("amammmeee"))
print(isPalindromePermutation(""))

print(isPalindromePermutation2("mynamecb"))
print(isPalindromePermutation2("amammmeee"))
print(isPalindromePermutation2(""))