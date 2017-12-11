__author__ = 'pretymoon'

f = open(r'input.txt', 'r')
strLine = f.readline().strip()

case = 1
result = True
while strLine != "":
    print("Case #{}: ".format(case),end='')
    for i in range(len(strLine)//2):
        if strLine[i] != strLine[len(strLine)-1-i]:
            result = False
            break
    print(result)
    strLine = f.readline().strip()
    case += 1
