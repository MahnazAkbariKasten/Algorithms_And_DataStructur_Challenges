__author__ = 'pretymoon'

import itertools

ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\B-small-input", "r")
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\B-small-practice.in", "r")

numOfCases = int(ff.readline())

for i in range(1, numOfCases+1):
    print("Case #{}: ".format(i), end='')
    strLine = ff.readline()
    n = int(strLine)
    strLine = ff.readline()
    a = strLine.split(" ")
    p = [float(x) for x in a]

    maxSuccessP= 0

    # permutations()
    for permutation in itertools.permutations(p):
        success = 1
        for itemId in range(0, len(permutation), 2):
            success = success * (1 - p[itemId] * p[itemId + 1])

        if success > maxSuccessP:
            maxSuccessP = success

    print(maxSuccessP, " ", p)

    # combinations()
    for combo in itertools.combinations(p, 2):
        print(combo)

# count()
for seq in itertools.count(start=0, step=0.5):
    print(seq, " ", end='')
    if seq >= 5:
        break

def genCycle():
    mylist = ["a", "b", "c", "d"]
