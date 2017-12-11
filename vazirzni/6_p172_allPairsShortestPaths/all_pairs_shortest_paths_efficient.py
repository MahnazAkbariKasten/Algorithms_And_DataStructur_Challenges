__author__ = 'pretymoon'

g = [[1], [-1, 2], [2, -1, -1], [5, 5, 1, 3], [-1, -1, 4, -1, 1]]
# g = [[4], [1, -1], [-1, 1, 1]]

n_nodes = len(g) + 1  # number of nodes
n_rows = n_nodes
n_col = n_nodes - 1
n_k = n_nodes + 1   # number of iteration before finding all_pair_shortest_path, one for direct connection without
                    # any nodes in between, and after that add one node at at time ( in each iteration)

dist = []
for i in range(n_rows):
    dist.append([])
    if i < n_rows - 1:
        dist[-1] = [float("inf") for j in range(i+1)]
        dist[-1][i] = 0
    else:
        dist[-1] = [float("inf") for j in range(i)]

for i in range(len(g)):  # iteration number 0, only direct connections through direct edge between two nodes
    for j in range(len(g[i])):
        if g[i][j] > 0:
            dist[i+1][j] = g[i][j]

for k in range(1, n_k):     # iterate over (number of) valid nodes to be used in this iteration
                            # add one node at each iteration to valid nodes
    for i in range(len(dist)):  # for all nodes
        for j in range(len(dist[i])):  # calculate distance from only nodes with smaller index
            if k == n_k - 1 and i == len(dist) - 1:  # no need to compare very last node with itself
                print(k, i)
                break

            if i < k - 1:  # in order to refer to table dist correctly, the larger index has to come first
                left = dist[k-1][i]
            else:
                left = dist[i][k-1]

            if j < k - 1:  # in order to refer to table dist correctly, the larger index has to come first
                right = dist[k-1][j]
            else:
                right = dist[j][k-1]

            tmp = left + right
            if tmp < dist[i][j]:
                dist[i][j] = tmp

for i in range(len(dist)):
    print(dist[i])