__author__ = 'pretymoon'
import unittest


class TestMethod(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(mySum(), ())

    def test_int(self):
        self.assertEqual(mySum(1, 2, 3), 6)
        self.assertEqual(mySum(0), 0)
        self.assertEqual(mySum(0, 100), 100)

    def test_str(self):
        self.assertEqual(mySum("ab", "cd", "ef"), "abcdef")
        self.assertEqual(mySum(""), "")

    def test_list(self):
        self.assertEqual(mySum([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(mySum([]), [])

    def test_set(self):
        self.assertEqual(mySum({1, 3, 2}, {2, 3, 4}), {1, 2, 3, 4})


def getUnit(myArg):
    if isinstance(myArg, int):
        return 0
    elif isinstance(myArg, float):
        return 0.0
    elif isinstance(myArg, list):
        return []
    elif isinstance(myArg, set):
        return set([])
    elif isinstance(myArg, dict):
        return {}
    elif isinstance(myArg, float):
        return 0.0
    elif isinstance(myArg, str):
        return ""
    elif isinstance(myArg, tuple):
        return ()


def mySum(*myArg):
    if not myArg:
        # print(myArg)
        return myArg    # getUnit(myArg)
    elif getUnit(myArg[0]) is not None:
        res = getUnit(myArg[0])
        for a in myArg:
            res = res + a  # += a
        return res


if __name__ == "__main__":
    unittest.main()