__author__ = 'pretty moon'

'''
Problem :-
Given a maze in the form of a matrix of size n x n with all elements as 0 or 1.
0 denotes safe cell & 1 denotes dangerous cell.
A rat is placed at cell ( 0, 0 ). Print a safe path ( if exists ) which rat can take to reach last cell ( n-1, n-1 ).
Constraint :- Rat can move rightwards ( R ) or downwards ( D ).
'''

def safe_path(row, col):
    m = len(maze)
    n = len(maze[0])
    if row == m - 1 and col == n - 1:
        maze[row][col] = 2
        for maze_row in maze:
            print(maze_row)
        return True

    if row == m - 1:
        if maze[row][col + 1] == 0:
            maze[row][col] = 2
            if not safe_path(row, col + 1):
                maze[row][col] = 0
                return False
            return True
        return False

    if col == n - 1:
        if maze[row + 1][col] == 0:
            maze[row][col] = 2
            if not safe_path(row + 1, col):
                maze[row][col] = 0
                return False
            return True
        return False

    maze[row][col] = 2
    if maze[row][col + 1] == 0:
        if safe_path(row, col + 1):
            return True
    if maze[row + 1][col] == 0:
        if safe_path(row + 1, col):
            return True
    maze[row][col] = 0
    return False


def print_safe_path(maze):
    safe_path(0, 0)

maze = [[0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]]

for maze_row in maze:
    print(maze_row)
print()

print_safe_path(maze)