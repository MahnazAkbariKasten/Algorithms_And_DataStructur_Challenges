__author__ = 'pretymoon'

def solve(r1,c1,r2,c2):
    cnt=0
    init =""
    for i in range(r1, r2+1):
        for j in range(c1,c2+1):
            if g[i][j] != "?":
                cnt += 1
                init = g[i][j]
    if cnt == 1:
        for i in range(r1, r2+1):
            for j in range(c1,c2+1):
               g[i][j] = init
        return True
    elif cnt> 1:
        for k in range(r1,r2):
            if solve(r1,c1,k,c2) and solve(k+1,c1,r2,c2):
                return True
        for k in range(c1,c2):
            if solve(r1,c1,r2,k) and solve(r1,k+1,r2,c2):
                return True
    else:
        pass

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_1A\\A-alphabet-cake\\A-alphabet-cake-small.in", "r")
ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_1A\\A-alphabet-cake\\A-alphabet-cake-large.in", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case))

    strLine = ff.readline()
    a = strLine.split(" ")
    r, c = [int(i) for i in a]

    g = []
    rows=set([])
    for i in range(r):
        strLine = ff.readline()
        a = strLine.split(" ")
        aa = a[0].strip()
        g.append([])
        for j in range(c):
            g[i].append(aa[j:j+1])
            if aa[j:j+1] != "?":
                rows.add(i)

    solve(0,0,r-1,c-1)

    for m in range(r):
        for t in range(c):
            print(g[m][t], end='')
        print()
