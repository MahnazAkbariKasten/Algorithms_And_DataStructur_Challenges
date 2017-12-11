__author__ = 'pretymoon'

ff = open("C:\\Mahnaz\\PycharmProjects\\leetcode\\coinChange2\\coinChange2Input.in", 'r')

strLine = ff.readline()
numOfCases = int(strLine)

for case in range(1, numOfCases+1):
    strLine = ff.readline()
    amount = int(strLine)

    strLine = ff.readline()
    a = strLine.split(" ")
    coinDenom = [int(x) for x in a]

    coinDenom.sort()
    
    k = [[0 for i in range(len(coinDenom))] for i in range(amount + 1)]
    k[0] = [1 for i in range(len(coinDenom))]

    for v in range(1, amount + 1):
        if v % coinDenom[0] == 0:
            k[v][0] = 1
    # print(k)

    for i in range(1, len(coinDenom)):
        for v in range(1,amount + 1):
            if v < coinDenom[i]:
                k[v][i] = k[v][i - 1]
            else:
                k[v][i] = k[v][i - 1] + k[v - coinDenom[i]][i]

    print("Case #{0}: {1}".format(case, k[amount][len(coinDenom) - 1]))





