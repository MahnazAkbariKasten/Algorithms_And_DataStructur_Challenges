__author__ = 'pretymoon'
import unittest


class TestMethods(unittest.TestCase):
    def test_func(self):
        self.assertEqual(sum_diag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 15)
        self.assertEqual(sum_diag([[0, 0], [1, 0]]), 0)

    def tes_error(self):
        self.assertRaises(sum_diag([1]), TypeError)


def sum_diag(arr_2d):
    sumd = 0
    for i in range(len(arr_2d)):
        sumd += arr_2d[i][i]
    return sumd

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(sum_diag(a))

if __name__ == '__main__':
    unittest.main()