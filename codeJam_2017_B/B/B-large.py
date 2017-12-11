__author__ = 'pretymoon'
import math


def solve_large():
    idx = 0
    for j in range(1,6,2):
        if uni_quantity[j] > 0:
            nei_bor = (j + 3) % 6

            if uni_quantity[j] + uni_quantity[nei_bor] < n:
                stall[idx] = uni_symbol[nei_bor]
                idx += 1
                uni_quantity[nei_bor] -= 1

            while uni_quantity[j] > 0:
                stall[idx] = uni_symbol[j]
                idx += 1
                uni_quantity[j] -= 1

                stall[idx] = uni_symbol[nei_bor]
                idx += 1
                uni_quantity[nei_bor] -= 1

    return idx


def solve_small(begin):
    i = begin
    j = uni_quantity.index(max(uni_quantity))
    while max(uni_quantity) > 0:
        while i < n and uni_quantity[j] > 0:
            stall[i] = uni_symbol[j]
            uni_quantity[j] -= 1
            i += 2

        if i >= n:
            i = begin + 1
        elif uni_quantity[j] == 0:
            j = uni_quantity.index(max(uni_quantity))


ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_B\\B\\B-large.in", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')
    uni_symbol = ["R", "O", "Y", "G", "B", "V"]
    strLine = ff.readline()
    a = strLine.split(" ")
    n, r, o, y, g, b, v = [int(x) for x in a]
    uni_quantity = [r, o, y, g, b, v]
    stall = [" " for i in range(n)]

    #### used when every combo is possible
    nn = n
    bb = b
    rr = r
    yy = y
    if o > 0:
        bb = b - o - 1
        nn -= 2 * o + 1
    if g > 0:
        rr = r - g - 1
        nn -= 2 * g + 1
    if v > 0:
        yy = y - v - 1
        nn -= 2 * v + 1
    ####
    if   (o+b == n and o != b):
        print("IMPOSSIBLE 1")
    elif (v+y == n and v != y):
        print("IMPOSSIBLE 2")
    elif (g+r == n and g != r):
        print("IMPOSSIBLE 3")
    elif o == g == v == 0 and max(r, y, b) > math.floor(n/2):
        print("IMPOSSIBLE 4")
    elif o > 0 and ((o >= b and (y > 0 or r > 0)) or (bb != 0 and float(bb) == nn/2)):
        print("IMPOSSIBLE 5")
    elif v > 0 and ((v >= y and (r > 0 or b > 0)) or (yy != 0 and float(yy) == nn/2)):
        print("IMPOSSIBLE 6")
    elif g > 0 and ((g >= r and (y > 0 or b > 0)) or (rr != 0 and float(rr) == nn/2)):
        print("IMPOSSIBLE 7")
    elif (o > 0 or g > 0 or v > 0) and (max(rr, yy, bb) > math.ceil(nn/2) or (max(rr, yy, bb) != 0 and max(rr, yy, bb) == nn)):
        print("IMPOSSIBLE 8")
    else:
        begin_here = solve_large()
        solve_small(begin_here)
        for i in range(n):
            print(stall[i], end='')
        print()

