__author__ = 'pretymoon'

f = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodysJams\\CodysJamsInput", "r")

numOfCases = int(f.readline())

for i in range(1, numOfCases+1):
    print("Case #%d: " % i, end='')
    caseSize = int(f.readline())
    strLine = f.readline()
    a = strLine.split(" ")

    l = [int(x) for x in a]
    c12 = -1

    for n in l:
        if n % 12 == 0:
            if n * 4 / 3 == c12:
                c12 = -1
            else:
                print(n, " ", end='')
                c12 = n * 4 / 3
        elif n % 3 == 0:
            print(n, " ", end='')

    print("")