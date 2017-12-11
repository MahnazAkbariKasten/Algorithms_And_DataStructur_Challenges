__author__ = 'pretymoon'

n = 5
k = 4
p = [.1, .2, .3, .4, .5]

table = []
for i in range(n):
    table.append([])
    if i < k:
        l = i + 1
    else:
        l = k
    for j in range(l):
        table[i].append(0)

table[0][0] = p[0]
for i in range(1, k):  # all (diagonal)
    table[i][i] = table[i-1][i-1] * p[i]

none = (1 - p[0])
for i in range(1, n):  # only one (first col)
    table[i][0] = table[i-1][0] * (1 - p[i]) + none * p[i]
    none *= 1 - p[i]

for i in range(1, n):
    if i <= k:
        l = i
    else:
        l = k
    for j in range(1, l):
        table[i][j] = table[i-1][j-1] * p[i] + table[i-1][j] * (1 - p[i])

print(table)
print(table[n-1][k-1])