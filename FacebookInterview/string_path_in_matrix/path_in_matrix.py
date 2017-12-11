__author__ = 'pretymoon'

def path_in_matrix(s):
    if len(m) == 0:
        return False

    for i in range(len(m)):
        for j in range(len(m[0])):
            result.clear()
            if explore(i, j, s):
                return True

    return False


def explore(row, col, st):
    to_be_explored = neighbours(row, col) - result
    tmp = False
    if len(to_be_explored) == 0:
        return False
    elif len(st) == 1:
        for ii, jj in to_be_explored:
            if st[0] == m[ii][jj]:
                result.add((ii, jj))
                return True
        return False
    else:
        for ii, jj in to_be_explored:
            tmp_result = set({})
            if st[0] == m[ii][jj]:
                result.add((ii, jj))
                tmp_result.add((ii, jj))
                tmp = explore(ii, jj, st[1:])
                if not tmp:
                    for x in tmp_result:
                        result.remove(x)
                else:
                    return True
        return tmp


def neighbours(row, col):
    nb = set({})
    if row > 0:
        if col > 0:
            nb.update({(row, col-1), (row-1, col-1), (row-1, col)})
        else:
            nb.update({(row-1, col)})

        if col < (len(m[0]) - 1):
            nb.update({(row-1, col+1)})
    else:
        if col > 0:
            nb.update({(row, col-1)})

    if row < (len(m) - 1):
        if col < (len(m[0]) - 1):
            nb.update({(row, col+1), (row+1, col), (row+1, col+1)})
        else:
            nb.update({(row+1, col)})

        if col > 0:
            nb.update({(row+1, col-1)})
    else:
        if col < (len(m[0]) - 1):
            nb.update({(row, col+1)})

    return nb


m = [['A', 'B', 'C', 'E'], ['X', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
# m = [['A','B'],['S','F']]
result = set({})
print("found? ", path_in_matrix("ABFCSE"))

print('---------------')

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end='')
    print()

print('---------------')

for i in range(len(m)):
    for j in range(len(m[0])):
        if (i,j) in result:
            print(m[i][j], end='')
        else:
            print('+', end='')
    print()

