__author__ = 'pretymoon'


def rec_test(s1):
    if len(s1) < 4:
        s1 = s1 + s1
        return rec_test(s1)
    else:
        return s1

s="ko"
# print(rec_test(s), s)

# if s[0:1] == "o":
#     print("o")
# elif s[1:2] == "k":
#     print("k")
# else:
#     print("ok")

# def convert_to_digits(s1):
#     myString = ''
#     for m in range(len(s1)):
#         myString += s1[m]
#     return int(myString)
#
# s = ["1", "2", "3"]
# print(convert_to_digits(s))

print(min(("2","2"), ("1","3"), ("2","3")))
