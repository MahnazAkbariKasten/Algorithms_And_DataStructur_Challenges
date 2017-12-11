__author__ = 'pretymoon'

f = open("\\Mahnaz\\PycharmProjects\\codeJam\\Reverse Words\\ReverseWordsInput")

numOfCases = int(f.readline())

for case in range(1, numOfCases + 1):
    print("Case #%d:" % case, end='')

    strLine = f.readline()
    a = strLine.split()

    for j in range(len(a)):
        print(" ", a.pop(), end='')

    print()