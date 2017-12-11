__author__ = 'pretymoon'
# g = "{{1}, {-1, 2}, {2, -1, -1}, {5, 5, 1, 3}, {-1, -1, 4, -1, 1}}"
g = [[1], [-1, 2], [2, -1, -1], [5, 5, 1, 3], [-1, -1, 4, -1, 1]]
# g = [[4], [1, -1], [-1, 1, 1]]
n_nodes = len(g) + 1 # 4
n_k = n_nodes + 1 # 5
n_rows = n_nodes # 4
n_cols = n_nodes - 1  # 3

dist = [[[float("inf") for i in range(n_cols)] for j in range(n_rows)] for k in range(n_k)]
dist[0][0][0] = 0
for i in range(1, n_rows): #row
    for j in range(i+1): #col
        if j == i < len(g):
            dist[0][i][j] = 0
        if j < i and g[i-1][j] > 0:
            dist[0][i][j] = g[i-1][j]

for k in range(1, n_k): #depth
    for i in range(n_rows): #row
        if i < n_rows - 1:
            s = i + 1
        else:
            s = i
        for j in range(s): #col
            # k_1 = k - 1
            # print("dist[{k_1}][{i}][{k_1}] + dist[{k_1}][{k}][{j}] = ".format(k_1=k_1, i=i, k=k, j=j), end='')
            # print(dist[k-1][i][k-1], " + ",  dist[k-1][j][k-1])
            if i == n_rows - 1 and k == n_k - 1:
                dist[k][i][j] = dist[k-1][i][j]
                continue

            if i < k - 1:
                left = dist[k-1][k-1][i]
            else:
                left = dist[k-1][i][k-1]
            if j < k - 1:
                right = dist[k-1][k-1][j]
            else:
                right = dist[k-1][j][k-1]
            tmp = left + right

            # tmp = dist[k-1][i][k-1] + dist[k-1][j][k-1]
            # print("k:{k} row:{i}  col:{j}   tmp = {tmp}".format(k=k,i=i,j=j,tmp=tmp))
            #
            # print("-"*20)

            if tmp < dist[k-1][i][j]:
                dist[k][i][j] = tmp
            else:
                dist[k][i][j] = dist[k-1][i][j]

# for k in range(len(dist)):
#     print(dist[k][:][:])
print(dist[-1][:][:])
