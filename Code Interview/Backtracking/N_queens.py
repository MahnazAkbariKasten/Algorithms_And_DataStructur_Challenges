__author__ = 'pretty moon'
'''
https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/

We start from far left column and place a queen in first row and try to solve the problem for rest of columns.
If there is no answer, then we backtrack and move the queen in first column to the second row and repeat the process
till we find an answer or we find out that we have tried all the possible arrangement, and none have worked.

This strategy allows us not be be worried about the cells on the right side of current cell, because we are using the
columns from left to right.

Basically, backtracking is a very systematic brute-force technique.
'''

def print_matrix(b):
    for i in range(len(b)):
        print(b[i])


def is_attacked(board, cell):
    s = len(board)
    x = cell[0]
    y = cell[1]
    # checking for row and column
    if sum(board[x]) > 0:
        return True

    if sum([row[y] for row in board]) > 0:
        return True

    # checking diagonals
    while x >= 0 and y < s:  # check lower-right-diagonal
        if board[x][y] == 1:
            return True
        x -= 1
        y += 1

    # x = cell[0]
    # y = cell[1]
    # while x < s and y >= 0:  # check lower-left-diagonal
    #     if board[x][y] == 1:
    #         return True
    #     x += 1
    #     y -= 1

    x = cell[0]
    y = cell[1]
    while x >= 0 and y >= 0:  # check upper-left-diagonal
        if board[x][y] == 1:
            return True
        x -= 1
        y -= 1

    # x = cell[0]
    # y = cell[1]
    # while x < s and y < s:  # check lower-right-diagonal
    #     if board[x][y] == 1:
    #         return True
    #     x += 1
    #     y += 1

    return False


def N_queens(board, N):
    s = len(board)
    if N == 0:
        print_matrix(board)
        return True
    for i in range(s):
        for j in range(s):
            if not is_attacked(board, (i, j)):
                board[i][j] = 1
                if N_queens(board, N-1):
                    return True

                # Can not place a queen in this position, backtrack and try other positions
                board[i][j] = 0
    return False


b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
print(3, N_queens(b, 3))

b = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
print(4, N_queens(b, 4))

b = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]
print(5, N_queens(b, 5))

b = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]
print(6, N_queens(b, 6))