__author__ = 'pretymoon'
import unittest


class TestMethods(unittest.TestCase):
    def test_lent(self):
        self.assertFalse(largerThan("1", "12"))
        self.assertTrue(largerThan("12", "9"))

    def test_value(self):
        self.assertFalse(largerThan("12", "13"))
        self.assertFalse(largerThan("12", "12"))
        self.assertTrue(largerThan("12", "11"))
        self.assertTrue(largerThan("22", "11"))

def largerThan(str1, str2):
    if len(str1) > len(str2):
        return True
    elif len(str1) < len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i] > str2[i]:
                return True
            elif str1[i] < str2[i]:
                return False
        return False

# s1 = "123"
# s2 = "123"
#
# print(largerThan(s2,s1))

if __name__ == '__main__':
    unittest.main()