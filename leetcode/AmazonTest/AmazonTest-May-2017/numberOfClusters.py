__author__ = 'pretymoon'
import unittest

class TestMethods(unittest.TestCase):
    def test_singleton(self):
        self.assertEqual(numberOfClusters([[0]]), 0)
        # self.assertEqual(numberOfClusters([[1]]), 1)

    def test_one(self):
        self.assertEqual(numberOfClusters([[1, 0], [0, 0]]), 1)
        self.assertEqual(numberOfClusters([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 1)
        self.assertEqual(numberOfClusters([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]]), 1)
        self.assertEqual(numberOfClusters([[0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0],
                                           [0, 0, 1, 1, 0, 0]]), 1)

    def test_multi(self):
        self.assertEqual(numberOfClusters([[1, 0, 1], [0, 0, 0]]), 2)
        self.assertEqual(numberOfClusters([[1, 0, 1], [0, 0, 0], [1, 0, 1]]), 4)
        self.assertEqual(numberOfClusters([[1, 0, 1, 0, 1, 0, 1, 0, 1]]), 5)


def numberOfClusters(matrix):
    count = 0
    global visited
    visited = set([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (i, j) not in visited:
                count += 1
                explore(matrix, i, j)
    return count


def explore(matrix, i, j):
    toBeParsed = [(i, j)]
    while toBeParsed:
        row, col = toBeParsed.pop()
        visited.add((row, col))
        nbs = get_neighbours(matrix, row, col)
        for k, l in nbs:
            if matrix[k][l] == 1 and (k, l) not in visited:
                toBeParsed.append((k, l))


def get_neighbours(matrix, i, j):
    nbs = []
    if i > 0 and j > 0:
        nbs.append((i-1, j-1))
        nbs.append((i-1, j))
        nbs.append((i, j-1))
    else:
        if i > 0:
            nbs.append((i-1, j))
        if j > 0:
            nbs.append((i, j-1))

    if i < len(matrix)-1 and j < len(matrix[0])-1:
        nbs.append((i, j+1))
        nbs.append((i+1, j))
        nbs.append((i+1, j+1))
    else:
        if i < len(matrix)-1:
            nbs.append((i+1, j))
        if j < len(matrix[0])-1:
            nbs.append((i, j+1))

    if i > 0 and j < len(matrix[0])-1:
            nbs.append((i-1, j+1))

    if i < len(matrix)-1 and j > 0:
            nbs.append((i+1, j-1))

    return nbs

# matrix = [[1]]
# print(numberOfClusters(matrix))

if __name__ == '__main__':
    unittest.main()