__author__ = 'pretymoon'

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\C-large-practice.in", "r")
ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\D-small-input", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{} :".format(case))
    strLine = ff.readline()
    b = int(strLine) # number of buildings
    # print("number of building: {}".format(b))

    d = []
    for i in range(2, b+1):
        strLine = ff.readline()
        a = strLine.split(" ")
        d.append([int(x) for x in a])

    dd=[]

    if d[b-2][0] == -1:
        dd.append([float("inf")])
    else:
        dd.append(d[b-2][0]/2)

    for i in range(2, 2 * len(d) - 1, 2):
        row = []
        row.append()
        for j in range(i-2,0,-1):

        dd.append(row)


    print(dd)
# numOfCases = int(input())
#
# for case in range(1, numOfCases+1):
#     # print("Case #{}: ".format(i))
#     strLine = input()
#     a = strLine.split(" ")
#     d, n = [int(x) for x in a]