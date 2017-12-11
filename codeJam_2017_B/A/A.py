__author__ = 'pretymoon'

ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_B\\A\\A-large.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    d, n = [int(x) for x in a]

    h = []
    for l in range(n):
        strLine = ff.readline()
        a = strLine.split(" ")
        k, s = [int(x) for x in a]
        h.append((k, s))

    max_l = 0
    for i in range(n):
        ll = (d - h[i][0])/h[i][1]
        if max_l < ll:
            max_l = ll
    annie = d/max_l

    print(annie)