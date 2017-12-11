__author__ = 'pretty moon'

import unittest

class TestparanthesisPairs(unittest.TestCase):
    def test_0(self):
        self.assertEqual(all_valid_pairs(0), {})

    def test_1(self):
        self.assertEqual(all_valid_pairs(1), {"()"})

    def test_2(self):
        self.assertEqual(all_valid_pairs(2), {"(())", "()()"})

    def test_3(self):
        self.assertEqual(all_valid_pairs(3), {"((()))", "()()()", "()(())", "(())()", "(()())"})


def all_valid_pairs(n):
    if n == 0:
        return {}
    elif n == 1:
        return {"()"}
    else:
        all_pairs = set()
        tmp = all_valid_pairs(n - 1)
        for m in tmp:
            for i in range(len(m)):
                all_pairs.add(m[:i] + "()" + m[i:])
        return all_pairs

if __name__ == "__main__":
    unittest.main()