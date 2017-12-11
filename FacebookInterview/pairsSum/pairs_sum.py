__author__ = 'pretymoon'
# http://codercareer.blogspot.com/p/facebook-interview-questions.html
# this function can consider an item more than once!!! WRONG
# def pairs_sum(my_list, my_sum):
#     for i in range(len(my_list)):
#         tmp = -1
#         if (my_sum - my_list[i]) in my_list:
#             tmp = my_list.index(my_sum - my_list[i])
#             return my_list[i], my_list[tmp]
#     return []

def pairs_sum2(my_list, my_sum):
    smaller = 0
    larger = len(my_list) - 1
    while smaller < len(my_list) and larger >= 0 and smaller != larger:
        if my_list[smaller] + my_list[larger] == my_sum:
            return [my_list[smaller], my_list[larger]]
        elif my_list[smaller] + my_list[larger] < my_sum:
            smaller += 1
        else:
            larger -= 1

    return []


def three_sum_0(my_list):
    my_list.sort()
    for i in range(len(my_list)):
        tmp = my_list.copy()
        tmp.remove(my_list[i])
        result = pairs_sum2(tmp, -1 * my_list[i])
        if len(result) > 0:
            result.extend([my_list[i]])
            return result
    return []

############# pair summed to s
l = [-1, 1]
s = 2
result = pairs_sum2(l, s)

if len(result) < 2:
    print("No pair found summing to {0}".format(s))
else:
    print("{0} + {1} = {2}".format(result[0], result[1], s))


############# three sum to zero
l = [1, -3, 5]
result = three_sum_0(l)
if len(result) < 2:
    print("No three elements found summing to {0}".format(0))
else:
    print("{0} + {1} + {2} = {3}".format(result[0], result[1], result[2], 0))
