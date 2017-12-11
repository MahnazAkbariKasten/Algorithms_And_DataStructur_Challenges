__author__ = 'pretymoon'

f = open("\\Mahnaz\\pycharmProjects\\codeJam\\ManyPrizes\\manyPrizesInput")

numOfCases = int(f.readline())

for i in range(1, numOfCases + 1):
    print("Case #{0}: ".format(i), end='')
    strList = f.readline()
    a = strList.split()
    n, p = (int(x) for x in a)

    tournamentList = [x for x in range(2**n)]
    record = [0 for x in range(2**n)]



    print(n, " ", p, " ", tournamentList, record)