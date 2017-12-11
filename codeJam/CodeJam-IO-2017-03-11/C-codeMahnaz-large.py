__author__ = 'pretymoon'
import math
import itertools

# # ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\C-large-practice.in", "r")
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\C-small-input", "r")
#
# numOfCases = int(ff.readline())
#
# for case in range(1, numOfCases+1):
#
#     strLine = ff.readline()
#     a = strLine.split(" ")
#     d, n = [int(x) for x in a]

numOfCases = int(input())

for case in range(1, numOfCases+1):
    # print("Case #{}: ".format(i))
    strLine = input()
    a = strLine.split(" ")
    d, n = [int(x) for x in a]


    if n <= 14:
        capPerRow = 7
        fullRow = n//capPerRow
        extraCol = n % capPerRow
    else:
        fullRow = 2
        n -= 14
        capPerRow = 21
        extraCol = n % capPerRow
        fullRow += n//capPerRow

    print("Case #{0}:".format(case))

    # print(fullRow, extraCol)

    if fullRow == 0:
        if extraCol == 0:
            print("I//////////////")
        elif extraCol == 1:
            print("I/O////////////")
        elif extraCol == 2:
            print("I/O/I//////////")
        elif extraCol == 3:
            print("I/O/I/O////////")
        elif extraCol == 4:
            print("I/O/I/O/I//////")
        elif extraCol == 5:
            print("I/O/I/O/I/O////")
        elif extraCol == 6:
            print("I/O/I/O/I/O/I//")
        elif extraCol == 7:
            print("I/O/I/O/I/O/I/O")
    elif fullRow == 1:
        print("I/O/I/O/I/O/I/O")
        if extraCol == 0:
            print("I//////////////")
        elif extraCol == 1:
            print("I/O////////////")
        elif extraCol == 2:
            print("I/O/I//////////")
        elif extraCol == 3:
            print("I/O/I/O////////")
        elif extraCol == 4:
            print("I/O/I/O/I//////")
        elif extraCol == 5:
            print("I/O/I/O/I/O////")
        elif extraCol == 6:
            print("I/O/I/O/I/O/I//")
        elif extraCol == 7:
            print("I/O/I/O/I/O/I/O")
    elif fullRow == 2 and extraCol == 0:
        print("I/O/I/O/I/O/I/O")
        print("I/O/I/O/I/O/I/O")
    else:
        for i in range(fullRow):
            print("I/O/I/O/I/O/I/O")
        if extraCol == 1:
            print("I//////////////")
        elif extraCol == 2:
            print("//O////////////")
        elif extraCol == 3:
            print("IOO////////////")
        elif extraCol == 4:
            print("OOOOI//////////")
        elif extraCol == 5:
            print("IOOOI//////////")
        elif extraCol == 6:
            print("OOOOIOO////////")
        elif extraCol == 7:
            print("IOOOIOO////////")
        elif extraCol == 8:
            print("OOOOIOOOI//////")
        elif extraCol == 9:
            print("IOOOIOOOI//////")
        elif extraCol == 10:
            print("OOOOIOOOIOO////")
        elif extraCol == 11:
            print("IOOOIOOOIOO////")
        elif extraCol == 12:
            print("OOOOIOOOIOOOI//")
        elif extraCol == 13:
            print("IOOOIOOOIOOOI//")
        elif extraCol == 14:
            print("IOOOIOOOIOOOIOO")
        elif extraCol == 15:
            print("I/OOIOOOIOOOIOO")
        elif extraCol == 16:
            print("I/O/IOOOIOOOIOO")
        elif extraCol == 17:
            print("I/O/I/OOIOOOIOO")
        elif extraCol == 18:
            print("I/O/I/O/IOOOIOO")
        elif extraCol == 19:
            print("I/O/I/O/I/OOIOO")
        elif extraCol == 20:
            print("I/O/I/O/I/O/IOO")
        elif extraCol == 21:
            print("I/O/I/O/I/O/I/O")


#################################
# print("   ", end='')
# for j in range(15):
#     print((j%10), "", end='')
# print()
# for k in range(15):
#     print(repr(k).rjust(2), "", end='')
#     print(("I / O / I / O / I / O / I / O"))



