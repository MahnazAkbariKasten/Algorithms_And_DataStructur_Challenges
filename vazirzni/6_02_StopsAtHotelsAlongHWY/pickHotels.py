__author__ = 'pretymoon'

def penalty(x, p=200):
    return (200 - x) ** 2

# a = [0, 100, 290, 110, 410]     # hotels' miles from departure point: i<j => a[i] < a[j}
a = [0, 190, 410, 600]
prev = []     # keep track of the most efficient second to last stop for each hotel as destination
k = []        # keep track of the min penalty for each hotel as destination

# start process from the departure point

# initialize
k.append(0)
prev.append(-1)

for j in range(1, len(a)):
    k.append(penalty(a[j]))     # set to penalty for direct hop
    prev.append(0)

    # find penalty for other routs, through second last stop
    for i in range(1, j):
        if k[i] + penalty(a[j] - a[i]) < k[j]:
            prev[j] = i
            k[j] = k[i] + penalty(a[j] - a[i])

# print the path with minimum penalty
i = len(a) - 1
print(i, end='')
i = prev[i]
while i != -1:
    print(" -", i, end='')
    i = prev[i]
print("")


print(k)
print(prev)