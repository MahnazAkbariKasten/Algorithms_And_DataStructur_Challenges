__author__ = 'pretymoon'
n = 20
cuts = [3, 8, 16]
table = [[float("inf") for i in range(n+1)] for j in range(n+1)]
efficient_cut = {}

def min_cost_cut(i, j):
    curr_cuts = []
    for cut in cuts:
        if i < cut < j:
            curr_cuts.append(cut)

    if len(curr_cuts) == 0:
        return 0
    else:
        best_cut = curr_cuts[0]
        for cut in curr_cuts:
            print(i, j, cut)
            tmp = min_cost_cut(i, cut) + min_cost_cut(cut, j) + j - i
            if tmp < table[i][j]:
                table[i][j] = tmp
                best_cut = cut
        efficient_cut[(i, j)] = best_cut
        return table[i][j]

print(min_cost_cut(0, n))
print(efficient_cut)