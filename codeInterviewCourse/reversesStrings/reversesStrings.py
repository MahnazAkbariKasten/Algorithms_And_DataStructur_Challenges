__author__ = 'pretymoon'
import unittest

class TestMethods(unittest.TestCase):
    def test_lent(self):
        self.assertFalse(checkReverses("", "CBA"))
        self.assertFalse(checkReverses("AAAA", "CBA"))

    def test_reverse(self):
        self.assertTrue(checkReverses("ABC", "CBA"))
        self.assertFalse(checkReverses("AAA", "CBA"))

def checkReverses(str1, str2):
    if len(str1) != len(str2):
        return False
    if len(str1) == 0 or len(str2) == 0:
        return False
    lent = len(str1)
    for i in range(len(str1)):
        if str1[i] != str2[lent - i -1]:
            return False
    return True


# s1 = "AABC"
# s2 = "CBAA"
#
#
# print(checkReverses(s1, s2))
# print(s1 , ''.join(list(reversed(s2))))

# print(s1 == ''.join(list(reversed(s2))))
# s3 = ''.join(list(reversed(s2)))
# print("is the same? ", s1 is ''.join(list(reversed(s2))))

if __name__ == '__main__':
    unittest.main()




