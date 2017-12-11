__author__ = 'pretymoon'

measurements = [(5, 1), (2, 3), (2, 4), (4, 3), (5, 4), (7, 5), (3, 5), (4, 1), (4, 5), (5, 2)]

def is_smaller(m1, m2):
    if m1[0] < m2[0]:
        if m1[1] < m2[1]:
            return True
    return False

# height = [m[0] for m in measurements]
# girth = [m[1] for m in measurements]

measurements.sort()
print(measurements)

groups = []

for m in range(len(measurements)-1, -1, -1):
    for g in groups:
        # print(measurements[m], g)
        if is_smaller(measurements[m], g[-1]):
            g.append(measurements[m])
            break
    else:
        new_group = [measurements[m]]
        groups.append(new_group)

print("\n----- {0} GROUPS -----".format(len(groups)))
for g in groups:
    print(g)
