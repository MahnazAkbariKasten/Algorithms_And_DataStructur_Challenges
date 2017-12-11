__author__ = 'pretymoon'
def second_largest(l):
    max1 = max(l[0], l[1])
    max2 = min(l[0], l[1])

    for i in range(2, len(l)):
        if l[i] >= max1:
            max2 = max1
            max1 = l[i]

    return max2

f = open("input.txt", 'r')
numberOfCases = int(f.readline().strip())
strLine = f.readline().strip()
case = 1
while case <= numberOfCases:
    print("Case #{}: ".format(case), end='')
    if strLine == "" or len([int(x) for x in strLine.split(' ')]) < 2:
        print("second largest element is {}.".format("None!"))
        strLine = f.readline().strip()
        case += 1
        continue

    second_max = second_largest([int(x) for x in strLine.split(' ')])
    ###
    print("second largest element is {}.".format(second_max))
    strLine = f.readline().strip()
    case += 1
    ###
