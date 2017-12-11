__author__ = 'pretymoon'
################################
# NOT CORRECT!!!
###############################
ff = open("\\Mahnaz\\PycharmProjects\\codeJam_practice_2016_1B\\B-close-match\\B-close-match-small.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    c = [a[0][i:i+1] for i in range(len(a[0].strip()))]
    j = [a[1][i:i+1] for i in range(len(a[1].strip()))]
    print(c, j, end='')

    i=0
    while i< len(c) and c[i]==j[i]=="?":
        c[i]=j[i]="0"
        i += 1

    for k in range(i, len(c)):
        if c[k]==j[k]=="?":
            if str(c[:k]) == str(j[:k]):
                c[k]=j[k]=0
            elif str(c[:k]) > str(j[:k]):
                c[k]="0"
                j[k]="9"
            else:
                c[k]="9"
                j[k]="0"
        elif c[k]=="?":
            if str(c[:k]) == str(j[:k]):
                c[k]= j[k]
            elif str(c[:k]) > str(j[:k]):
                c[k]="0"
            else:
                c[k]="9"
        elif j[k]=="?":
            if str(c[:k]) == str(j[:k]):
                j[k]=c[k]
            elif str(c[:k]) > str(j[:k]):
                j[k]="9"
            else:
                j[k]="0"

    for m in range(len(c)):
        print(c[m],end='')

    print(" ", end='')
    for m in range(len(c)):
        print(j[m], end='')
    print()