__author__ = 'pretymoon'

ff = open("C:\\Mahnaz\\PycharmProjects\\leetcode\\singleElementInSortedArr\\singleElementInput.in",'r')

strLine = ff.readline()

numOfCases = int(strLine)

for case in range(1, numOfCases + 1):

    strLine = ff.readline()
    a = strLine.split(" ")
    sortedArray = [int(x) for x in a]

    s = 0
    e = len(sortedArray) - 1

    q = 0

    while q == 0:
        if s == e:
            print("Case #{0}: {1}".format(case, sortedArray[s]), sortedArray)
            q = 1
        else:
            m = int((s + e)/2)
            if sortedArray[m] == sortedArray[m-1] and m % 2 == 0:
                e = m - 2
            elif sortedArray[m] == sortedArray[m+1] and m % 2 == 0:
                s = m + 2
            elif sortedArray[m] == sortedArray[m+1] and m % 2 == 1:
                e = m - 1
            elif sortedArray[m] == sortedArray[m-1] and m % 2 == 1:
                s = m + 1
            else:
                s = e = m
