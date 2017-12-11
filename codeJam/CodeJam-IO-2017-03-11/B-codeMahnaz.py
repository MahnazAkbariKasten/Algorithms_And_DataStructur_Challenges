__author__ = 'pretymoon'

# # ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\B-small-input", "r")
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\B-small-practice.in", "r")
#
# numOfCases = int(ff.readline())
#
# for i in range(1, numOfCases+1):
#     # print("Case #{}: ".format(i), end='')
#     strLine = ff.readline()
#     n = int(strLine)
#     strLine = ff.readline()
#     a = strLine.split(" ")
#     p = [float(x) for x in a]

numOfCases = int(input())
for i in range(1, numOfCases+1):
    # print("Case #{}: ".format(i), end='')
    strLine = input()
    n = int(strLine)
    strLine = input()
    a = strLine.split(" ")
    p = [float(x) for x in a]

    p.sort()
    # success1=1
    success2=1
    for k in range(n):
        # print("k: {0} , j: {1}   ".format(k,(2*n-k-1)))
        # success1 = success1 * (2 - p[k] - p[2*n-k-1] - ((1 - p[k])* (1-p[2*n-k-1])))
        success2 = success2 * (1 - p[k]* p[2*n-k-1])
    print("Case #{}: ".format(i), success2)