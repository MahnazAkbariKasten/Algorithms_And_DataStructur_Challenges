__author__ = 'pretymoon'
def print_tree(i, j):
    if i == j:
        print("M_{0}[{1}x{2}]".format(i, dim[i], dim[i+1]), end='')
    elif j == i + 1:
        print("( M_{0}[{1}x{2}] X M_{3}[{4}x{5}] )".format(i, dim[i], dim[i+1], j, dim[j], dim[j+1]), end='')
    else:
        print("( ", end='')
        print_tree(i, dividing_points[i][j])
        print(" X ", end='')
        print_tree(dividing_points[i][j]+1, j)
        print(" )", end='')


dim = [2, 5, 3, 1]
quantity = len(dim) - 1
table = [[float("inf") for i in range(quantity)] for j in range(quantity)]
dividing_points = [[-1 for i in range(quantity)] for j in range(quantity)]

for i in range(quantity):
    table[i][i] = 0

for i in range(quantity-1, -1, -1):
    for j in range(i+1, quantity):
        if j == i+1:
            table[i][j] = dim[i] * dim[j] * dim[j+1]
        else:
            for k in range(i, j):
                tmp = table[i][k] + table[k+1][j] + dim[i] * dim[k+1] * dim[j+1]
                if tmp < table[i][j]:
                    table[i][j] = tmp
                    point = k
            dividing_points[i][j] = point

print("The most efficient cost: ", table[0][quantity-1])

# print(dividing_points)
# print(table)

print_tree(0,quantity-1)