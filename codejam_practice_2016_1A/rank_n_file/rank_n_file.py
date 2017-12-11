__author__ = 'pretymoon'

import collections

ff = open("\\Mahnaz\\PycharmProjects\\codeJam_practice_2016_1A\\rank_n_file\\B-large-practice.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    cnt = collections.Counter()
    print("Case #{}: ".format(case), end='')
    strLine = ff.readline()
    a = strLine.split(" ")
    n = int(a[0])
    for i in range(2*n-1):
        strLine = ff.readline()
        a = strLine.split(" ")
        line = [int(x) for x in a]
        for num in line:
            cnt[num] += 1
    missing_row = []
    for num in cnt.items():
        if num[1] % 2 == 1:
            missing_row.append(num[0])
    missing_row.sort()
    for x in missing_row:
        print(x, end=' ')
    print()

