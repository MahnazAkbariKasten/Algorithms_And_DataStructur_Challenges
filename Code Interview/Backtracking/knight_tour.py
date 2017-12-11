__author__ = 'pretty moon'
'''
http://www.csegeek.com/csegeek/view/tutorials/algorithms/backtrack/backtrack_part3.php
http://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/

Note that Backtracking is not the best solution for the Knight’s tour problem.
See below article for other better solutions.
http://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/
http://math.oregonstate.edu/~math_reu/proceedings/REU_Proceedings/Proceedings1996/1996Squirrel.pdf
'''

def is_valid_move(board, move):
    if not (0 <= move[0] < len(board)):
        return False
    if not (0 <= move[1] < len(board[0])):
        return False
    if board[move[0]][move[1]] == 1:
        return False
    return True


def iter_moves(cell):
    moves_list = []
    for i in [cell[0] - 2, cell[0] + 2]:
        for j in [cell[1] - 1, cell[1] + 1]:
            moves_list.append((i, j))
    for i in [cell[0] - 1, cell[0] + 1]:
        for j in [cell[1] - 2, cell[1] + 2]:
            moves_list.append((i, j))
    return moves_list


def find_knight_tour(board, cell, path):
    if len(path) == len(board) * len(board[0]):
        print(path)
        return True
    for move in iter_moves(cell):
        if is_valid_move(board, move):
            board[move[0]][move[1]] = 1
            path.append(move)
            if find_knight_tour(board, move, path):
                return True
            board[move[0]][move[1]] = 0
            path.pop()
    return False


def knight_tour_wrapper(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            path = []
            board[i][j] = 1
            path.append((i, j))
            if find_knight_tour(board, (i, j), path):
                return True
    print("No answer!")
    return False

# b = [[0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0]]

# input:
# b = [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]]
# output:
#  No answer!

# input:
# b = [[0, 0, 0, 0],
#      [0, 0, 0, 0],
#      [0, 0, 0, 0]]
# output:
# [(0, 0), (1, 2), (2, 0), (0, 1), (1, 3), (2, 1), (0, 2), (2, 3), (1, 1), (0, 3), (2, 2), (1, 0)]

# input:
# b = [[0, 0, 0, 0],
#      [0, 0, 0, 0],
#      [0, 0, 0, 0],
#      [0, 0, 0, 0]]
# output:
#  No answer!

# input:
# b = [[0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0]]
# output:
# [(0, 0), (2, 1), (0, 2), (1, 0), (3, 1), (2, 3), (0, 4), (1, 2), (3, 3), (1, 4), (2, 2), (3, 0), (1, 1), (0, 3),
#  (2, 4), (3, 2), (2, 0), (0, 1), (1, 3), (3, 4)]

# input:
# b = [[0 for i in range(4)] for j in range(5)]
# output:
# [(0, 0), (2, 1), (4, 0), (3, 2), (1, 3), (0, 1), (2, 0), (4, 1), (3, 3), (1, 2), (3, 1), (1, 0), (0, 2), (2, 3),
# (4, 2), (3, 0), (1, 1), (0, 3), (2, 2), (4, 3)]

# input:
# b = [[0 for i in range(5)] for j in range(5)]
# output:
# [(0, 0), (2, 1), (0, 2), (1, 0), (3, 1), (4, 3), (2, 2), (1, 4), (3, 3), (4, 1), (2, 0), (0, 1), (1, 3), (3, 4),
# (4, 2), (3, 0), (1, 1), (0, 3), (2, 4), (1, 2), (0, 4), (2, 3), (4, 4), (3, 2), (4, 0)]

# input:
b = [[0 for i in range(7)] for j in range(5)]
# output:
#

knight_tour_wrapper(b)
