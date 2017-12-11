__author__ = 'pretty moon'

import unittest

class TestStringCompression(unittest.TestCase):
    def test_null(self):
        self.assertEqual(compress_string(""), "")

    def test_short(self):
        self.assertEqual(compress_string("xyz"), "xyz")

    def test_equal(self):
        self.assertEqual(compress_string("ooxx"), "ooxx")

    def test_long(self):
        self.assertEqual(compress_string("ooojjjjjjjjjjj"), "o3j11")

def compress_string(s):
    len_s = len(s)

    # check for null string, at this point this checking is not neccesary, because the main
    # for-loop will take care of null string.
    if len_s == 0:
        return s

    new_s_list = []

    i = 0
    while i < len_s:
        cnt = 0
        curr_letter = s[i]
        while i < len_s and s[i] == curr_letter:
            cnt += 1
            i += 1

        new_s_list.append(curr_letter + str(cnt))

    new_s = ''.join(new_s_list)

    if len(new_s) >= len_s:
        return s
    else:
        return new_s

if __name__ == "__main__":
    unittest.main()