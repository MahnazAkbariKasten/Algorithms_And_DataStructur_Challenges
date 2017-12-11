__author__ = 'pretymoon'
import itertools

#________________________________________#
def table_on_fly2(cur_row, prev_pat):  # n-1 , best_path
    while cur_row > 0:
        grid.insert(0, list(legal_row_patterns_list[prev_pat]))
        prev_pat = sum_table[cur_row - 1][prev_pat][1]
        cur_row -= 1

#________________________________________#
def table_on_fly(cur_row, prev_pat):  # , prev_pat
    while cur_row > 0:
        grid.insert(1, list(legal_row_patterns_list[prev_pat]))
        prev_pat = sum_table[cur_row - 1][prev_pat][1]
        cur_row -= 1

#________________________________________#
def is_compatible(my_table, my_row):
    legal_col_patterns = legal_row_patterns(len(my_table)+1)
    left_diag  = []
    right_diag = []
    curr_col = []
    for k in range(len(my_row)):  # col - my row
        left_diag  = [my_row[k]]
        right_diag = [my_row[k]]
        curr_col = [my_row[k]]
        for i in range(len(my_table[0])):  # col - table's cols
            for j in range(len(my_table)):   # row - table's rows
                if tuple(my_table[j]) not in legal_patterns:
                    return False
                if i == k:  # same col
                    curr_col.append(my_table[j][i])
                if i+j == k+len(my_table):  # right diag
                    right_diag.append(my_table[j][i])
                if i-j == k-len(my_table):
                    left_diag.append(my_table[j][i])

            if i == k and tuple(curr_col) not in legal_col_patterns:
                return False
        if right_diag.count("o") + right_diag.count("+") > 1 or left_diag.count("o") + left_diag.count("+") > 1:
            return False
    return True

#________________________________________#
def is_lpads(row_id, pattern):   # check for legal patterns applicable, considering designer selection for this row

    tmp = [choice for choice in director_choices if choice[0] == row_id]
    # selected = ["." for i in range(len(pattern))]
    # for choice in tmp:
    #     selected[choice[1]] = choice[2]
    # print("selected: ", selected)
    # print(" pattern: ", pattern)

    for choice in tmp:
        if pattern[choice[1]] == ".":
            # print(" False1")
            return False
        elif pattern[choice[1]] != choice[2] and pattern[choice[1]] != "o":
            # print(" False2")
            return False
    # print(" True")
    return True

#________________________________________#
def legal_row_patterns(girth):
    symbols = {"o": 2, "+": 1, "x": 1}
    tmp = ["." for j in range(girth)]
    legal_patterns = {tuple(tmp): 0}

    for i in range(girth):  # single symbol in a row
        for symbol in symbols:
            tmp = ["." for j in range(girth)]
            tmp[i] = symbol
            # print(tuple(tmp))
            legal_patterns[tuple(tmp)] = symbols[symbol]

    for cnt in range(2, girth+1):  # only "+"'s in a row
        myString = "+"*cnt
        myString += "."*(girth-cnt)
        tmp = [tuple(c) for c in itertools.permutations(myString, girth)]
        for tpl in tmp:
            legal_patterns[tpl] = cnt

    for cnt in range(1, girth):  # one or more "+"'s plus one more symbol
        myString = "+"*cnt
        myString += "."*(girth-cnt-1)
        for s in {"o", "x"}:
            this_string = myString
            this_string += s
            tmp = [tuple(c) for c in itertools.permutations(this_string, girth)]
            for tpl in tmp:
                # print(tpl, cnt, symbols[s])
                legal_patterns[tpl] = cnt + symbols[s]
    return legal_patterns

###############################################
ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_qualification\\problem_4\\D-small-practice.in", "r")
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_qualification\\problem_4\\D-small.in", "r")

