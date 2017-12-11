__author__ = 'pretymoon'
import unittest


class TestMethods(unittest.TestCase):
    def test_singleton(self):
        self.assertTrue(safe_rooks([[1]]))

    def test_larger(self):
        self.assertTrue(safe_rooks([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
        self.assertFalse(safe_rooks([[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]))
        self.assertFalse(safe_rooks([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))


def safe_rooks(arr_2d):
    for i in range(len(arr_2d[0])):
        for j in range(1, len(arr_2d)):
            if arr_2d[0][i] == arr_2d[j][i] == 1:
                return False
            if arr_2d[i][0] == arr_2d[i][j] == 1:
                return False
    return True

# a = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
# b = [[1]]
# print(safe_rooks(a), safe_rooks(b))

if __name__ == '__main__':
    unittest.main()