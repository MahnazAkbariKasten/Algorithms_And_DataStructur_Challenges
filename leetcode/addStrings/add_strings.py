__author__ = 'pretymoon'

"""
ACCEPTED
"""
def addStrings(num1, num2):
    if len(num1) >= len(num2):
        n1 = list(num1)
        n2 = list(num2)
    else:
        n1 = list(num2)
        n2 = list(num1)

    n1.reverse()
    n2.reverse()
    l1 = len(n1)
    l2 = len(n2)
    n = 0
    tmp = 0
    digit_sum = 0
    num_of_dig = 0

    for i in range(l2):
        digit_sum = tmp + int(n1[i]) + int(n2[i])
        tmp = digit_sum // 10
        n += (digit_sum % 10) * (10 ** i)
        num_of_dig += 1

    for j in range(l2, l1):
        digit_sum = tmp + int(n1[j])
        tmp = digit_sum // 10
        n += (digit_sum % 10) * (10 ** j)
        num_of_dig += 1

    if tmp > 0:
        n += tmp * (10 ** num_of_dig)

    return str(n)

print(addStrings("123", "345"))
print(addStrings("1123", "345"))
print(addStrings("123", "2345"))
print(addStrings("1", "9"))
print(addStrings("1", "19"))
print(addStrings("21", "9"))
print(addStrings("0", "0"))