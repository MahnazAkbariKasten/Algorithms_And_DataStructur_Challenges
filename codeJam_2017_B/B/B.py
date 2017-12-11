__author__ = 'pretymoon'
import math

def solve():
    i = 0
    j = 0
    going = True
    while going:
        while uniuni[j][0]==0:
            j += 1
            if j>5:
                going = False
                break
            elif j==5 and uniuni[j][0]==0:
                going = False
                break
        else:
            if i >= n:
                i = 1

            stall[i] = uniuni[j][1]
            uniuni[j][0] -= 1

            i += 2

ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_B\\B\\B-small.in", "r")
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_B\\B\\B-large.in", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')
    uni_sym = ["R", "O", "Y", "G", "B", "V"]
    strLine = ff.readline()
    a = strLine.split(" ")
    n, r, o, y, g, b, v = [int(x) for x in a]
    uni = [r, o, y, g, b, v]
    uni_max = max(uni)
    uniuni=[]
    for i in range(len(uni_sym)):
        uniuni.append([uni[i], uni_sym[i]])
    uniuni.sort()
    uniuni.reverse()
    stall = [" " for i in range(n)]
    # my_dict = {("r","r"):0, ("o","o"):0, ("y","y"):0, ("g","g"):0, (,):0,(,):0, (,):0, (,):0, (,):0, (,):0, (,):0,(,):0, (,):0, (,):0,
    # ():1, }
    if uni_max> math.floor(n/2):
        print("IMPOSSIBLE")
    else:
        solve()
        for i in range(n):
            print(stall[i], end='')
        print()

