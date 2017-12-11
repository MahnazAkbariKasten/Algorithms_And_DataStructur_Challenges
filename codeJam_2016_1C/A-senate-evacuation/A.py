__author__ = 'pretymoon'

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2016_1C\\A-senate-evacuation\\A-small.in", "r")
ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2016_1C\\A-senate-evacuation\\A-large.in", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    n = int(a[0])

    strLine = ff.readline()
    a = strLine.split(" ")
    p = [int(x) for x in a]

    parties = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N",
               14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}
    num_non_0_parties = n

    while num_non_0_parties > 0:
        # print(p)
        if sum(p) == 2:
            maj1 = max(p)
            idx1 = p.index(maj1)
            p[idx1] -= 1
            maj2 = max(p)
            idx2 = p.index(maj2)
            p[idx2] -= 1
            print(parties[idx1], end='')
            print(parties[idx2], end=' ')
            num_non_0_parties -= 2
        elif num_non_0_parties == 2:
            maj1 = max(p)
            idx1 = p.index(maj1)
            p[idx1] -= 1
            if p[idx1] == 0:
                num_non_0_parties -= 1
            maj2 = max(p)
            idx2 = p.index(maj2)
            p[idx2] -= 1
            if p[idx2] == 0:
                num_non_0_parties -= 1
            print(parties[idx1], end='')
            print(parties[idx2], end=' ')
        else:
            maj1 = max(p)
            idx1 = p.index(maj1)
            p[idx1] -= 1
            if p[idx1] == 0:
                num_non_0_parties -= 1
            print(parties[idx1], end=' ')
    print()
