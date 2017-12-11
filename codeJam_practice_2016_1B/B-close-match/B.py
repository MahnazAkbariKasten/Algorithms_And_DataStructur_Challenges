__author__ = 'pretymoon'


def fill_rest(s1, s2, idx):  # when you face the first different digits, you know which score is larger
                            # and can fill the rest of positions
    while idx < len(s1):
        if s1[idx] == "?":
            s1[idx] = "0"
        if s2[idx] == "?":
            s2[idx] = "9"
        idx += 1


def solve(s1, s2):
    i = 0
    while i < len(s1) and s1[i] == s2[i] and s1[i] != "?":  # just ignore the positions that are similarly filled
    # in the left side
        i += 1
    if i == len(s1):  # if both scores are the same, return them
        return s1, s2

    if s1[i] == s2[i] == "?":
        while i+1 < len(s1) and s1[i+1] == s2[i+1] == "?":  # only one set of ? in left side matters,
        # fill rest of them with 0's
            i += 1
            s1[i-1] = s2[i-1] = "0"

        # try 3 possible filling and compare the result
        c1 = s1.copy()
        j1 = s2.copy()
        c1[i] = j1[i] = "0"
        c1, j1 = solve(c1, j1)
        res1 = abs(convert_to_digits(c1) - convert_to_digits(j1))

        c2 = s1.copy()
        j2 = s2.copy()
        c2[i] = "0"
        j2[i] = "1"
        fill_rest(j2, c2, i+1)
        res2 = abs(convert_to_digits(c2) - convert_to_digits(j2))

        c3 = s1.copy()
        j3 = s2.copy()
        c3[i] = "1"
        j3[i] = "0"
        fill_rest(c3, j3, i+1)
        res3 = abs(convert_to_digits(c3) - convert_to_digits(j3))

        res = min((res1, c1, j1), (res2, c2, j2), (res3, c3, j3))
        return res[1], res[2]

    elif s1[i] == "?" and s2[i] != "?":
        res2 = res3 = float("inf")
        c1 = s1.copy()
        j1 = s2.copy()
        c2 = s1.copy()
        j2 = s2.copy()
        c3 = s1.copy()
        j3 = s2.copy()
        c1[i] = j1[i]
        c1, j1 = solve(c1, j1)
        res1 = abs(convert_to_digits(c1) - convert_to_digits(j1))

        if s2[i] > "1":
            c2[i] = str(int(j2[i]) - 1)
            fill_rest(j2, c2, i+1)
            res2 = abs(convert_to_digits(c2) - convert_to_digits(j2))

        if s2[i] < "9":
            c3[i] = str(int(j3[i]) + 1)
            fill_rest(c3, j3, i+1)
            res3 = abs(convert_to_digits(c3) - convert_to_digits(j3))

        res = min((res1, c1, j1), (res2, c2, j2), (res3, c3, j3))
        return res[1], res[2]

    elif s2[i] == "?":
        res2 = res3 = float("inf")
        c1 = s1.copy()
        j1 = s2.copy()
        c2 = s1.copy()
        j2 = s2.copy()
        c3 = s1.copy()
        j3 = s2.copy()
        j1[i] = c1[i]
        c1, j1 = solve(c1, j1)
        res1 = abs(convert_to_digits(c1) - convert_to_digits(j1))

        if s1[i] > "1":
            j2[i] = str(int(c2[i]) - 1)
            fill_rest(c2, j2, i+1)
            res2 = abs(convert_to_digits(c2) - convert_to_digits(j2))
        if s1[i] < "9":
            j3[i] = str(int(c3[i]) + 1)
            fill_rest(j3, c3, i+1)
            res3 = abs(convert_to_digits(c3) - convert_to_digits(j3))

        res = min((res1, c1, j1), (res2, c2, j2), (res3, c3, j3))
        return res[1], res[2]

    elif s1[i] != s2[i]:
        if s1[i] > s2[i]:
            fill_rest(s1, s2, i+1)
        else:
            fill_rest(s2, s1, i+1)
        return s1, s2

def convert_to_digits(s1):
    myString = ''
    for m in range(len(s1)):
        myString += s1[m]
    return int(myString)


ff = open("\\Mahnaz\\PycharmProjects\\codeJam_practice_2016_1B\\B-close-match\\B-small.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    c = [a[0][i:i+1] for i in range(len(a[0].strip()))]
    j = [a[1][i:i+1] for i in range(len(a[1].strip()))]

    # print(c, j, end='')

    c, j = solve(c, j)
    for m in range(len(c)):
        print(c[m],end='')

    print(" ", end='')
    for m in range(len(c)):
        print(j[m], end='')
    print()
