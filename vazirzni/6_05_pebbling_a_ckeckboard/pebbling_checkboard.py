__author__ = 'pretymoon'

# board = [[2, 50, 2, 2], [2, 100, 2, 2], [2, 2, 100, 2], [2, 2, 2, 100]]
# board = [[1, 50, 1, 1], [1, 100, 1, 1]]
board = [[1, 50, 1, 1]]

comp_table = [[0], [1, 0], [1, 1, 0], [1, 1, 1, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0]]

placement = [[-1 for i in range(4)] for j in range(len(board))]
pattern_traceback = [[-1 for i in range(7)] for j in range(len(board))]

def are_compatible(pat1, pat2):
    if pat2 > pat1:
        return comp_table[pat2][pat1]
    else:
        return comp_table[pat1][pat2]


def pattern(row_num, pat_num):
    if 0 <= pat_num <= 3:
        placement[row_num][pat_num] = board[row_num][pat_num]
        return 
    elif pat_num == 4:
        placement[row_num][0] = board[row_num][0]
        placement[row_num][2] = board[row_num][2]
        return 
    elif pat_num == 5:
        placement[row_num][1] = board[row_num][1]
        placement[row_num][3] = board[row_num][3]
        return 
    elif pat_num == 6:
        placement[row_num][0] = board[row_num][0]
        placement[row_num][3] = board[row_num][3]
        return 


def p(this_row):
    return [this_row[0], this_row[1], this_row[2], this_row[3], this_row[0]+this_row[2], this_row[1]+this_row[3], this_row[0]+this_row[3]]


curr_row = p(board[0])

for row in range(1, len(board)):  # row
    peb = p(board[row])
    prev_row = curr_row.copy()
    curr_row = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(comp_table)):  # prev peb
        for j in range(len(comp_table)):  # curr peb
            if are_compatible(i, j):
                tmp = prev_row[i] + peb[j]
                if tmp > curr_row[j]:
                    pattern_traceback[row][j] = i
                    curr_row[j] = tmp

pat = curr_row.index(max(curr_row))
pattern(len(board)-1, pat)



for row in range(len(board)-1, 0, -1):
    pattern(row-1, pattern_traceback[row][pat])
    pat = pattern_traceback[row][pat]


print("-"*7, "check board", "-"*7)
for i in range(len(board)):
    print(board[i])


print("")
print("-"*7, "pebbles' placement ", "-"*7)
for i in range(len(placement)):
    print(placement[i])


print("")
print("-"*20)
print("Total Max Sum: ", max(curr_row))