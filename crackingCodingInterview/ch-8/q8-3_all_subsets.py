__author__ = 'pretty moon'

import unittest

class TestAllSubsets(unittest.TestCase):
    def test_0(self):
        self.assertEqual(all_subsets(set()), {frozenset()})

    def test_1(self):
        self.assertEqual(all_subsets({1}), {frozenset(), frozenset([1])})

    def test_2(self):
        self.assertEqual(all_subsets({1, 2}), {frozenset({}), frozenset({2}), frozenset({1}), frozenset({1, 2})})

    def test_3(self):
        self.assertEqual(all_subsets({1, 2, 3}), {frozenset({}), frozenset({1}), frozenset({2}), frozenset({1, 2}),
                                                 frozenset({3}), frozenset({1, 3}), frozenset({3, 2}), frozenset({1, 2, 3})})

    def test_4(self):
        self.assertEqual(all_subsets({1, 2, 3, 4}), {frozenset({}), frozenset({1}), frozenset({2}), frozenset({1, 2}),
                                                 frozenset({3}), frozenset({1, 3}), frozenset({3, 2}), frozenset({1, 2, 3}),
                                   frozenset({4}), frozenset({1, 4}), frozenset({2, 4}), frozenset({1, 2, 4}),
                                                frozenset({3, 4}), frozenset({1, 3, 4}), frozenset({3, 2, 4}), frozenset({1, 2, 3, 4})})


def all_subsets(my_set):
    def find_all_subsets(s):
        if s == set():
            return {frozenset([])}
        new_set = s
        arb_element = s.pop()
        subsets = find_all_subsets(new_set)
        return subsets.union({x.union(set([arb_element])) for x in subsets} )                  # [x.append(arb_element) for x in subsets]

    return find_all_subsets(my_set)


if __name__ == "__main__":
    unittest.main()