__author__ = 'pretymoon'

s = [5, 15, -30, 10, -5, 40, 10, -10]
# s = [5, 15, -30, 20]
cur_sum = s[0]
max_sum = s[0]
cur_beg = 0
max_beg = 0
max_end = 0

for j in range(1, len(s)):
    if s[j] > s[j] + cur_sum:
        cur_sum = s[j]
        cur_beg = j
    else:
        cur_sum += s[j]

    if cur_sum >= max_sum:
        max_sum = cur_sum
        max_beg = cur_beg
        max_end = j

print("max_sum: ", max_sum)
print("max_beg: ", max_beg)
print(s[max_beg:max_end + 1])

