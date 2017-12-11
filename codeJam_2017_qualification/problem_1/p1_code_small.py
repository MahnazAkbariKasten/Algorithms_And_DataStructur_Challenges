__author__ = 'pretymoon'
def flip(idx, girth):
    for i in range(girth):
        if pancakes[idx+i] == "+":
            pancakes[idx+i] = "-"
        else:
            pancakes[idx+i] = "+"
    return
###############################################
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_qualification\\problem_1\\problem_1_small.in", "r")
# numOfCases = int(ff.readline())
#
# for i in range(1, numOfCases+1):
#     print("Case #{}: ".format(i), end='')
#     strLine = ff.readline()

###############################################
numOfCases = int(input())
for i in range(1, numOfCases+1):
    print("Case #{}: ".format(i), end='')
    strLine = input()

###############################################

    a = strLine.split(" ")
###############################################

    pancakes = list(a[0])
    k = int(a[1])

    start = 0
    end = len(pancakes) - 1
    num_of_flips = 0

    while end - start + 1 > k:
        if pancakes[start] == "+":
            start += 1
        else:
            flip(start, k)
            num_of_flips += 1
            start += 1

        if pancakes[end] == "+":
            end -= 1
        else:
            flip(end-k+1, k)
            num_of_flips += 1
            end -= 1
    if len(pancakes[start:end+1]) == k and pancakes[start:end+1].count("-") == k:
        flip(end-k+1, k)
        num_of_flips += 1

    if pancakes[start:end+1].count("-") > 0:
        print("IMPOSSIBLE")
    else:
        print(num_of_flips)






