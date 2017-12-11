__author__ = 'pretymoon'
#
# str = "{{()()()"
# s = []
# match = True
#
# for i in range(len(str)):
#     if str[i] in "([{<":
#         s.append(str[i])
#         # print("s: ", s)
#     elif str[i] in ")]}>":
#         if len(s) == 0:
#             match = False
#             break
#         else:
#             l = s.pop()
#         # print("l: ", l, str[i])
#         if l == "(":
#             if str[i] == ")":
#                 print(l, str[i])
#             else:
#                 match = False
#                 break
#         if l == "[":
#             if str[i] == "]":
#                 print(l, str[i])
#             else:
#                 match = False
#                 break
#         if l == "{":
#             if str[i] == "}":
#                 print(l, str[i])
#             else:
#                 match = False
#                 break
#         if l == "<":
#             if str[i] == ">":
#                 print(l, str[i])
#             else:
#                 match = False
#                 break
#
# if match and len(s) == 0:
#     print("pass")
# else:
#     print("fail")
#     print(s)


def hasBalancedBrackets(str):
    """check to see if the str has balanced brackets"""
    s = []

    for i in range(len(str)):

        if str[i] in "({[<":
            s.append(str[i])

        elif str[i] in ")}]>":
            if len(s) == 0:
                return 0
            else:
                l = s.pop()

            if l == "(" and str[i] == ")":
                continue
            elif l == "{" and str[i] == "}":
                continue
            elif l == "[" and str[i] == "]":
                continue
            elif l == "<" and str[i] == ">":
                continue
            else:
                return 0

    if len(s) == 0:
        return 1
    else:
        return 0

str = "[](){}<>]"
print(hasBalancedBrackets(str))