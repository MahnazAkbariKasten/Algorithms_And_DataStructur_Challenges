__author__ = 'pretymoon'

import collections
ff = open("\\Mahnaz\\PycharmProjects\\codeJam_practice_2016_1A\\BFF's\\C-small-practice.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    n = int(a[0])

    strLine = ff.readline()
    a = strLine.split(" ")
    f = [int(x)-1 for x in a]
    print(f)

    longest_path_to = collections.defaultdict(int)

    for i in range(n):
        visited = [False for x in range(n)]
        path_len = 0
        largest_loop = 0
        j = i
        p =[]
        #pre
        while not visited[j]:  # chain
            visited[j] = True
            # p.append(j)
            path_len += 1
            j = f[j]

        if i == j:  # The path is a loop with length of more than 2
            largest_loop = max(largest_loop, path_len)

        if f[f[j]] == j:  # the path ends with a loop of length 2
            longest_path_to[j] = max(longest_path_to[j], path_len)


    #     print(p, end='')
    # print(longest_path_to)
    print(max(largest_loop, sum(longest_path_to.values()) - len(longest_path_to)))




