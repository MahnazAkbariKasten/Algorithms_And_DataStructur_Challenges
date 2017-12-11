__author__ = 'pretymoon'
import itertools
# g = [[1], [-1, 2], [2, -1, -1], [5, 5, 1, 3], [-1, -1, 4, -1, 1]]
g = [[], [14], [1, 7], [1, 1, 1]]
myPoints = [i for i in range(len(g))]

def length(point1, point2):
    if point1 == point2:
        return 0
    elif point1 > point2:
        return g[point1][point2]
    else:
        return g[point2][point1]


def solve_tsp_dynamic(points):
    #calc all lengths
    all_distances = [[length(x, y) for y in points] for x in points]
    print("--- all_distances ---")
    for row in all_distances:
        print(row)
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0, idx+1]) for idx, dist in enumerate(all_distances[0][1:])}
    print("--- A ---")
    print(A)
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j}, k)][0] + all_distances[k][j], A[(S-{j}, k)][1] +
                                   [j]) for k in S if k != 0 and k!=j])
                                   #this will use 0th index of tuple for ordering,
                                   # the same as if key=itemgetter(0) used
        print("--- B ---")
        print(B)
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]

print()
print("--- result ---\n", solve_tsp_dynamic(myPoints))

# def all_subsets(mySet):
#     all = []
#     for i in mySet:
#         all.append(set(i))
#
# print(all_subsets(points_set))