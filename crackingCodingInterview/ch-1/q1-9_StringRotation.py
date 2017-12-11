__author__ = 'pretty moon'

import unittest

s1_a = "waterbottle"
s2_a = "aterbottlew"

s1_b = "abca"
s2_b = "aabc"


class TestStringRotation(unittest.TestCase):
    def test_a(self):
        self.assertTrue(isStringRotation(s1_a, s2_a))

    def test_b(self):
        self.assertTrue(isStringRotation(s1_b, s2_b))


def isStringRotation(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 != len_s2:
        return False

    s = s1 * 2

    if s.find(s2) >= 0:
        return True
    else:
        return False

if __name__ == "__main__":
    unittest.main()