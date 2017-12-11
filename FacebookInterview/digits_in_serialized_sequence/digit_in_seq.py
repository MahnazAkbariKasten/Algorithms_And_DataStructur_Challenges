__author__ = 'pretymoon'
# http://codercareer.blogspot.com/2013/02/no-38-digits-in-sequence.html


def digit_in_pos(pos):
    if pos < 10:
        return pos
    elif 10 <= pos < 190:
        pos_in_2dg = pos - 10
        # d_1 = pos_in_2dg % 2
        d_2 = pos_in_2dg // 2
        number = 10 + d_2
        if (pos_in_2dg % 2) == 0:
            return number // 10
        else:
            return number % 10
    elif 190 <= pos < 2890:
        pos_in_3dg = pos - 10 - 180
        d_2 = pos_in_3dg // 3
        number = 100 + d_2
        print("number: ", number)
        dig_in_num = pos_in_3dg % 3
        return str(number)[dig_in_num]



print(digit_in_pos(490))

# print first 200 elements of such array: position digit number
# cnt = 0
# for i in range(200):
#     for j in range(len(str(i))):
#         print(cnt, ' ', str(i)[j], ' ', i)
#         cnt += 1