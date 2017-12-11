__author__ = 'pretymoon'

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\C-large-practice.in", "r")
# numOfCases = int(ff.readline())
#
# for case in range(1, numOfCases+1):
#     print("Case #{}: ".format(case))
#     strLine = ff.readline()
#     a = strLine.split(" ")
#     d, n = [int(x) for x in a]

numOfCases = int(input())

for i in range(1, numOfCases+1):
    strLine = input()
    a = strLine.split(" ")
    d, n = [int(x) for x in a]
    print("Case #:{0} d:{1} n:{2} ".format(i, d, n))