numOfCases = int(ff.readline())
for test_case in range(1, numOfCases+1):
    print("Case #{}: ".format(test_case), end='')
    strLine = ff.readline()
    a = strLine.split(" ")
    n, m = [int(x) for x in a]
    director_choices = []
    select_rows = set([])
    for choice_row in range(m):
        strLine = ff.readline()
        a = strLine.split(" ")
        symbol = a[0]
        row = int(a[1]) - 1
        col = int(a[2]) - 1
        director_choices.append([row, col, symbol])
        select_rows.add(row)
###############################################
# numOfCases = int(input())
# for test_case in range(1, numOfCases+1):
#     print("Case #{}: ".format(test_case), end='')
#     strLine = input()
#     a = strLine.split(" ")
#     n, m = [int(x) for x in a]
#     director_choices = []
#     select_rows = set([])
#     for choice_row in range(m):
#         strLine = input()
#         a = strLine.split(" ")
#         symbol = a[0]
#         row = int(a[1]) - 1
#         col = int(a[2]) - 1
#         director_choices.append([row, col, symbol])
#         select_rows.add(row)
###############################################

    legal_patterns = legal_row_patterns(n)
    legal_row_patterns_list = list(legal_patterns)

    # print("legal_patterns \n", legal_patterns)
    # print("legal_row_patterns_list \n", legal_row_patterns_list)

    sum_table = [[[0, -1] for i in range(len(legal_row_patterns_list))] for j in range(n)]
    grid = []

    # initialize first row with value of each pattern
    for i in range(len(legal_row_patterns_list)):
        if 0 in select_rows and not is_lpads(0, legal_row_patterns_list[i]):
            sum_table[0][i][0] = - float("inf")
        else:
            sum_table[0][i][0] = legal_patterns[legal_row_patterns_list[i]]

    # print("sum_table0 \n", sum_table )

    # fill the sum table
    for u in range(1, n):  # row in stage
        for i in range(len(legal_row_patterns_list)):  # curr_row's column - one col per each legal patterns
            for p in range(len(legal_row_patterns_list)):  # prev_row's column col - one col per each legal patterns
                # is the curr pattern compatible (with designer selection of models) for this row

                if (u in select_rows and not is_lpads(u, legal_row_patterns_list[i])) or \
                        (u == 1 and 0 in select_rows and not is_lpads(0, legal_row_patterns_list[p])):
                    continue
                else:
                    # is the pattern compatible col-wise and diag-wise
                    grid = []
                    table_on_fly2(u, p)  # simulate the grid so far

                    # print("grid---")
                    # for i in range(len(grid)):
                    #     print(grid[i])
                    if is_compatible(grid, list(legal_row_patterns_list[i])):
                        tmp_sum = sum_table[u-1][p][0] + legal_patterns[legal_row_patterns_list[i]]
                        if sum_table[u][i][0] < tmp_sum:
                            sum_table[u][i][0] = tmp_sum
                            sum_table[u][i][1] = p

    #
    # print("sum_table1")
    # for i in range(len(sum_table)):
    #     print(sum_table[i])
    #

    # find the total max sum possible
    # keep track of the col results the max sum possible
    max_sum = 0
    best_pat = -1
    col = -1
    for i in range(len(sum_table[0])):
        if sum_table[-1][i][0] > max_sum:
            max_sum = sum_table[-1][i][0]
            best_pat = sum_table[-1][i][1]
            col = i

    #
    # print("col: ", col)
    #

    grid = []

    table_on_fly2(n-1, best_pat)
    #
    # print(grid)
    #
    grid.append(list(legal_row_patterns_list[col]))

    #
    # for i in range(len(grid)):
    #     print(grid[i])
    #

    count = 0
    for i in range(len(grid)):  # row
        for j in range(len(grid)):  # col
            if grid[i][j] != ".":
                count += 1
        if i in select_rows:
            tmp = [choice for choice in director_choices if choice[0] == i]
            for choice in tmp:
                if choice[2] == grid[i][choice[1]]:
                    count -= 1

    print(max_sum, count)

    for i in range(len(grid)):  # row
        for j in range(len(grid)):  # col
            if grid[i][j] != "." and [i, j, grid[i][j]] not in director_choices:
                print(grid[i][j], i+1, j+1)
