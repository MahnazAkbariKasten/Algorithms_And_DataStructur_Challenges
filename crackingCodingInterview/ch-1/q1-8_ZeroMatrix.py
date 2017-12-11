__author__ = 'pretty moon'

import unittest

matrix_1 = [[1, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 1, 1, 1]]
zero_matrix_1 = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 1, 1, 0]]

matrix_2 = [[1, 0]]
zero_matrix_2 = [[0, 0]]


class TestZeroMartix(unittest.TestCase):
    def test_matrix_1(self):
        self.assertEqual(zero_matrix(matrix_1), zero_matrix_1)

    def test_matrix_2(self):
        self.assertEqual(zero_matrix(matrix_2), zero_matrix_2)

def zero_matrix(m):
    zero_col_set = set()
    zero_row_set = set()
    num_rows_m = len(m)
    num_cols_m = len(m[0])

    def print_matrix():
        for i in range(num_rows_m):
            print()
            for j in range(num_cols_m):
                print(m[i][j], end='')
                if j != num_cols_m - 1:
                    print(" , ", end='')
        print()

    # print_matrix()

    for i in range(num_rows_m):
        for j in range(num_cols_m):
            if j not in zero_col_set:
                if m[i][j] == 0:
                    zero_row_set.add(i)
                    zero_col_set.add(j)
    for r in zero_row_set:
        m[r] = [0 for x in range(num_cols_m)]
    for c in zero_col_set:
        for i in range(num_rows_m):
            m[i][c] = 0

    # print_matrix()
    return m

if __name__ == "__main__":
    unittest.main()