__author__ = 'pretymoon'


def solve(mm):
    for row in range(1, bb-1):
        for col in range(row+1, bb):
            table[row][col] = 1
    for col in range(1, bb):
        exp = max(bb-2-col, 0)
        if mm >= 2 ** exp:
            table[0][col] = 1
            mm -= 2 ** exp


ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2016_1C\\B-slides\\B-small.in", "r")
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2016_1C\\B-slides\\B-large.in", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    aa = strLine.split(" ")
    bb, mm = [int(x) for x in aa]

    if 2 ** (bb - 2) < mm:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        table = [[0 for i in range(bb)] for j in range(bb)]
        solve(mm)
        for i in range(bb):
            for j in range(bb):
                print(table[i][j], end='')
            print()


