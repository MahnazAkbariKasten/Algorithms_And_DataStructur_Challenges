__author__ = 'pretty moon'

import unittest

class TestDeepSet(unittest.TestCase):
    def test_deep_test(self):
        self.assertEqual(ListPermutation.areListPermutations([[1, 1, 1], [2, 1], [1, 2], [3]], [[1, 1, 1], [1, 2], [2, 1], [3]]), True)


class ListPermutation:

    def areListPermutations(m1, m2):
        def deep_set(m):
            m_set = set(tuple(x) for x in m)

        return deep_set(m1) == deep_set(m2)


if __name__ == "__main__":
    unittest.main()