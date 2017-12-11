__author__ = 'pretymoon'

f = open(r'input.txt')
strLine = f.readline().strip()

s = []
result = True
case = 1

while strLine != "":
    print("Case #{}: ".format(case), end='')
    for i in range(len(strLine)):
        if strLine[i] in "[{(<":
            s.append(strLine[i])
        elif strLine[i] == "]":
            if len(s) > 0 and s[-1] == "[":
                s.pop()
            else:
                result = False
                break
        elif strLine[i] == ")":
            if len(s) > 0 and s[-1] == "(":
                s.pop()
            else:
                result = False
                break
        elif strLine[i] == "}":
            if len(s) > 0 and s[-1] == "{":
                s.pop()
            else:
                result = False
                break
        elif strLine[i] == ">":
            if len(s) > 0 and s[-1] == "<":
                s.pop()
            else:
                result = False
                break
    if len(s) > 0:
        result = False
    print(result)
    case += 1
    strLine = f.readline().strip()

