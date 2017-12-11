__author__ = 'pretymoon'

# a = [10, 20, 30]
# for idx, val in enumerate(a):
#     print(idx, val)
#     print(frozenset([0, idx+1]))
#     print("---")
table = []
def recur(i):
    if i == 0:
        table.append([0, 0])
    else:
        table.append([i, i])
        recur(i-1)

recur(3)
print(table)