__author__ = 'pretymoon'
def get_digits(myNumber):
    length = len(str(myNumber))
    digits = []
    fold = length - 1
    for i in range(length):
        tmp = myNumber // (10 ** fold)
        digits.append(tmp)
        myNumber %= 10 ** fold
        fold -= 1
    return digits

def digits_to_number(myDigits):
    tmp = 0
    length = len(myDigits)
    for fold in range(length):
        tmp += myDigits[fold] * (10 ** (length-1-fold))
    return tmp

def is_tidy(myNumber):
    digits = get_digits(myNumber)
    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
    else:
        return True

###############################################
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_qualification\\problem_2\\problem_2_small.in", "r")
# numOfCases = int(ff.readline())
# for i in range(1, numOfCases+1):
#     print("Case #{}: ".format(i), end='')
#     strLine = ff.readline()

###############################################
numOfCases = int(input())
for i in range(1, numOfCases+1):
    print("Case #{}: ".format(i), end='')
    strLine = input()

###############################################
    a = strLine.split(" ")
    n = int(a[0])

    if is_tidy(n):
        print(n)
    else:
        digits = get_digits(n)
        tidy = []
        flag = False
        for idx in range(len(digits)):
            if not flag:
                if digits[idx] <= digits[idx+1]:
                    tidy.append(digits[idx])
                else:
                    if idx == 0:
                        tidy.append(digits[0]-1)
                    elif idx>0 and digits[idx]-1 >= digits[idx-1]:
                        tidy.append(digits[idx]-1)
                    else:
                        tidy.append(9)
                        tidy[idx-1] -= 1
                        for repel in range(idx-1, 0, -1):
                            if tidy[repel] < tidy[repel-1]:
                                tidy[repel] = 9
                                tidy[repel-1] -= 1
                    flag = True
            else:
                tidy.append(9)

        print(digits_to_number(tidy))






    # print(n)
    # print(get_digits(n))
    # print(is_tidy(10))
    # print(digits_to_number(get_digits(n)))
