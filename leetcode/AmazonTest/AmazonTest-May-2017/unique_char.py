__author__ = 'pretymoon'
import unittest

class TestMethods(unittest.TestCase):
    def test_emptyString(self):
        self.assertEqual(find_unique(""), -1)

    def test_unique_unique(self):
        self.assertEqual(find_unique("ababc"), "c")

    def test_unique_unique_unique(self):
        self.assertEqual(find_unique("ababc"), "c")

    def test_unique(self):
        self.assertEqual(find_unique("abdabc"), "d")


def find_unique(str_in):
    if str_in == "": return -1
    tmp = {}
    for c in str_in:
        if c in tmp:
            tmp[c] += 1
        else:
            tmp[c] = 1

    for c in str_in:
        if tmp[c] == 1: return c
    return -1

# myStr = "ababc"
# print(find_unique(myStr))

if __name__ == "__main__":
    unittest.main()