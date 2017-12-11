__author__ = 'Mahnaz'

##################################################################################################################
# Python Operator Precedence: "http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html"
#
# Function:
# Given a string containing an expression, return the expression with unnecessary parentheses removed.
#
# Assumptions:
# 1. All the input expressions are valid.
# 2. The valid operators are {**, +, -, *, /, +, -}.
# 3. "+" and "-" can be binary or unary. While the unary cases are second in precedence list,
#    the binary ones are the last in the list.
# 4. The precedence list for the operators is: {{**}, {+, -}, {*, /}, {+, -}}. Operators grouped in the same internal
#    set have the same precedence ranking.
#
# Pre-processing:
# 1. All the spaces in the expressions are removed beforehand.
# 2. A dictionary of valid operations along with their rank and a flag for their associativity ability
#    needs to be created.
##################################################################################################################


#####################  unittest definition  ######################################################################
import unittest


class TestParenthesesRemoval(unittest.TestCase):
    def test_recursion(self):
        self.assertEqual(rm_p("(1+(1+(1+(1+1))))"), "1+1+1+1+1")

    def test_precedence_no_associative(self):
        self.assertEqual(rm_p("(2+(3+3+(4+4)+(5+5-(6+6)+7)))"), "2+3+3+4+4+5+5-(6+6)+7")

    def test_recursion_associative(self):
        self.assertEqual(rm_p("(2+(3+4*(5*6)))"), "2+3+4*5*6")

    def test_recursion_associative2(self):
        self.assertEqual(rm_p("7*(2+(3+3))*9"), "7*(2+3+3)*9")

    def test_recursion_associative3(self):
        self.assertEqual(rm_p("7*(2+(3+3))**9"), "7*(2+3+3)**9")

    def test_recursion_associative4(self):
        self.assertEqual(rm_p("7*(2+(3+3))"), "7*(2+3+3)")

    def test_recursion_associative5(self):
        self.assertEqual(rm_p("(1*(2+(3+3)))/(4+5)"), "1*(2+3+3)/(4+5)")

    def test_recursion_not_associative(self):
        self.assertEqual(rm_p("(2+(3+4/(5*6)))"), "2+3+4/(5*6)")

    def test_recursion_not_associative2(self):
        self.assertEqual(rm_p("(2+(3+4/(5*6*(2**3))))"), "2+3+4/(5*6*2**3)")

    def test_recursion_not_associative3(self):
        self.assertEqual(rm_p("2+(2-2)+(3+3)-2"), "2+2-2+3+3-2")

    def test_recursion_not_associative4(self):
        self.assertEqual(rm_p("(1+1-(1+1))+1-(1+1)"), "1+1-(1+1)+1-(1+1)")

    def test_recursion_not_associative5(self):
        self.assertEqual(rm_p("1+(2-(3*(2**2)))"), "1+2-3*2**2")

    def test_var(self):
        self.assertEqual(rm_p("x+(y+z)+(t+(v+w))"), "x+y+z+t+v+w")

    def test_recursion_precedence(self):
        self.assertEqual(rm_p("1*(2+(3*(4+5)))"), "1*(2+3*(4+5))")

    def test_unary(self):
        self.assertEqual(rm_p("2+(3/-5)"), "2+3/-5")

    def test_unary2(self):
        self.assertEqual(rm_p("2+(3/(-5))"), "2+3/-5")

    def test_unary3(self):
        self.assertEqual(rm_p("2 + 3 / -5"), "2+3/-5")

    def test_lro1(self):
        self.assertEqual(find_lro("2**2"), "**")

    def test_lro2(self):
        self.assertEqual(find_lro("2*2**2"), "*")

    def test_lro3(self):
        self.assertEqual(find_lro("2*2**2-1"), "-")

#####################  initialization   #########################################################################

# replace unnecessary "(" and ")" with this character
r_p_w = " "

# "operand": (precedence_rank, associativity)
oprt_prcd = {"**": (2, 1), "+u": (3, 0), "-u": (3, 0),  "*": (5, 1), "/": (5, 0), "+": (7, 1),
             "-": (7, 0), "dig": (9, ''), "var": (10, ''), "": (0, 1)}

# set of valid operators
oprt = {"+", "-", "*", "/", "**"}

#####################  module definition   #######################################################################
def matched_close_p(s, l):
    # This method finds the matched ) for the current (. In other words, it skips the nested parentheses.
    # l : the location of open parenthesis
    p_lst = ["("]
    s_loc = l + 1
    while p_lst:
        if s[s_loc] == "(":
            p_lst.append("(")
        elif s[s_loc] == ")":
            p_lst.pop()
        s_loc += 1
    return s_loc - 1


