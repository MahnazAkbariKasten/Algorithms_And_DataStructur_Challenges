__author__ = 'pretymoon'


# this function eliminate duplication of letters
def perm_func(myInput):
    if len(myInput) == 1:
        return list(myInput)
    else:
        myInput_set = set(myInput)
        result = []
        for x in myInput:
            tmp = myInput_set - {x}
            result.extend([x+y for y in perm_func(tmp)])
        return result


# this function treats repeated letters as individuals
def perm_func2(myInput):
    if len(myInput) == 1:
        return myInput
    else:
        result = []
        tmp = myInput[1:]
        prev_result = perm_func2(tmp)
        for x in prev_result:
            for i in range(len(x)+1):
                result.append(x[:i]+myInput[0]+x[i:])
        return result

print(list(set(perm_func('dod'))))
print(list(set(perm_func2('dod'))))
print(len(list(set(perm_func2('spam')))))