__author__ = 'prettymoon'


numOfCases = int(input())
for i in range(1, numOfCases+1):
    print("Case #{}: ".format(i), end='')
    strLine = input()
    a = strLine.split(" ")
    f, s = [int(x) for x in a]

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam\\CodeJam-IO-2017-03-11\\A-small-attempt0.in", "r")
# numOfCases = int(ff.readline())
#
# for i in range(1, numOfCases+1):
#     print("Case #{}: ".format(i), end='')
#     strLine = ff.readline()
#     a = strLine.split(" ")
#     f, s = [int(x) for x in a]

    largest = 0
    curr=[0 for x in range(s+1)]
    dict = {}

    for j in range(1,f+1):
        strLine = input()
        a = strLine.split(" ")
        r, c = [int(x) for x in a]

        if (r,c) in dict:
            dict.pop((r,c))
        else:
            dict[(r,c)]=0
            curr[r-1]=curr[r-1]+1
            if r!=c:
                curr[c-1]=curr[c-1]+1


    for k in range(s):
        if curr[k]> largest:
            largest=curr[k]



    print(largest)
