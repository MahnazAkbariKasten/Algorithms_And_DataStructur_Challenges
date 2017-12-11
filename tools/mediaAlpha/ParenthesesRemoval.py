__author__ = 'Mahnaz'

import re

oprt_prcd = {"()": 0, "**": 1, "+u": 2, "-u": 2,  "*": 3, "/": 3, "+": 4, "-": 4, "dig": 5, "var": 5, "null": 6}


def chk_p_pairs(s):
    # ??? check for pairs of parentheses. If not paired return error.
    if s[0] == ")":
        return "error"

    p_stack = []
    for l in s:
        if l == "(":
            p_stack.append("(")
    return "passed"


def rm_outer_p(s):
    # remove outer parentheses
    new_string = s
    while new_string[0] == "(" and new_string[-1] == ")":
        new_string = new_string[1:-1]
    return new_string


def rm_p(s, l_opt, r_opt):
    # ??? pass the string inside the () and the highest rank among the operand immediate to the ().
    # ??!! For first time, pass the whole string with l_op and r_op set to NULL
    # ??? use recursive to solve this problem

    # s = rm_outer_p(s)
    new_s = rm_outer_p(s)
    inner_rank = 5
    for i in range(len(new_s)):
        # scan string to find (
        opening_p = s.find("(")
        if opening_p < 0:
            inner_opt = find_lowest_rank(new_s)
            return [new_s, inner_opt]
        else:
            # find the matched ) for this ( and call rm_p for whatever in between
            closing_p = find_matched_closing(new_s[opening_p:])

            # if opening_p == 0:
            #     outer_rank = oprt_prcd[new_s(closing_p + 1)]
            # elif closing_p == len(new_s) - 1:
            #     outer_rank = oprt_prcd[new_s(opening_p - 1)]
            # else:
            #     outer_rank = max(oprt_prcd[new_s(closing_p + 1)], oprt_prcd[new_s(opening_p - 1)])

            new_s = rm_p(s[opening_p + 1, closing_p], outer_rank)

    return [new_s]


def tokenize_str(s):
    op_lst = ["*", "/", "-", "+"]
    return

def find_matched_closing(s):
    #find the ) for the current (



def find_match_p(s):
    # build a dictionary of the location of matched parentheses in the string s
    p_loc_dic = dict()
    p_loc_lst = []   # use as stack
    for i in range(len(s)):
        if s[i] == "(":
            p_loc_lst.append(i)
        elif s[i] == ")":
            p_loc_dic[p_loc_lst.pop()] = i
    return p_loc_dic

my_string = "(((7-5))*2)"

new_string = rm_outer_p(my_string)
# print(new_string)
#
# print(find_match_p(my_string).items())

# print(u"5.0".isnumeric(), u"5.0".isdecimal(), "51".isdigit())
#
# print(re.split('\**|\*|\+|\-', "I*love-Amber**so"))

print("a+(5)".index("("))




