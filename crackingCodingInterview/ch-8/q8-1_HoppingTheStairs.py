__author__ = 'pretty moon'

import unittest


def areListPermutations(m1, m2):
    def deep_set(m):
        m_set = set(tuple(x) for x in m)

    return deep_set(m1) == deep_set(m2)


class TestHoppingTheStairs(unittest.TestCase):
    def test_cnt_0(self):
        self.assertEqual(number_of_ways(0, [1, 2, 3]), 1)

    def test_cnt_1(self):
        self.assertEqual(number_of_ways(1, [1, 2, 3]), 1)

    def test_cnt_2(self):
        self.assertEqual(number_of_ways(2, [1, 2, 3]), 2)

    def test_cnt_3(self):
        self.assertEqual(number_of_ways(3, [1, 2, 3]), 4)

    def test_cnt_4(self):
        self.assertEqual(number_of_ways(4, [1, 2, 3]), 7)

    def test_cnt_5(self):
        self.assertEqual(number_of_ways(5, [1, 2, 3]), 13)

    def test_cnt_3_4(self):
        self.assertEqual(number_of_ways(3, [1, 2, 3, 4]), 4)

    def test_cnt_4_4(self):
        self.assertEqual(number_of_ways(4, [1, 2, 3, 4]), 8)

    def test_path_0(self):
        self.assertEqual(list_of_ways(0, [1, 2, 3]), [[]])

    def test_path_1(self):
        self.assertEqual(list_of_ways(1, [1, 2, 3]), [[1]])

    def test_path_2(self):
        self.assertEqual(list_of_ways(2, [1, 2, 3]), [[1, 1], [2]])

    def test_path_3(self):
        self.assertEqual(list_of_ways(3, [1, 2, 3]), [[1, 1, 1], [2, 1], [1, 2], [3]])

    def test_path_3_4(self):
        self.assertEqual(list_of_ways(3, [1, 2, 3, 4]), [[1, 1, 1], [2, 1], [1, 2], [3]])

    def test_path_4_4(self):
        output = list_of_ways(4, [1, 2, 3, 4])
        expected = [[1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 3], [1, 1, 2], [2, 2], [3, 1], [4]]
        self.assertEqual(areListPermutations(output, expected), True)


def number_of_ways(N, I):
    n_table = [1]
    if N > 0:
        for n in range(1, N+1):
            cnt = 0
            for i in I:
                if i <= n:
                    cnt += n_table[n - i]
            n_table.append(cnt)

    return n_table[N]

def list_of_ways(N, I):
    n_list = [[[]]]
    if N > 0:
        for n in range(1, N+1):
            n_list.append([])
            for i in I:
                if i <= n:
                    for path in n_list[n - i]:
                        n_list[n].append(path + [i])
    return n_list[N]


if __name__ == "__main__":
    unittest.main()