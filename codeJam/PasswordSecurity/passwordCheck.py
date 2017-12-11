__author__ = 'pretymoon'

import random

f = open("\\Mahnaz\\PycharmProjects\\codeJam\\PasswordSecurity\\passwordSecurityInput", "r")
numOfCases = int(f.readline())

for i in range(1, numOfCases+1):
    print("Case #%d: " % i, end='')
    numOfPass = int(f.readline())
    strLine = f.readline()
    a = strLine.split(" ")
    passList = [x.strip() for x in a]

    if numOfPass == 1:
        if len(passList[0]) == 1:
            print("impossible")
        else:
            az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            loc = az.find(passList[0])
            if loc == -1:
                print(az)
            else:
                new = ''.join(random.sample(passList[0], len(passList[0])))
                print(az[:loc].strip(), end='')
                print(new, end='')
                print(az[(loc + len(passList[0])):].strip())
    else:
        for i in range(100):
            new = ''.join(random.sample(az,26))
            for password in passList:
                if password in new:
                    new = "impossible"
                    break

            if new != "impossible":
                break

        print(new)
