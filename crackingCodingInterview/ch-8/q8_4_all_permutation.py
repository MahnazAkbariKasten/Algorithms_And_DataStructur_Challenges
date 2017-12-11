__author__ = 'pretty moon'

import unittest


class TestAllPermutation(unittest.TestCase):
    def test_0(self):
        self.assertEqual(all_permutation(""), {})

    def test_1(self):
        self.assertEqual(all_permutation("a"), {"a"})

    def test_2(self):
        self.assertEqual(all_permutation("ab"), {"ab", "ba"})

    def test_3(self):
        self.assertEqual(all_permutation("abc"), {"abc", "acb", "bca", "bac", "cab", "cba"})


def all_permutation(myString):
    def find_all_permutation(s):
        if len(s) == 0:
            return {}
        elif len(s) == 1:
            return {s}
        else:
            all_perm = set()
            for i in range(len(s)):
                new_s = s[:i] + s[i+1:]
                all_perm.update({s[i]+x for x in all_permutation(new_s)})
            return all_perm

    return find_all_permutation(myString)
if __name__ == "__main__":
    unittest.main()