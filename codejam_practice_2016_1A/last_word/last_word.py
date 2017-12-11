__author__ = 'pretymoon'

###############################################
ff = open("\\Mahnaz\\PycharmProjects\\codeJam_practice_2016_1A\\last_word\\A-large-practice.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')
    strLine = ff.readline()
###############################################
# numOfCases = int(input())
# for i in range(1, numOfCases+1):
#     print("Case #{}: ".format(i), end='')
#     strLine = input()
###############################################
    a = strLine.split(" ")
    s = a[0].strip()
###############################################
    last_word = [s[0:1]]
    for i in range(1, len(s)):
        if s[i:i+1] >= last_word[0]:
            last_word.insert(0, s[i:i+1])
        else:
            last_word.append(s[i:i+1])

    print("".join(x for x in last_word))

