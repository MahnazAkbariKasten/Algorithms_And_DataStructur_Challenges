__author__ = 'pretymoon'
import math
import itertools

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\C-small-input", "r")
# numOfCases = int(ff.readline())
#
# for i in range(1, numOfCases+1):
#     print("Case #{}: ".format(i))
#     strLine = ff.readline()
#     a = strLine.split(" ")
#     d, n = [int(x) for x in a]

numOfCases = int(input())

for i in range(1, numOfCases+1):
    print("Case #{}: ".format(i))
    strLine = input()
    a = strLine.split(" ")
    d, n = [int(x) for x in a]

    capPerRow = math.floor(d/3)
    fullRow = math.floor(n/capPerRow)
    extraCol = n % capPerRow

    # print(fullRow, extraCol)

    if fullRow == 0:
        if extraCol == 0:
            print("I")
        else:
            for j in range(extraCol):
                print("I/O", end='')
            print()
    else:
        for k in range(fullRow):
            row = ''.join(itertools.repeat('I/O',16))
            print(row)
            row = ''.join(itertools.repeat('O',48))
            print(row)
        for j in range(extraCol):
            print("I/O", end='')
        filler = 48 - (extraCol * 3)
        for j in range(filler):
            print("O", end='')
        print()
