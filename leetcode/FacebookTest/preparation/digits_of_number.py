__author__ = 'pretymoon'


def write_digits(num):
    num_in_str_list = [int(x) for x in list(str(num))]
    return num_in_str_list


def cum_sum(input_list):
    total = 0
    cum_list = []
    for i in range(len(input_list)):
        total += input_list[i]
        cum_list.append(total)

    return cum_list


def odd_mem(input_list):
    odd_list = []
    if len(input_list) > 1:
        for i in range(1, len(input_list), 2):
            odd_list.append(input_list[i])

    return odd_list

def most_freq(input_list):
    my_dic = {}
    for i in input_list:
        if input_list[i] in my_dic.keys():
            my_dic[input_list[i]] += 1
        else:
            my_dic[input_list[i]] = 1
    # tmp_list = [(k, v) for k, v in my_dic.items()]
    popularity = 0
    pop_item = None
    for k, v in my_dic.items():
        if v > popularity:
            pop_item, popularity = k, v

    return pop_item

print(write_digits(123))
print(cum_sum([1,-1,1]))
print(odd_mem([1,2,3,4]))
print(max([1, 1, 1, 100]))
print(most_freq([1, 1, 1, 2, 2, 3]))