def find_lro(s):
    # find the lowest-rank-operator in the string. This parameter will be used in order to recognize
    # the unnecessary parentheses.
    lro = ""
    i = 0
    while i < len(s):

        if s[i] == "(":
            # ignore inside parentheses
            i = matched_close_p(s, i)
        elif s[i:i+2] in oprt_prcd:
            # check for the double character operators
            if oprt_prcd[s[i:i+2]][0] > oprt_prcd[lro][0]:
                lro = s[i:i+2]
            i += 1
        elif (s[i] in oprt_prcd and s[i-1] in oprt_prcd) or (i==0 and s[i] in oprt_prcd):
            # check for unary operands. Note that double character operators has been checked already.
            if oprt_prcd[''.join([s[i], "u"])][0] > oprt_prcd[lro][0]:
                lro = ''.join([s[i], "u"])
        elif s[i] in oprt_prcd:
            # check for single character binary operators
            if oprt_prcd[s[i]][0] > oprt_prcd[lro][0]:
                lro = s[i]
        i += 1
    return lro


def find_op(s, d):
    # match the operator among valid list
    # d specifies if the operator is in left sid(1) or in right side(0) of the parentheses
    if s in oprt:
        return s
    elif s[d] in oprt:
        return s[d]
    else:
        return ''


def replace_p(s):
    # !!! IMPROVE IT! Avoid processing similar expressions repeatedly! Keep track of processed expressions and
    # the suitable replacement for them. replace all the numbers and variables with one constant token, process,
    # convert to original tokens!

    # initial what this method will return
    return_string = s.replace(" ", "")

    # main loop which goes through each pair of parentheses at this level.
    # In other word, it does not care about the nested parentheses.

    # initialize the location of "(" under process
    open_p_idx = 0

    # initialize the progress point in processing the string s.
    s_loc = 0

    # initialize the internal operator with empty string.
    i_op = ""

    while open_p_idx >= 0 and s_loc < len(s):
        open_p_idx = s.find("(", s_loc)   # finds the next (
        if open_p_idx >= 0:
            close_p_idx = matched_close_p(s, open_p_idx)

            # recursion here in order to process the nested parentheses.

            internal_returning_string, i_op = replace_p(s[open_p_idx+1:close_p_idx])

            return_string = return_string[:open_p_idx + 1] + internal_returning_string + return_string[close_p_idx:]

            # find the operators around ()
            if open_p_idx > 1:
                # check for operators specified with 2 characters like "**"
                l_op = find_op(s[open_p_idx - 2:open_p_idx], 1)
            elif open_p_idx > 0:
                l_op = find_op(s[open_p_idx - 1], 0)
            else:
                l_op = ""

            if close_p_idx < len(s) - 2:
                # check for operators specified with 2 characters like "**"
                r_op = find_op(s[close_p_idx + 1: close_p_idx + 3], 0)
            elif close_p_idx < len(s) - 1:
                r_op = find_op(s[close_p_idx + 1], 0)
            else:
                r_op = ""

            # REPLACE unnecessary "()" WITH SPACES  when they need to be removed. We don't want to change the length
            # of the string at this stage.

            if l_op == r_op == "":
                # there is no operator around the () then remove them
                return_string = return_string[:open_p_idx] + r_p_w + internal_returning_string + r_p_w + return_string[close_p_idx + 1:]
                i_op = find_lro(return_string)
            elif l_op == "":
                # there is only operator on right side of ()
                if oprt_prcd[i_op][0] <= oprt_prcd[r_op][0]:
                    return_string = return_string[:open_p_idx] + r_p_w + internal_returning_string + r_p_w + return_string[close_p_idx + 1:]
                i_op = find_lro(return_string)
            elif r_op == "":
                #  there is only operator on left side of ()
                if (oprt_prcd[l_op][0] > oprt_prcd[i_op][0]) or (oprt_prcd[l_op][0] == oprt_prcd[i_op][0] and oprt_prcd[l_op][1]):
                    return_string = return_string[:open_p_idx] + r_p_w + internal_returning_string + r_p_w + return_string[close_p_idx + 1:]
                i_op = find_lro(return_string)
            else:
                # there are operators on both sides of ()
                if l_op == i_op == r_op:
                    if oprt_prcd[l_op][1]:
                        return_string = return_string[:open_p_idx] + r_p_w + internal_returning_string + r_p_w + return_string[close_p_idx + 1:]
                elif oprt_prcd[l_op][0] < oprt_prcd[i_op][0] < oprt_prcd[r_op][0]:
                    return_string = return_string[:open_p_idx] + r_p_w + internal_returning_string + r_p_w + return_string[close_p_idx + 1:]
                elif oprt_prcd[l_op][0] == oprt_prcd[i_op][0] == oprt_prcd[r_op][0] and oprt_prcd[l_op][1]:
                    return_string = return_string[:open_p_idx] + r_p_w + internal_returning_string + r_p_w + return_string[close_p_idx + 1:]

                i_op = find_lro(return_string)

            s_loc = close_p_idx + 2

        else:
            # base case: there is no () in the string.

            # find the lowest-rank-op in the string
            i_op = find_lro(return_string)

    return return_string, i_op


def rm_rpw(s):
    # remove all the r_p_w characters, spaces in this case, at the end!
    return s.replace(r_p_w, "")


def rm_p(s):
    s1, o1 = replace_p(s)
    return rm_rpw(s1)


#####################   main module      #######################################################################
if __name__ == '__main__':
    unittest.main()


