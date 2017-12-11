__author__ = 'pretymoon'

# from itertools import cycle

f = open("\\Mahnaz\\PycharmProjects\\codeJam\\DanceAroundTheClock\\dancersInput", "r")
numOfCases = int(f.readline())

for i in range(1, numOfCases+1):
    print("Case #%d: " % i, end='')
    strLine = f.readline()
    a = strLine.split(" ")

    d, k, n = [int(x) for x in a]

    if k%2 == 0:
        # oddNumbers = list(range(d-1,0,-2))
        # oddPool = cycle(oddNumbers)
        # while (p != k-1):
        #     p = next(oddPool)
        # for i in range(n -2):
        #     next(oddPool)
        # left = next(oddPool)
        # right = next(oddPool)

        # moore efficient way
        right2 = (k - 1 - 2 * n) % d
        left2 = (right2 - 2 ) % 2
        print(left2, " ", right2)
    else:
        # evenNumbers = list(range(2,d+1,2))
        # evenPool = cycle(evenNumbers)
        # p = int((k-1)/2)
        # for i in range(p + n - 1):
        #     next(evenPool)
        #
        # right = next(evenPool)
        # left = next(evenPool)

        right2 = ((k - 2 + 2 * n) % d) + 1
        left2 = ((k + 2 * n) % d) + 1
        print(left2, " ", right2)

f.close()

