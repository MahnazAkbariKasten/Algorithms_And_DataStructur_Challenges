__author__ = 'pretymoon'

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\B-small-input", "r")
# numOfCases = int(ff.readline())
#
# for i in range(1, numOfCases+1):
#     print("Case #{}: ".format(i), end='')
#     strLine = ff.readline()
#     n = int(strLine)
#     strLine = ff.readline()
#     a = strLine.split(" ")
#     p = [float(x) for x in a]

numOfCases = int(input())
for i in range(1, numOfCases+1):
    print("Case #{}: ".format(i), end='')
    strLine = input()
    n = int(strLine)
    strLine = input()
    a = strLine.split(" ")
    p = [float(x) for x in a]

    p.sort()
    fail=0
    for i in range(n):
        fail = fail + (p[i]*p[n-i])
    print(1-fail)