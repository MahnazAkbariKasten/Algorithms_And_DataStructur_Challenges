__author__ = 'pretymoon'
import unittest

class TestMethods(unittest.TestCase):
    def test_car(self):
        self.assertEqual(car([0, 1, 2, 3, 4], [1, 2, 3], 2), [3, 4, 0])
        self.assertEqual(car([], [], 2), [])
        self.assertEqual(car([1], [], 2), [1])
        self.assertEqual(car([1, 2], [1], 0), [2])
        self.assertEqual(car([1, 2], [1], 1), [1])
        self.assertEqual(car([1, 2], [1], 2), [2])

def car(o_arr, q_arr, k):
    if len(o_arr) <= 1:
        return o_arr
    else:
        res = []
        for q in q_arr:
            new_idx = (k + q + 1) % (len(o_arr))
            res.append(o_arr[new_idx - 1])
        return res

# print(car([0,1,2,3,4], [1,2,3], 2))
if __name__ == '__main__':
    unittest.main()