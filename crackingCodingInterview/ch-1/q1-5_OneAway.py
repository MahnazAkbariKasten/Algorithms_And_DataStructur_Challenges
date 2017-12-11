__author__ = 'pretymoon'

import unittest

class testOneAway(unittest.TestCase):
    def testSameSize(self):
        self.assertEqual(isOneAway("pae", "pale"), True)

def isOneAway(s1, s2):

    def isSubStr(str1, subStr1):
        for i in range(len(str1)):
            if str1[:i]+str1[i+1:] == subStr1:
                return True
        return False

    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 == len_s2:
        cnt = 0
        for i in range(len_s1):
            if s1[i] != s2[i]:
                cnt += 1
        if cnt > 1:
            return False
        return True
    elif len_s1 < len_s2:
        return isSubStr(s2, s1)
    else:
        return isSubStr(s1, s2)


if __name__ == "__main__":
    unittest.main()


# print(isOneAway("pae", "pale"))
# print(isOneAway("ple", "pale"))
# print(isOneAway("pmle", "pale"))