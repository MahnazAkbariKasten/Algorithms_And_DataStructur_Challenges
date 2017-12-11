__author__ = 'pretymoon'

def valid_distance(m1, m2, k=200):
    if abs(m1-m2) >= k:
        return True
    else:
        return False

mile = [0, 50, 150, 250, 300, 370, 500, 550]
expected_profit = [0, 2, 3, 2, 5, 4, 2, 4]
# mile = [0, 50, 150, 250]
# expected_profit = [0, 2, 3, 2]
max_profit = [0 for i in range(len(mile))]
prev = [-1]

# for the max profit at this point, there will be a restaurant at this location or not
flag = [0 for i in range(len(mile))]

for j in range(1, len(mile)):  # for each location from the beginning

    # initialize with the case that there is no restaurant along the road before the current location
    prev.append(0)
    max_profit[j] = expected_profit[j]
    flag[j] = 1

    for i in range(1, j):   # for all the locations previous to the current one
        if valid_distance(mile[j], mile[i]):    # if its distance from current location is valid, there can be
                                                # restaurants in both locations.
            if max_profit[i] + expected_profit[j] > max_profit[j]:
                max_profit[j] = max_profit[i] + expected_profit[j]
                if flag[i] == 1:
                    prev[j] = i
                else:
                    prev[j] = prev[i]
                flag[j] = 1
        else:   # otherwise, we have choose between two locations based on their max profit
            if max_profit[i] > max_profit[j]:
                max_profit[j] = max_profit[i]
                if flag[i] == 1:
                    prev[j] = i
                else:
                    prev[j] = prev[i]
                flag[j] = 0

print("max_profit: ", max_profit[-1])
i = len(mile) - 1
while prev[i] > -1:
    if flag[i] == 1:
        print(mile[i], " ", end='')
        i = prev[i]
print()

# print("-"*20)
# print("mile: ", mile)
# print("expected_profit: ", expected_profit)
# print("max_profit: ", max_profit)
# print("prev: ", prev)
# print("flag: ", flag)