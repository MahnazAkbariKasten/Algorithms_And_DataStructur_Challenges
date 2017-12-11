# encoding: UTF-8

from __future__ import absolute_import, division

# from future_builtins import *
# range = xrange

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    buf = None

    identity = lambda x: x

    @classmethod
    def _read_line_raw(cls):
        if cls.buf:
            res = cls.buf
            cls.buf = None
        else:
            res = cls.IN.readline()
        if not res:
            raise EOFError()
        return res

    @classmethod
    def _read_line_view(cls):
        line = cls._read_line_raw()
        if not isinstance(line, memoryview):
            line = memoryview(line)
        return line

    @classmethod
    def _read_line(cls):
        line = cls._read_line_raw()
        if isinstance(line, memoryview):
            line = line.tobytes()
        return line

    @classmethod
    def line(cls, conv=identity):
        line = cls._read_line()
        return conv(line.rstrip(b'\r\n'))

    @classmethod
    def splitline(cls, conv=identity):
        line = cls._read_line()
        return [conv(x) for x in line.split()]

    @classmethod
    def whitespace(cls):
        line = None
        while not line:
            line = cls._read_line_raw()
            i = 0
            l = len(line)
            while i < l and line[i].isspace():
                i += 1
            line = memoryview(line)[i:]
        cls.buf = line

    @classmethod
    def token(cls, conv=identity):
        cls.whitespace()
        line = cls._read_line_view()
        i = 0
        l = len(line)
        while i < l and not line[i].isspace():
            i += 1
        cls.buf = line[i:] if i < l else None
        return conv(line[:i].tobytes())

    @classmethod
    def tokens(cls, cnt, conv=identity):
        return [cls.token(conv) for _ in range(cnt)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return b'Case #{}:'.format(cls.current_case)

def solve():
    # n = gcj.token(int)
    # f = gcj.tokens(n, int)
    n = 11
    f = [2, 1, 4, 5, 4, 7, 1, 9, 10, 11, 1]
    for i in range(n):
        f[i] -= 1
    res = 0
    longest = collections.defaultdict(int)
    for i in range(n):
        done = [False] * n
        l = 0
        j = i
        while not done[j]:
            done[j] = True
            l += 1
            j = f[j]
        if i == j:  # the path is a loop with length of more than 2
            res = max(res, l)
        if f[f[j]] == j:  # the path ends with a loop with length of 2
            k = min(j, f[j])
            k = j
            longest[k] = max(longest[k], l)
        print("i={0}  j={1}  l={2}  res={3}  ".format(i, j, l, res), done, longest.items())
    return max(res, sum(longest.values()) - len(longest))

# def main():
#     sys.setrecursionlimit(10000)
#     t = gcj.token(int)
#     for _ in range(t):
#         print(gcj.case()), solve()
#         sys.stdout.flush()
#
# main()


print(solve())
