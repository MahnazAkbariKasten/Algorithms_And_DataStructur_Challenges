__author__ = 'pretymoon'

elements = ["a", "b", "c"]
multiplication_table = [["b", "b", "a"], ["c", "b", "a"], ["a", "c", "c"]]
valid_set = {"a": [("a", "c"), ("b", "c"), ("c", "a")], "b": [("a", "a"), ("a", "b"), ("b", "b")],
             "c": [("b", "a"), ("c", "b"), ("c", "c")]}

# myString = "bbbbac"
myString = "cbabcbc"
# myString = "a"
myChar = "b"
dividing_points = {}

def results(symbols, char):
    if (symbols, char) in dividing_points:
        return True
    elif len(symbols) == 1:
        if symbols == char:
            return True
        else:
            return False
    elif len(symbols) == 2:
        idx1 = elements.index(symbols[0])
        idx2 = elements.index(symbols[1])
        if multiplication_table[idx1][idx2] == char:
            return True
        else:
            return False
    else:
        for valid_operands in valid_set[char]:
            for k in range(1, len(symbols)):
                if results(symbols[:k], valid_operands[0]) and results(symbols[k:], valid_operands[1]):
                    dividing_points[(symbols, char)] = (k, valid_operands[0], valid_operands[1])
                    return True
        return False

test = results(myString, myChar)
# print(test)

def parenthesize(this_string, char):
    if len(this_string) < 3:
        print(this_string,end='')
    else:
        k = dividing_points[(this_string, char)][0]
        c = dividing_points[(this_string, char)][1]
        if len(this_string[:k]) > 1:
            print("(", end='')
        parenthesize(this_string[:k], c)
        if len(this_string[:k]) > 1:
            print(")", end='')

        k = dividing_points[(this_string, char)][0]
        c = dividing_points[(this_string, char)][2]
        if len(this_string[k:]) > 1:
            print("(", end='')
        parenthesize(this_string[k:], c)
        if len(this_string[k:]) > 1:
            print(")", end='')
if test:
    print("Parenthesize '{0}' as below in order to get '{1}'".format(myString, myChar))
    parenthesize(myString, myChar)
else:
    print("There is no way to parenthesize '{0}' in order to get '{1}'".format(myString, myChar))


