__author__ = 'pretymoon'
def max_in_win(my_list, k):
    result = []
    for i in range(len(my_list) - k + 1):
        result.append(max([x for x in my_list[i:i+k]]))
    return result

l = [2, 3, 4, 2, 6, 2, 5, 10]
print(max_in_win(l, 4))
