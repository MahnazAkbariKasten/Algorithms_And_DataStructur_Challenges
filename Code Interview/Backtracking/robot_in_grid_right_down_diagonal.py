__author__ = 'pretty moon'

'''
http://www.csegeek.com/csegeek/view/tutorials/algorithms/backtrack/backtrack_part1.php

PROBLEM: Given a maze in the form of a matrix of size m x n. A robot is placed at cell ( 0, 0 ).
Print all possible paths that robot can take to reach the last cell ( n-1, n-1 ) of the maze.
Constraint :- Robot can move rightwards ( R ) or downwards ( D ) or diagonal_right_down ( G).

We need to keep track of the path paved to get to the cell and add to path along the way.
If you go to the next column then we add "R". If we go to the next row, then we add "D" to the path.

'''


def all_paths(path, m, n, row, col):
    if row == m - 1 and col == n - 1:
        print(path)
        return

    if row == m - 1:
        all_paths(path + "R", m, n, row, col + 1)
        return

    if col == n - 1:
        all_paths(path + "D", m, n, row + 1, col)
        return

    all_paths(path + "R", m, n, row, col + 1)
    all_paths(path + "D", m, n, row + 1, col)
    all_paths(path + "G", m, n, row + 1, col + 1)


all_paths("", 2, 2, 0, 0)
