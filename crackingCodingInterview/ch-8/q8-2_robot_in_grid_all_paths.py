__author__ = 'pretty moon'

# find all the paths to the destination

import unittest

grid_1 = [[1, 1, 1],
          [0, 1, 1],
          [0, 0, 1]]
path_list_1 = {tuple([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]), tuple([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])}

grid_2 = [[1, 0, 0],
          [1, 1, 1],
          [1, 0, 1]]
path_list_2 = {tuple([(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)])}

grid_3 = [[1, 1, 1],
          [1, 0, 1],
          [1, 0, 1]]
path_list_3 = {tuple([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])}

grid_4 = [[1, 1, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 0, 1]]
path_list_4 = {tuple([(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)])}

grid_5 = [[1, 1, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 1]]
path_list_5 = {tuple([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]),
               tuple([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)]),
               tuple([(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3)]),
               tuple([(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)])}


class TestRobot(unittest.TestCase):
    def test_grid_1(self):
        self.assertEqual(set(robot_path(grid_1)), path_list_1)

    def test_grid_2(self):
        self.assertEqual(set(robot_path(grid_2)), path_list_2)

    def test_grid_3(self):
        self.assertEqual(set(robot_path(grid_3)), path_list_3)

    def test_grid_4(self):
        self.assertEqual(set(robot_path(grid_4)), path_list_4)

    def test_grid_5(self):
        self.assertEqual(set(robot_path(grid_5)), path_list_5)


def robot_path(m):

    back_track = dict()  # back_track[curr_cell] = [prev_cell_set, next_cell_list]
    num_row = len(m)
    num_col = len(m[0])
    start_cell = tuple((0, 0))
    dest_cell = tuple((num_row - 1, num_col - 1))

    def find_next(cell):
        # Can go right?
        if cell[1] < num_col - 1 and m[cell[0]][cell[1] + 1]:
            back_track[cell][1].append((cell[0], cell[1] + 1))

        # Can go down?
        if cell[0] < num_row - 1 and m[cell[0] + 1][cell[1]]:
            back_track[cell][1].append((cell[0] + 1, cell[1]))

    # Form all paths
    path_list = []

    #   recursive exploration of paths   #
    def form_paths(cell, p):
        if cell == start_cell:
            path_list.append(tuple(p))
            return
        ancestors = back_track[cell][0][:]
        while ancestors:
            path = p[:]
            next_cell = ancestors.pop()
            path.insert(0, next_cell)
            form_paths(next_cell, path)
        return


    #   recursive exploration of the grid   #
    def explore(cell):
        if cell == dest_cell:
            return
        find_next(cell)
        while back_track[cell][1]:
            next_cell = back_track[cell][1].pop()
            if next_cell not in back_track:
                back_track[next_cell] = [[cell], []]
                explore(next_cell)
            else:
                back_track[next_cell][0].append(cell)
        return
    #        ----------------------          #

    # existence of an entry for a cell in back_track shows that
    back_track[start_cell] = [[], []]
                                          # it has been explored.
    explore(start_cell)

    form_paths(dest_cell, [dest_cell])

    return path_list

if __name__ == "__main__":
    unittest.main()
