__author__ = 'pretymoon'


def magic_numbers(start, numbers, n):
    cnt = 0
    cur = start

    magic_num_lst = []

    k = 0  # size of the magic number list

    for i in range(cur):
        if k < n:
            magic_num_lst.append(cur)
        k += 1
    idx = 1

    if len(magic_num_lst) == 1:
        nex = numbers - {magic_num_lst[-1]}
        cur = list(nex)[0]

        for i in range(cur):
            if k < n:
                magic_num_lst.append(cur)
            k += 1
        idx = 2

    while k < n:
        nex = numbers - {magic_num_lst[-1]}
        cur = list(nex)[0]

        for i in range(magic_num_lst[idx]):
            if k < n:
                magic_num_lst.append(cur)
                # print(cur)
            k += 1
        idx += 1

    return magic_num_lst, cnt

my_list, my_cnt = magic_numbers(1, {1, 2}, 416)
# print(my_list[:11])
# print(''.join([str(x) for x in my_list]).index(''.join([str(x) for x in my_list[:7]]),16))

print("count of pattern1: ", ''.join([str(x) for x in my_list]).count(''.join([str(x) for x in my_list[:7]])))
# print(sum([x for x in my_list[:55] if x==1]))
# print(sum([x for x in my_list[55:110] if x==1]))
# print(sum([x for x in my_list[108:16] if x==1]))
# print(sum([x for x in my_list[162:216] if x==1]))
print(my_list[:54])
print(my_list[54:108])
print(my_list[108:163])
print(my_list[163:216])
# print(magic_numbers(1, {1, 2}, 54))
# print(magic_numbers(2, {1, 2}, 20))
shadow_list1 = [0 for x in my_list]
shadow_list2 = shadow_list1[:]
idx = 0
my_string = ''.join([str(x) for x in my_list])
my_pattern = ''.join([str(x) for x in my_list[:7]])
print("pattern1: ", my_list[:7])
occur = 0
while idx < len(my_list):
    occur = my_string.find(my_pattern, idx)
    if occur >= 0:
        shadow_list1[occur:occur+7] = [8]*7
        # print(occur, idx)
        # print(my_list[idx:occur])
        idx = occur + 7
    else:
        break

print(shadow_list1)
print(my_list)

my_pattern2 = ''.join([str(x) for x in [2, 2, 1, 2, 1, 1, 2]])
idx = 0
while idx < len(my_list):
    occur = my_string.find(my_pattern2, idx)
    if occur >= 0:
        shadow_list2[occur:occur+7] = [8]*7
        # print(occur, idx)
        # print(my_list[idx:occur])
        idx = occur + 7
    else:
        break

print(shadow_list2)

residual_list = []

for i in range(len(my_list)):
    if shadow_list1[i] != 8 and shadow_list2[i] != 8:
        residual_list.append(my_list[i])

print()
print(residual_list)
print("count of pattern2: ", ''.join([str(x) for x in my_list]).count(''.join([str(x) for x in [2, 2, 1, 2, 1, 1, 2]])))
print("len of residuals: ", len(residual_list))
print("count 1's residuals: ", ''.join([str(x) for x in residual_list]).count('1'))