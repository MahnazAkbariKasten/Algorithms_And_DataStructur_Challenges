__author__ = 'pretymoon'

import math

f = open("\\Mahnaz\\PycharmProjects\\codeJam\\Polynesiaglot\\PolynesiaglotInput", "r")
numOfCases = int(f.readline())

for i in range(1, numOfCases+1):
    #print("case #%d: " % i, end='')
    strLine = f.readline()
    a = strLine.split(" ")

    c, v, l = [int(x) for x in a]

    result = v ** l
    #print("0 ", result)

    iterNum = math.ceil(l/2)

    for j in range(1, iterNum + 1):
        result += int((math.factorial(l-j) / (math.factorial(l-2*j) * math.factorial(j))) * (v ** (l-j)) * (c ** j)) % ((10 ** 9) + 7)
        #print(j, " ", result)

    print("Case #%d: " % i, result)