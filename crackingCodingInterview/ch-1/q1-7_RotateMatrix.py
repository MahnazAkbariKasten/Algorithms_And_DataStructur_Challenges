__author__ = 'pretymoon'

import unittest

matrix_1_1 = ["a"]
matrix_1_1_rotated = ["a"]

matrix_2_2 = [["a", "b"],
              ["c", "d"]]
matrix_2_2_rotated = [["c", "a"],
                      ["d", "b"]]

matrix_3_3 = [["a", "b", "c"],
              ["d", "e", "f"],
              ["g", "h", "i"]]
matrix_3_3_rotated = [["g", "d", "a"],
                      ["h", "e", "b"],
                      ["i", "f", "c"]]

matrix_4_4 = [["a", "b", "c", "d"],
              ["e", "f", "g", "h"],
              ["i", "j", "k", "l"],
              ["m", "n", "o", "p"]]
matrix_4_4_rotated = [["m", "i", "e", "a"],
                      ["n", "j", "f", "b"],
                      ["o", "k", "g", "c"],
                      ["p", "l", "h", "d"]]

class TestRotateMatrix(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(rotate_matrix(matrix_1_1), matrix_1_1_rotated)

    def test_2_2(self):
        self.assertEqual(rotate_matrix(matrix_2_2), matrix_2_2_rotated)

    def test_3_3(self):
        self.assertEqual(rotate_matrix(matrix_3_3), matrix_3_3_rotated)

    def test_4_4(self):
        self.assertEqual(rotate_matrix(matrix_4_4), matrix_4_4_rotated)

def rotate_matrix(m):

    len_m = len(m)

    def print_matrix():
        for i in range(len_m):
            print()
            for j in range(len_m):
                print(m[i][j], end='')
                if j != len_m - 1:
                    print(" , ", end='')
        print()

    def fetch_row(r, col_s, col_e):
        if col_s < col_e:
            step = 1
        else:
            step = -1
        buffer = []
        for i in range(col_s, col_e + step, step):
            buffer.append(m[r][i])
        return buffer

    def fetch_col(c, row_s, row_e):
        if row_s < row_e:
            step = 1
        else:
            step = -1
        buffer = []
        for i in range(row_s, row_e + step, step):
            buffer.append(m[i][c])
        return buffer

    if len(m) == 1:
        return m

    # number of layers/shells to peel from matrix
    layer_count = int(len_m / 2)
    for layer in range(layer_count):
        # top-left corner of layer has same row and col
        left = layer
        # right corner of layer has same row and col
        right = len_m - layer - 1
        # buffer the top row
        buffer = fetch_row(left, left + 1, right)
        # replace the top row
        m[left][left+1:right+1] = fetch_col(left, right - 1, left)
        # replace the left col
        tmp_arr = fetch_row(right, left, right-1)
        j = 0
        for i in range(left, right):
            m[i][left] = tmp_arr[j]
            j += 1
        # replace the bottom row
        tmp_arr = fetch_col(right, right, left+1)
        m[right][left:right] = tmp_arr
        # replace the right col
        j = 0
        for i in range(left+1, right+1):
            m[i][right] = buffer[j]
            j += 1

    return m

if __name__ == "__main__":
    unittest.main()