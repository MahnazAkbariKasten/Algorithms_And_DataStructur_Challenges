__author__ = 'pretymoon'

def is_proper(quan, idx, serv):
    tmp = r[idx] * serv
    if quan < tmp * .9:
        return -1
    elif quan > tmp * 1.1:
        return -2
    else:
        return 1

# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_1A\\B-ratatouille\\B-ratatouille-small.in", "r")
ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_1A\\B-ratatouille\\B-ratatouille-large.in", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    n, p = [int(i) for i in a]

    strLine = ff.readline()
    a = strLine.split(" ")
    r = [int(i) for i in a]

    q=[]
    for i in range(n):
        q.append([])
        strLine = ff.readline()
        a = strLine.split(" ")
        q[i] = sorted([int(i) for i in a])

    going = True
    serving = 1
    cnt = 0
    while going:
        for i in range(n):
            while is_proper(q[i][0], i, serving) == -1:
                q[i].pop(0)
                if len(q[i]) == 0:
                    going = False
                    break
            if going and is_proper(q[i][0], i, serving) == -2:
                serving += 1
                break
            if not going:
                break
        else:
            cnt += 1
            if going:
                for i in range(n):
                    q[i].pop(0)
                    if len(q[i]) == 0:
                        going = False

    print(cnt)
