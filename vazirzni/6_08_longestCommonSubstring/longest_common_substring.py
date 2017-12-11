__author__ = 'pretymoon'

# s1 = "airport"
# s2 = "portal"
s1 = "ppnnn"
s2 = "tppnnn"
len1 = len(s1)
len2 = len(s2)

table = [[0 for i in range(len1)] for j in range(len2)]

longest = 0
sub1 = 0
sub2 = 0

for i in range(len1):
    if s1[i] == s2[0]:
        table[0][i] = 1
        longest = 1
        sub1 = 0
        sub2 = i

for i in range(1, len2):
    if s2[i] == s1[0]:
        table[i][0] = 1
        longest = 1
        sub1 = i
        sub2 = 0

for i in range(1, len1):
    for j in range(1, len2):
        if s1[i] == s2[j]:
            table[j][i] = 1 + table[j-1][i-1]
            if table[j][i] >= longest:
                longest = table[j][i]
                sub1 = j
                sub2 = i

print(sub1, sub2, longest)
if sub1 < sub2:
    print(s1)
    print("-"*(sub2 - sub1), end='')
    print(s2)
else:
    print(s2)
    print("-"*(sub1 - sub2), end='')
    print(s1)