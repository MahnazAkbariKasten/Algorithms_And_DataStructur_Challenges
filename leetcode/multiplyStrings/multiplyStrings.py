__author__ = 'pretymoon'
import math


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


def multiply_1(num1, num2):
    # if len(num1) == len(num2) == 1:
    #     return int(num1) * int(num2)
    n = 0
    tmp = 0
    mul_dig = 0
    n2 = int(num2)
    for i in range(len(num1)):
        mul_dig = int(num1[len(num1) - i - 1]) * n2 + tmp
        tmp = mul_dig // 10
        n += (mul_dig % 10) * (10 ** i)
    if tmp > 0:
        n += tmp * (10 ** (len(num1)))
    return n


def multiply_str(num1, num2):
    if len(num1) == 1:
        return multiply_1(num2, num1)

    if len(num2) == 1:
        return multiply_1(num1, num2)

    num1_l = num1[:math.ceil(len(num1)/2)]
    num1_r = num1[math.ceil(len(num1)/2):]
    num2_l = num2[:math.ceil(len(num2)/2)]
    num2_r = num2[math.ceil(len(num2)/2):]

    if len(num1) == len(num2) and math.log(len(num1), 2) % 2 == 0:
        p1 = multiply_str(num1_l, num2_l)
        p2 = multiply_str(num1_r, num2_r)
        p3 = multiply_str(addStrings(num1_l, num1_r), addStrings(num2_l, num2_r))
        res = p1 * (10 ** len(num1)) + \
            (p3 - p1 - p2) * (10 ** math.ceil(len(num2)/2)) + p2
    else:
        p1 = multiply_str(num1_l, num2_l)
        p2 = multiply_str(num1_l, num2_r)
        p3 = multiply_str(num1_r, num2_l)
        p4 = multiply_str(num1_r, num2_r)
        res = p1 * (10 ** (len(num1) + len(num2) - math.ceil(len(num1)/2) - math.ceil(len(num2)/2))) + \
              p2 * (10 ** (len(num1) - math.ceil(len(num1)/2))) + \
              p3 * (10 ** (len(num2) - math.ceil(len(num2)/2))) + p4

    return res

def multiply(num1, num2):
    res = multiply_str(num1, num2)
    return str(res)

print(multiply("111", "2"), "expected: 222")
print(multiply("95", "2"), "expected: 190")
print(multiply("9", "9"), "expected: 81")
print(multiply("99", "9"), "expected: 891")
print(multiply("99", "0"), "expected: 0")
print(multiply("99", "1"), "expected: 99")
print(multiply("100", "100"), "expected: 10000")
print(multiply("1000", "10"), "expected: 10000")
print(multiply("11", "22"), "expected: 242")
print(multiply("123", "456"), "expected: 56088")
print(multiply("1111", "2222"), "expected: 2468642")
