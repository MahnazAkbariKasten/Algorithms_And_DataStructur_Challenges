__author__ = 'pretymoon'


def addStrings(num1, num2):
    if len(num1) >= len(num2):
        n1 = num1
        n2 = num2
    else:
        n1 = num2
        n2 = num1

    tmp = 0
    digit_sum = 0
    n = []
    b = False

    for i in range(len(n2)):
        digit_sum = tmp + int(n1[len(n1)-i-1]) + int(n2[len(n2)-i-1])
        tmp = digit_sum // 10
        n[:0] = str(digit_sum % 10)

    for i in range(len(n2), len(n1)):
        digit_sum = tmp + int(n1[len(n1)-i-1])
        tmp = digit_sum // 10
        n[:0] = str(digit_sum % 10)

    if tmp > 0:
        n[:0] = str(tmp)

    return "".join(n)

print(addStrings("0", "0"))