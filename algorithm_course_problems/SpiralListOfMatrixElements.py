__author__ = 'pretty moon'


import unittest
import math

m_1 = [["a", "b"],
       ["d", "c"]]

l_1 = ["a", "b", "c", "d"]

m_2 = [["a", "b", "c"],
       ["h", "i", "d"],
       ["g", "f", "e"]]

l_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

alphabet16 = [['a', 'b', 'c', 'd'],
              ['l', 'm', 'n', 'e'],
              ['k', 'p', 'o', 'f'],
              ['j', 'i', 'h', 'g'],
             ]

confirm16 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']


class TestSpiralList(unittest.TestCase):
    def test_1(self):
        self.assertEqual(spiralList(m_1), l_1)

    def test_2(self):
        self.assertEqual(spiralList(m_2), l_2)

    def test_16(self):
        self.assertEqual(spiralList(alphabet16), confirm16)


def spiralList(m):
    spiral_list = []
    len_m = len(m)
    num_layers = int(math.ceil(len_m / 2))
    for layer in range(num_layers):
        # Top row
        for cell in m[layer][layer:len_m - layer]:
            spiral_list.append(cell)
        # Right col
        for r in range(layer + 1, len_m - layer - 1):
            spiral_list.append(m[r][len_m - layer - 1])
        # Bottom row
        if layer != len_m - layer - 1:
            for cell in m[len_m - layer - 1][layer:len_m - layer][::-1]:
                spiral_list.append(cell)
        # Left col
        for r in range(len_m - layer - 2, layer, -1):
            spiral_list.append(m[r][layer])
    return spiral_list


if __name__ == "__main__":
    unittest.main()